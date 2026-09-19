"""
사이버 팩트체커 (IL.html) 로컬 테스트 서버
Python 3 내장 http.server를 활용하여 브라우저에서 편리하게 테스트할 수 있습니다.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/IL.html"
        print("=" * 60)
        print(" [코드네임: 팩트체커] 로컬 테스트 서버가 실행되었습니다.")
        print(f" 접속 주소: {url}")
        print(" 종료하려면 터미널에서 Ctrl + C 를 누르세요.")
        print("=" * 60)
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n서버를 종료합니다.")
            httpd.server_close()

if __name__ == '__main__':
    run()
