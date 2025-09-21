웹 브라우저로 테이블을 조회하는 예제

Flask_mono.py : Python + Flask + jinja를 이용하여 프론트와 백엔드를 하나의 프로그램 모듈로 만든 예제. (Monolithic 구조)
templates folder : jinja의 html template 폴더

실행 : python Flask_mono.py  (http://localhost:5000)


Flask_BE.py : Flask를 이용한 Back-end 서버.
frontend folder : react front-end 프로젝트 폴더. src\app.js :예제 app 코드 파일

실행 방법 
react project 생성 : npx create-react-app frontend (at working directory, webserever)
cd frontend
npm start

python Flask_BE.py (백엔드 서버가 실행되고 있어야 함)

http://localhost:3000

*** 2가지 모두 mariaDB의 sample database (쇼핑몰 예제 데이터베이스)를 사용.

webserver/FlaskOnly/flaskonly : flask에서 react를 host해서 serving

npx create-react-app flaskonly
cd flaskonly
npm start <=== development mode로 실행.
npm run build <=== static build (flask 에서 hosting할 수 있도록)