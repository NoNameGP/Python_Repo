# 뷰우미 : 저시력장애인을 위한 객체인식기반 AR 보행 앱

<div align="center"><img src="https://github.com/NoNameGP/Python_Repo/assets/106591445/7e7e2bf4-1a9a-436f-8f68-7aa3f6ea0883"/></div>

## 📆 프로젝트 일정
기획 기간 : 2022.12 ~ 2023.02
개발 기간 : 2023.03 ~ 2023.10

## 🫂팀원
<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://github.com/kchaeys2"><img src="https://avatars.githubusercontent.com/u/106591445?v=4" width="150px;" alt=""/><br /><b>김채연</b></a><br /></td>
      <td align="center"><a href="https://github.com/Pjh01"><img src="https://avatars.githubusercontent.com/u/64469496?v=4" width="150px;" alt=""/><br /><b>박주하</b></a><br /></td>
      <td align="center"><a href="https://github.com/Hyyeb"><img src="https://avatars.githubusercontent.com/u/64469496?v=4" width="150px;" alt=""/><br /><b>이혜빈</b>
</a><br /></td>
<br /></td>
      <td align="center"><a href="https://github.com/ohyojin"><img src="https://avatars.githubusercontent.com/u/124988190?v=4" width="150px;" alt=""/><br /><b>오효진</b>
</a><br /></td>
     <tr/>
      <td align="center">Backend & Object Detection</td>
      <td align="center">Frontend & AR </td>
      <td align="center">Frontend</td>
      <td align="center">Design</td>
    </tr>
  </tbody>
</table> 

## 🐈기술 스택
**Framework**
- Python 3.10
- flask 2.7
  
**Dependencies**
- opencv
- ultralytics
- flask-socketio
- Flask-Migrate
- Flask-SQLAlchemy

**Infra**
- AWS EC2

**Database**
- sqlite

## 📁 Package Structure
- Image : 사진
- YOLO-Weights : Yolo 학습 모델
- studycrud : flaks 서버 구축을 위한 공부 패키지
- test
  - templates : 사물인식 결과 test html
  - main.py : YOLO를 통한 사물인식 및 socket활용을 통한 실시간 데이터 전달
  - video.py : 사물인식 결과 비디오로 저장 (미사용)


## 💾 데이터베이스 ERD
![erd](https://github.com/NoNameGP/Python_Repo/assets/106591445/775aa3f6-6b70-4dd9-a150-6effeb13ef09)
* JAVA에서 flask로 이전 중
