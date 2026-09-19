"""
GitHub 자동 업로더 스크립트 (GitHub REST API 기반)
별도의 Git 설치 없이 GitHub Personal Access Token(PAT)을 이용해
elainee8900-commits/prideandprejudice 레포지토리에 파일을 커밋/업로드합니다.
"""

import os
import sys
import json
import base64
import urllib.request
import urllib.error
import getpass

REPO_OWNER = "elainee8900-commits"
REPO_NAME = "prideandprejudice"
BRANCH = "main"

FILES_TO_UPLOAD = [
    "IL.html",
    "index.html",
    "README.md",
    "server.py"
]

def upload_file(file_path, file_name, token):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{file_name}"
    
    with open(file_path, "rb") as f:
        content_bytes = f.read()
    
    content_b64 = base64.b64encode(content_bytes).decode("utf-8")
    
    # Check if file already exists to get its SHA (for update)
    sha = None
    try:
        check_req = urllib.request.Request(
            url,
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github.v3+json",
                "User-Agent": "Antigravity-Uploader"
            }
        )
        with urllib.request.urlopen(check_req) as resp:
            data = json.loads(resp.read().decode())
            sha = data.get("sha")
    except urllib.error.HTTPError:
        sha = None

    payload = {
        "message": f"Upload {file_name} - 중학생 문해력 & 정보문해력 5분 진단 웹앱",
        "content": content_b64,
        "branch": BRANCH
    }
    if sha:
        payload["sha"] = sha

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json",
            "User-Agent": "Antigravity-Uploader"
        },
        method="PUT"
    )

    try:
        with urllib.request.urlopen(req) as resp:
            print(f"  [OK] {file_name} 업로드 성공!")
            return True
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode()
        print(f"  [FAIL] {file_name} 업로드 실패 (HTTP {e.code}): {err_msg}")
        return False

def main():
    print("=" * 65)
    print(f" GitHub 업로더: {REPO_OWNER}/{REPO_NAME}")
    print("=" * 65)
    
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        # Check ~/.env
        env_path = os.path.expanduser("~/.env")
        if os.path.exists(env_path):
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("GITHUB_TOKEN="):
                        token = line.strip().split("=", 1)[1]
                        break

    if not token:
        print("\nGitHub Personal Access Token (PAT)이 필요합니다.")
        print("(토큰 발급: https://github.com/settings/tokens - 'repo' 권한 체크)")
        token = getpass.getpass("GitHub Token 입력 (화면에 표시되지 않음): ").strip()

    if not token:
        print("토큰이 입력되지 않아 작업을 취소합니다.")
        return

    base_dir = os.path.dirname(os.path.abspath(__file__))
    success_count = 0

    print(f"\n[1/2] '{BRANCH}' 브랜치로 파일 업로드를 시작합니다...")
    for fname in FILES_TO_UPLOAD:
        fpath = os.path.join(base_dir, fname)
        if os.path.exists(fpath):
            if upload_file(fpath, fname, token):
                success_count += 1
        else:
            print(f"  [SKIP] 파일이 존재하지 않음: {fname}")

    print("\n" + "=" * 65)
    if success_count == len(FILES_TO_UPLOAD):
        print(f"  축하합니다! 총 {success_count}개 파일이 성공적으로 업로드되었습니다.")
        print(f"  저장소 확인: https://github.com/{REPO_OWNER}/{REPO_NAME}")
        print("=" * 65)
    else:
        print(f"  일부 파일 업로드 완료 ({success_count}/{len(FILES_TO_UPLOAD)})")
        print("=" * 65)

if __name__ == '__main__':
    main()
