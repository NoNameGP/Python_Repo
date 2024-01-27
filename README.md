# 뷰우미 : 저시력장애인을 위한 객체인식기반 AR 보행 앱

<div align="center"><img src="https://github.com/NoNameGP/Python_Repo/assets/106591445/7e7e2bf4-1a9a-436f-8f68-7aa3f6ea0883"/></div>

## 📆 프로젝트 일정
기획 기간 : 2022.12 ~ 2023.02
<br/>집중 개발 기간 : 2023.03 ~ 2023.10
<br/>유지 보수 기간 : 2023.12 ~

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
- Flask-login
- Flask-Bcrypt

**Database**
- sqlite

## 📁 Package Structure
- YOLO-Weights : 학습된 YOLO 모델
- controllers
- dto
- instance : DB파일
- migrations : DB 변경 사항
- models
- routes : controllers API 등록 계층
- services
- test : YOLO 실행 test 폴더 

## 💾 데이터베이스 ERD
![erd](https://github.com/NoNameGP/Python_Repo/assets/106591445/69b8832e-f3f5-4c89-8a36-a6a177f530f7)

## 최적의 길찾기 알고리즘
![viewMe 알고리즘](https://github.com/NoNameGP/Python_Repo/assets/106591445/1796955e-5847-4340-b566-a03a7ec43277)

