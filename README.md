# TCP-IP_project
Title: OX퀴즈<br>
개발인원 : 201744076 김지용<br>
제 프로젝트는 교안에 나와있던 채팅방 코드를 응용해<br> 
OX퀴즈 기능까지 더해 사람들이 OX퀴즈와 채팅을 동시에 즐길 수 있게 설계하였습니다.<br>
<br>

사용환경 <br>
1.Python <br>
2.GUI <br>
3.Socket 통신 <br>
4.멀티 쓰레드

설계의도 <br>
기존 채팅방 코드에 <br>
서버에서 모든 유저한테 공지와 퀴즈를 던져주는 send_all_message 함수<br>
서버에서 답을 제출한 유저한테만 결과를 알려주는 send_one_clients 함수<br>
를 추가해 채팅과 동시에 퀴즈를 즐길수 있도록 설계하였습니다.<br>
또한, 퀴즈를 맞추는 중간에도 채팅기능이 제대로 작동되게끔 멀티 쓰레드를 사용하여<br>
채팅과 퀴즈를 동시에 즐길 수 있습니다.<br>
그 외에도 소스코드에 주석이 작성되어 쉽게 구조를 파악할 수 있습니다.<br>
![image](https://user-images.githubusercontent.com/71188378/122051856-03070880-ce20-11eb-92e5-6bb96d879572.png)


실행화면<br>
처음 클라이언트를 실행했을때의 화면 입니다.<br>
이상태에서 아무것도 입력하지 않고 엔터를 치면 127.0.0.1로 연결됩니다.<br>
(포트는 코드에서 2500으로 설정되었습니다.)<br>
![image](https://user-images.githubusercontent.com/71188378/122154468-0e9a1400-cea0-11eb-860c-1da8f5f07424.png)


서버를 실행하고 한유저가 접속했을때의 상황입니다.유저가 <br>
두명이상일 때만 퀴즈가 시작되기 때문에 한명의 유저는 채팅을 치는 상황입니다.<br>
![image](https://user-images.githubusercontent.com/71188378/122154506-207bb700-cea0-11eb-9168-0267cda186b5.png)

유저 수가 두명이 되자마자 퀴즈가 시작됩니다.<br>
![image](https://user-images.githubusercontent.com/71188378/122154554-34bfb400-cea0-11eb-9682-1dbc76dcef65.png)

<br>'O' , 'X'를 입력하여 정답을 제출할 수 있습니다. <br>
정답입니다 혹은 오답입니다 메세지는 답을 제출한 본인에게만 보여지게끔 설계되었습니다.<br>
다른 유저는 상대가 O 또는 X를 쓴것 만 보입니다. <br>
![image](https://user-images.githubusercontent.com/71188378/122154593-4b660b00-cea0-11eb-9407-f9315624693a.png)

4개의 퀴즈를 풀고난 상황입니다.<br>
퀴즈의 제한시간을 늘려야 한다면 Time.sleep()의 시간을 늘리면 해결됩니다.<br>
![image](https://user-images.githubusercontent.com/71188378/122156150-5ff7d280-cea3-11eb-9c3e-fd744bd3a693.png)



