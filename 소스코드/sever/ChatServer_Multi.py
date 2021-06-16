import time
from socket import *
from threading import *

class MultiChatSever:
    clients = []#리스트 선언
    final_received_message = ""#메세지 저장 변수 선언

    OXquiz=['1+1=2 은 True인가?','자바는 객체지향 언어다','UDP는 신뢰성이 보장된다.','김지용의 학점은 F다']#퀴즈
    OXquizAnswer = ['O','O','X','X']#퀴즈정답
    OXquiznotAnswer = ['X', 'X', 'O', 'O']#퀴즈오답
    OXquiznum= 0#몇번째 퀴즈가 진행중인지 체크해주는 변수

    def __init__(self):
        self.s_sock = socket(AF_INET, SOCK_STREAM)# 소켓 객체 생성
        self.ip = '127.0.0.1'#IP
        self.port = 2500#포트번호
        self.s_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)#
        self.s_sock.bind((self.ip, self.port))#bind 항수를 통해 생성된 소켓을 특정호스트와 포트에 연결
        print("Waiting for clients...")#메세지 출력
        self.s_sock.listen(100)#Socket을 수신상태로 둡니다.
        self.accept_client()#밑에 정의된 accept_client()함수 실행

    def accept_client(self):#유저를 추가하는 함수
        while True:#무한반복 
            client = c_socket, (ip, port)= self.s_sock.accept()#연결수락
            if client not in self.clients:#만약 clients리스트에 없으면
                self.clients.append(client)#clients 리스트에 추가
            if len(self.clients) >= 2:#유저가 2명이상이면 퀴즈시작
                a = "start"#함수에 스타트메세지
                th = Thread(target=self.send_all_message, args=(a,))
                #퀴즈의 제한시간과 메세지를 받는 함수는 동시에 돌아야함으로 쓰레드사용
                th.start()
            print('{0}:{1} 접속'.format(ip, port))#프린트 문으로 유저가 출입할때마다 메세지출력
            t = Thread(target=self.receive_messages, args=(c_socket,))#쓰레드가 실행할 함수를 target으로 지정 입력파라미터는 args에 입력
            t.start()#쓰레드 실행
            #유저를 받는것과 메세지전송은 동시에 이루어져야함으로 멀티쓰레드 방식으로 다중실행한다.

    def receive_messages(self, c_socket):#메세지를 받는함수
        while True:
            try:
                incoming_message = c_socket.recv(1024)#클라이언트로 부터 받은 메세지 저장
                if not incoming_message:#아무것도 없으면
                    break#나간다
            except: #오류가 발생하면
                continue #다시 While 문으로
            else:#오류가 없으면
                if self.OXquiznum==1:#1번퀴즈 1+1=2 은 True인가?
                    result = incoming_message.decode('utf-8')#유저가 보낸메세지를
                    if result[len(result)-1:] == self.OXquizAnswer[0]:#가장 뒤의 글자만 잘라내 정답인지  판단
                        self.send_one_clients(c_socket,"T")#정답이면 T
                    if result[len(result)-1:]  == self.OXquiznotAnswer[0]:#정답이 아니면
                        self.send_one_clients(c_socket,"F")#F
                if self.OXquiznum==2:#2번퀴즈 자바는 객체지향 언어다
                    result = incoming_message.decode('utf-8')
                    if result[len(result)-1:] == self.OXquizAnswer[1]:
                        self.send_one_clients(c_socket,"T")
                    if result[len(result)-1:]  == self.OXquiznotAnswer[1]:
                        self.send_one_clients(c_socket,"F")
                if self.OXquiznum==3:#3번퀴즈 UDP는 신뢰성이 보장된다.
                    result = incoming_message.decode('utf-8')
                    if result[len(result)-1:] == self.OXquizAnswer[2]:
                        self.send_one_clients(c_socket,"T")
                    if result[len(result)-1:]  == self.OXquiznotAnswer[2]:
                        self.send_one_clients(c_socket,"F")
                if self.OXquiznum==4:#김지용의 학점은 F다
                    result = incoming_message.decode('utf-8')
                    if result[len(result)-1:] == self.OXquizAnswer[3]:
                        self.send_one_clients(c_socket,"T")
                    if result[len(result)-1:]  == self.OXquiznotAnswer[3]:
                        self.send_one_clients(c_socket,"F")

                self.final_received_message = incoming_message.decode('utf-8')#온메세지를 디코딩
                print(self.final_received_message)#메세지를 프린트문 으로 출력
                self.send_all_clients(c_socket)# send_all_clients() 함수실행
        c_socket.close()# 소켓 닫기

    def send_all_clients(self, senders_socket):#메세지를 다른 유저를에게 전송하는 함수
        for client in self.clients:#clients 리스트의 유저 수만큼 유저 순서대로
            socket, (ip, port) = client#유저 정보
            if socket is not senders_socket:#지금 전송한 유저가 아닐시
                try:#실행
                    socket.sendall(self.final_received_message.encode('utf-8'))#모든 유저에게 메세지를 인코딩하여 전송
                except:#오류발생시
                    self.clients.remove(client)#유저 삭제
                    print("{},{} 연결이 종료되었습니다.".format(ip, port))#메세지 출력

    def send_one_clients(self, senders_socket, event):#퀴즈 결과를 제출했던 유저에게만 보여주는 함수

        if event == "T":#정답일시
            for client in self.clients:  # clients 리스트의 유저 수만큼 유저 순서대로
                socket, (ip, port) = client  # 유저 정보
                if socket is senders_socket:  # 지금 전송한 유저 일시
                    try:  # 실행
                        result_message= '당신은 정답입니다.'
                        socket.sendall(result_message.encode('utf-8'))  # 모든 유저에게 메세지를 인코딩하여 전송
                    except:  # 오류발생시
                        self.clients.remove(client)  # 유저 삭제
                        print("{},{} 1번문제  T연결이 종료되었습니다.".format(ip, port))  # 메세지 출력

        if event == "F":#오답일시
            for client in self.clients:  # clients 리스트의 유저 수만큼 유저 순서대로
                socket, (ip, port) = client  # 유저 정보
                if socket is senders_socket:  # 지금 전송한 유저 일시
                    try:  # 실행
                        result_message = '당신은 정답이 아닙니다.'
                        socket.sendall(result_message.encode('utf-8'))  # 모든 유저에게 메세지를 인코딩하여 전송
                    except:  # 오류발생시
                        self.clients.remove(client)  # 유저 삭제
                        print("{},{} 1번문제 F 연결이 종료되었습니다.".format(ip, port))  # 메세지 출력



    def send_all_message(self, event):#모든 유저에게 메세지 전송
        if event == "start":
            try:#실행
                for client in self.clients:  # clients 리스트의 유저 수만큼 유저 순서대로
                    start_message = '퀴즈를 시작합니다'+'\n'
                    socket, (ip, port) = client  # 유저 정보
                    socket.sendall(start_message.encode('utf-8'))#모든 유저에게 메세지를 인코딩하여 전송
                a = "quiz1"
                self.send_all_message(a)
            except:#오류발생시
                print("오류발생.")#메세지 출력
        if event == "quiz1":
            try:
                self.OXquiznum=1
                for client in self.clients:  # clients 리스트의 유저 수만큼 유저 순서대로
                    quiz_message = self.OXquiz[0]
                    socket, (ip, port) = client  # 유저 정보
                    socket.sendall(quiz_message.encode('utf-8'))  # 모든 유저에게 메세지를 인코딩하여 전송
                    quiz_message = '15초뒤 다음 퀴즈로 넘어갑니다.'
                    socket.sendall(quiz_message.encode('utf-8'))  # 모든 유저에게 메세지를 인코딩하여 전송

                time.sleep(15)#제한시간 15초
                b = "quiz2"#15초가 지나면
                self.send_all_message(b)#다음퀴즈로
            except:
                print('오류발생')
        if event == "quiz2":
            try:
                self.OXquiznum=2
                for client in self.clients:  # clients 리스트의 유저 수만큼 유저 순서대로
                    quiz_message = self.OXquiz[1]
                    socket, (ip, port) = client  # 유저 정보
                    socket.sendall(quiz_message.encode('utf-8'))  # 모든 유저에게 메세지를 인코딩하여 전송
                    quiz_message = '15초뒤 다음 퀴즈로 넘어갑니다.'
                    socket.sendall(quiz_message.encode('utf-8'))  # 모든 유저에게 메세지를 인코딩하여 전송

                time.sleep(15)
                b = "quiz3"
                self.send_all_message(b)
            except:
                print('오류발생')
        if event == "quiz3":
            try:
                self.OXquiznum=3
                for client in self.clients:  # clients 리스트의 유저 수만큼 유저 순서대로
                    quiz_message = self.OXquiz[2]
                    socket, (ip, port) = client  # 유저 정보
                    socket.sendall(quiz_message.encode('utf-8'))  # 모든 유저에게 메세지를 인코딩하여 전송
                    quiz_message = '15초뒤 다음 퀴즈로 넘어갑니다.'
                    socket.sendall(quiz_message.encode('utf-8'))  # 모든 유저에게 메세지를 인코딩하여 전송

                time.sleep(15)
                b = "quiz4"
                self.send_all_message(b)
            except:
                print('오류발생')
        if event == "quiz4":
            try:
                self.OXquiznum=4
                for client in self.clients:  # clients 리스트의 유저 수만큼 유저 순서대로
                    quiz_message = self.OXquiz[3]
                    socket, (ip, port) = client  # 유저 정보
                    socket.sendall(quiz_message.encode('utf-8'))  # 모든 유저에게 메세지를 인코딩하여 전송
                    quiz_message = '15초뒤 다음 퀴즈로 넘어갑니다.'
                    socket.sendall(quiz_message.encode('utf-8'))  # 모든 유저에게 메세지를 인코딩하여 전송

                time.sleep(15)
                b = "end"
                self.send_all_message(b)
            except:
                print('오류발생')
        if event == "end":
            for client in self.clients:  # clients 리스트의 유저 수만큼 유저 순서대로
                quiz_message = '퀴즈 끝'
                socket, (ip, port) = client  # 유저 정보
                socket.sendall(quiz_message.encode('utf-8'))  # 모든 유저에게 메세지를 인코딩하여 전송



if __name__ == "__main__":#메인모듈일시
    MultiChatSever()#서버 함수 실행

