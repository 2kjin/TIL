# 220715 git

- git ( 로컬 저장소)
  - working directory
    - 작업하고 있는 장소
  - staging area
    - 정제하는곳 ( 휴지통 같은 정제 하는 단계)
  - commits
    - 버전에 대한 기록
    - 협업을 위해 남들도 보기 편하게 기록
- branch
  -  작업공간





- git-scm - documentation : 명령어 참고

- toptal.com/developers/gitignore : 추가 하지 않을 명령어들

  - python, windoes. visualstudiocode 등 사용할 프로그램 검색 후 생성
  - 프로젝트 시작 전에 나오는 명령어들 .gitignore 메모장에 넣어두기
    - *.so
      - so로 끝나는 모든 프로그램 무시

- 파일 이름을 README.md로 만들어서 push 하면 깃허브 메인에 보여요!

- git을 시작할때 git pull 하는 습관 들이기 ( 기존 github에 있는 자료들 다운받고 시작)

  - git push가 되지 않을때 (파일이 이쁠때)

    1. git pull로 merge 확인후

    2. :wq 명령어로 나가고

    3.  다시 git push 하기

  - 파일이 이쁘지 않을때

    - git pull로 merge 확인후
    - status 로 충돌 파일 확인 후 code로 해당폴더 열어 수정 후
    - add, commit, push 하면 된다.
      - accept current change : 현재 있는것이 맞다
      - accept both change  : 둘다 맞다

- bash 에서 붙여넣기 : shift + insert



## 초기 설정 (최초 1회)

- git config --global user.name {user.name}
- git config --global user.email {user.email}
- git config --global -l
  - name, email 설정값 확인

- git init
  - 해당 디렉토리를 git으로 관리하기 시작
- git add .
  - 변경 사항이 존재하는 해당 디렉토리의 모든 파일/폴더를 staging area로 이동

- git status
  -  현재 디렉토리 내의 git 관리 상태를 확인
- git add file_name
  - git 중 staging area 에 올리는것
- ctrl + l
  - 화면 지우기
- git commit -m 'commit message'
  - commit message 라는 메세지와 함께 버전을 기록
    - 어떤 변경 사항이 있었는지를 기록
  - git commit
    - vim 에디터가 나옴
    - i -> insert 모드 
    - esc 후 `:wq` 명령어 치면 밖으로 나와진다 .

- git log
  - 커밋의 기록을 확인



-  파일 변경 했을때
  - git status 를 치면 빨간 modified < 변경사항이 있는데 마지막 commit에 비해서 새로운 사항이 staging area 에 없다
  - 확인 후 git add 파일이름 
    - 아니면 git add . 
      - 현재 상태에 있는 모든아이들을 staging area 에 올려줘
  - git commit - m ''
    - '' 안에 있는 내용은 변경사항 기록
- 필요한 정보만 보고싶을때
  - git log --oneline
  - git log --oneline --graph
    - 그래프로 보기

- git log -1
  - 하나만 보여주기
  - -2 : 두개



## gib hun 에 업로드

- git remote add origin https://github.com/2kjin/git-practice
  - 내 git과 github repositories 연결
  - origin =  https://github.com/2kjin/git-practice 라 명명
- git push origin master
  - master 로 설정
- git push -u origin master
  -  -u : --set--upstram
    - -u = master를 origin에 올린다라고 명명하여
    - 다음부턴 git push 라고만 쳐도 된다



## git hub 로부터 다운로드

- git clone [주소]
  - 가져올 repositories의 주소 code 누르면 있다
  - 초기 다운로드 할 곳 설정
    - git clone [주소] .
      - 이 위치에다가 repositories를 바로 가져온다
- git pull 
  - 다운로드



- git 주의 사항
  - git 안에 git 설정 금지
  - 큰 용량 저장이 되지 않으므로
  - 메인 디렉토리에 설정 금지



## 새롭게 설정 파일 만들기

넣고 싶지 않은 정보 빼기

1. touch .gitignore 만들기
2. start .gitignore 후 메모장으로 열기
3. 업로드 원치 않는 파일 명쓰기
   - 추가 하고 싶다면 엔터로 추가

- .gitignore 이란 명령어는 맨 처음 git add 하기 전에 만들어 놔야 적용 가능

