# DEVOPS 연습

## 실행 환경

### Local
- Ubuntu 20.04

- Python 3.8.10

## Service 소개
1. Draw (draw.py)

    도커 고래 로고가 움직이는 애니메이션

2. Detect (detect.py)

    YOLO와 Flask를 활용한 객체 탐지 서비스

## Git Hooks / Github Action

### Git Hooks
- pre-commit
    
    commit 전 draw_test.py와 detect_test.py를 실행하여 오류없이 통과 시 commit

    - draw_test.py

        1. 첫번째 frame이 동일한지 확인
        2. 두번재 frame이 동일한지 확인

    - detect_test.py

        1. YOLO 모델이 정상적으로 호출되는지 확인
        2. test_img.jpg로 정상적으로 객체 탐지가 되는지 확인
        

### Github Action

- main.yml

    1. push와 pull_request 이벤트 발생 시 작동
    2. ubuntu 20.04, python 3.8 환경
    3. dependency 설치 (ultralytics flask)
    4. draw_test.py와 detect_test.py를 실행하여 테스트
    5. 
        - draw와 detect 이미지 빌드
        - github secrets에 설정해둔 docker hub id와 pw로 로그인
        - draw와 detect 이미지 docker hub에 push

## Docker

- Draw
    - 환경
        - Ubuntu 20.04

        - Python 3.8.10

    - 빌드
        ```bash
        $ docker build -t draw:latest -f Dockerfile.draw .
        ```

    - 실행
        ```bash
        $ docker run -it draw:latest
        ```

- Detect
    - 환경
        - Ubuntu 23.04

        - Python 3.11.2
    - 빌드

        ![주의]빌드 시 10분가량 소모 
        ```bash
        $ docker build -t detect:latest -f Dockerfile.detect .
        ```

    - 실행

        업로드된 이미지와 detect된 이미지 저장소 마운트, 로컬 5000번 포트와 컨테이너 5000번 포트 연결
        ```bash
        $ docker run -it -v ./static:/app/static -p 5000:5000 detect:latest
        ```

 ## Docker Swarm

- 실행
    ```bash
    $ docker service create --name detect_service --replicas=3 -p 5000:5000 --mount type=bind,source=./static,target=/app/static -t -d detect:latest
    ```

