# ⚡ 코드네임: 팩트체커 (Secret Fact-Checker)
### 중학생 문해력(PISA) & 정보 문해력(Big 6 Skills) 게이미피케이션 5분 측정 시스템

본 프로그램은 중학생들이 시험처럼 느끼지 않고 5분 동안 흥미진진한 정보 탐정 퀘스트를 수행하면서 자신의 **문해력(PISA 읽기 기준)**과 **정보 문해력(Big 6 Skills 기준)**을 자가 진단할 수 있도록 제작된 웹 애플리케이션입니다.

---

## 📁 파일 구성
- `IL.html` : 웹 애플리케이션 메인 파일 (HTML/CSS/JS 및 Web Audio 사운드 신시사이저 내장, 오프라인 단독 실행 가능)
- `index.html` : 깃허브 페이지(GitHub Pages) 배포 시 기본 메인 페이지로 자동 인식되는 파일 (`IL.html`과 동일)
- `server.py` : 파이썬 원클릭 로컬 테스트 서버 스크립트
- `README.md` : 프로젝트 매뉴얼 및 가이드

---

## 🎮 게임 및 평가 구성

### 1. 5분 미션 시나리오
송도 스마트 시티에서 발생한 *'AI 자율주행 버스 7호차 정지 사건'*을 둘러싼 인터넷 괴담과 가짜 뉴스를 5분 안에 팩트체크하여 사건의 전말을 밝혀내는 임무입니다.

### 2. 단계별 Big 6 Skills & PISA 문해력 매핑
| 스테이지 | 미션 명칭 | Big 6 Skills 영역 | PISA 읽기 인지 프로세스 |
| :--- | :--- | :--- | :--- |
| **Stage 1** | 사건 의뢰서 암호 해독 | **1. 과제 정의 (Task Definition)** | 정보 접근 및 검색 (Locating) |
| **Stage 2** | 정보원 신뢰도 감별 레이더 | **2. 정보 탐색 전략 (Seeking Strategies)** | 평가 및 성찰 (Reflecting) |
| **Stage 3** | 사이버 검색 시뮬레이터 | **3. 위치 파악 및 접근 (Location & Access)** | 정보 접근 및 검색 (Locating) |
| **Stage 4** | 돋보기 팩트체커: 왜곡 적발 | **4. 정보 활용 (Use of Information)** | 텍스트 이해 및 비판적 성찰 |
| **Stage 5** | 사건의 전말: 타임라인 조립 | **5. 정보 통합 (Synthesis)** | 텍스트 이해 및 종합적 추론 |
| **Stage 6** | 요원 디브리핑 (자기 평가) | **6. 평가 및 반성 (Evaluation)** | 평가 및 성찰 (Reflecting) |

### 3. PISA 읽기 문해력 성취수준 환산 기준
- **Level 6 (90점 이상)**: 최상위 비판적 디지털 문해력 (복합적 텍스트의 미묘한 편향성과 오류를 완벽 분석)
- **Level 5 (80~89점)**: 탁월한 비판적·탐색적 문해력 (다각도 출처 검증 및 논리정연한 정보 통합)
- **Level 4 (70~79점)**: 능숙한 문제해결형 문해력 (적절한 검색식 설계 및 명확한 인과관계 도출)
- **Level 3 (55~69점)**: 보통 수준의 디지털 문해력 (중학생 기준선 - 일반적인 사실관계 파악)
- **Level 2 (40~54점)**: 기본 문해력 (사회적 요구 최소기준 - 표면적 정보 식별 가능)
- **Level 1 (40점 미만)**: 기초 문해력 보완 권장 (키워드 추출 및 출처 구별 훈련 필요)

---

## 💻 실행 및 오프라인 테스트 방법

### 방법 A. 가장 간단한 실행 (오프라인 더블클릭)
1. `USB` 폴더 내의 `IL.html` 파일을 더블클릭합니다.
2. 크롬(Chrome), 엣지(Edge) 등 웹 브라우저에서 인터넷 연결 없이 즉시 100% 정상 작동합니다.
3. 내장된 **Web Audio API**를 통해 별도 음원 파일 없이도 경쾌한 효과음과 비프음이 출력됩니다.

### 방법 B. 파이썬 로컬 서버로 실행
터미널(PowerShell 또는 명령 프롬프트)에서 아래 명령어를 실행합니다:
```bash
python server.py
```
자동으로 브라우저가 열리며 `http://localhost:8000/IL.html`로 접속됩니다.

---

## 🌐 깃허브(GitHub) 배포 방법 (GitHub Pages)

인터넷상에서 학생들이 링크만 클릭하여 접속하게 하려면 깃허브 무료 웹 호스팅(GitHub Pages)을 사용합니다:

1. **GitHub 저장소(Repository) 생성**:
   - [github.com](https://github.com)에 로그인 후 새 레포지토리(예: `middle-school-literacy-game`)를 생성합니다 (Public 설정).
2. **파일 업로드**:
   - `USB` 폴더 안의 `index.html`, `IL.html`, `README.md` 파일을 GitHub 웹페이지의 [Add file] -> [Upload files]를 통해 드래그 앤 드롭으로 업로드하고 `Commit changes`를 누릅니다.
   - (또는 Git CLI 사용: `git init` -> `git add .` -> `git commit -m "Initial commit"` -> `git push origin main`)
3. **GitHub Pages 활성화**:
   - GitHub 저장소 상단 메뉴의 **Settings** 클릭
   - 좌측 메뉴의 **Pages** 클릭
   - **Branch** 섹션에서 `None`을 `main`(또는 `master`)으로 변경하고 `/ (root)` 선택 후 **Save** 클릭
   - 1~2분 뒤 생성되는 배포 주소(예: `https://<깃허브아이디>.github.io/<저장소이름>/`)로 접속하면 전 세계 어디서든 학생들이 접속할 수 있습니다!

---

## 🔥 파이어베이스(Firebase) 데이터베이스 연동 방법

학생들이 푼 결과(이름, 학급, 점수, PISA 레벨, Big 6 세부 점수)를 교사/관리자가 실시간으로 모아보려면 파이어베이스 Firestore를 연동할 수 있습니다.

1. [Firebase 콘솔](https://console.firebase.google.com/)에 구글 계정으로 로그인합니다.
2. **프로젝트 추가**를 클릭하고 새 프로젝트를 만듭니다 (예: `school-literacy`).
3. 좌측 메뉴에서 **빌드 > Firestore Database**로 이동하여 **데이터베이스 만들기**를 누릅니다.
   - 보안 규칙 설정 시 **테스트 모드에서 시작**을 선택합니다.
4. 프로젝트 홈 화면에서 **웹 아이콘(`</>`)**을 클릭하여 웹 앱을 등록합니다.
5. 화면에 나타나는 `firebaseConfig` 객체 코드를 복사합니다:
   ```json
   {
     "apiKey": "AIzaSy...",
     "authDomain": "school-literacy.firebaseapp.com",
     "projectId": "school-literacy",
     "storageBucket": "school-literacy.appspot.com",
     "messagingSenderId": "...",
     "appId": "..."
   }
   ```
6. `IL.html` 화면 우측 상단의 **설정 아이콘(⚙️)**을 누르고 복사한 JSON 코드를 붙여넣은 뒤 **[설정 저장]**을 누르면 완료됩니다!
   - 설정 후 게임이 끝나면 Firestore의 `il_literacy_results` 컬렉션에 실시간으로 데이터가 저장됩니다.
   - 미설정 상태이거나 오프라인일 때는 브라우저 `localStorage`에 자동 보관되며 **[📥 결과 CSV 다운로드]** 버튼으로 언제든지 엑셀 파일로 내려받을 수 있습니다.
