# Python version control system
A proof-of-concept version control system for a school project.

## 디자인
실행 디렉토리에 폴더 .pvcshist와 평문 파일 .pvcsconfig, .pvcsignore를 생성한다.

pvcshist 폴더 내에는 각 코밋 시의 프로젝트를 통째로 복사하여 저장한다(닷파일 제외)

pvcsconfig에는 추적할 파일의 워킹 디렉토리부터의 경로를 저장한다.

pvcsignore에는 변화를 무시할 파일의 경로를 저장한다.

추가해야 할 사항 파일 복사, 디렉토리 복사(파일복사와 함계 코밋시 파일 저장), 파일 변경점 검사, 히스트에서 파일 되돌리기
