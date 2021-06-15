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
![image](https://user-images.githubusercontent.com/71188378/122050519-7c9df700-ce1e-11eb-90d4-c6a7f6a2a5b3.png)

서버를 실행하고 한유저가 접속했을때의 상황입니다.유저가 <br>
두명이상일 때만 퀴즈가 시작되기 때문에 한명의 유저는 채팅을 치는 상황입니다.<br>
![image](https://user-images.githubusercontent.com/71188378/122050690-aa833b80-ce1e-11eb-8c75-a2dae13c44b7.png)

유저 수가 두명이 되자마자 퀴즈가 시작됩니다.<br>
![image](https://user-images.githubusercontent.com/71188378/122050867-e5856f00-ce1e-11eb-84f1-0128acc93a0b.png)

4개의 퀴즈를 풀고난 상황입니다.<br>
보시다시피 정답입니다 혹은 오답입니다 메세지는 답을 제출한 본인에게만 보여지게끔 설계되었습니다.<br>
![image](https://user-images.githubusercontent.com/71188378/122051096-28dfdd80-ce1f-11eb-95aa-d5da91a06ce9.png)


