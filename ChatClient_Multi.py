
from socket import *
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from threading import *


class ChatClient:
    client_socket = None#소켓 선언

    def __init__(self, ip, port):
        self.initialize_socket(ip, port)#소켓초기화
        self.initialize_gui()#gui 초기화
        self.listen_thread()#스레드 실행

    def initialize_socket(self, ip ,port):#소켓초기화
        self.client_socket = socket(AF_INET, SOCK_STREAM)#소켓 선언
        remote_ip = ip#ip저장
        remote_port = port#port 저장
        self.client_socket.connect((remote_ip ,remote_port))# 소켓 연결

    def send_chat(self):#메세지 전송
        senders_name = self.name_widget.get().strip() + ":"#유저이름 + :
        data = self.enter_text_widget.get(1.0, 'end').strip() #공백을 제거한뒤 사용자가 입력한 메세지를 첫 번째 줄 , 첫번째 문자 위치에 둔다.
        Message = (senders_name + data).encode('UTF-8')#이름 : 메세지 형식으로 만든뒤 인코딩
        self.chat_transcript_area.insert('end', Message.decode('UTF-8 ')+'\n')#대화창에 출력 한뒤 개행문자로 줄을 바꾼다.
        self.chat_transcript_area.yview(END)#
        self.client_socket.send(Message)#메세지 소켓 전송
        self.enter_text_widget.delete(1.0, 'end')#메세지 입력칸을 지운다.
        return 'break'

    def initialize_gui(self):#gui 생성
        self.root = Tk()
        fr =[]

        for i in range(0 ,5):#프레임 5개
            fr.append(Frame(self.root))#프레임 추가
            fr[i].pack(fill=BOTH)#프레임 순서대로 할당된 크기에 맞춘다.

        self.name_label = Label(fr[0], text='사용자 이름')#첫번째 프레임에 추가
        self.recv_label = Label(fr[1], text='수신 메세지:')#두번째 프레임에 추가
        self.send_label = Label(fr[3], text='송신 메세지:')#네번째 프레임에 추가
        self.send_btn = Button(fr[3], text='전송', command=self.send_chat)#버튼이 눌릴시 send_chat 실행
        self.chat_transcript_area = ScrolledText(fr[2], height=20, width=60)#대화방
        self.enter_text_widget = ScrolledText(fr[2], height=5, width=60)#유저가 메세지 입력하는 란
        self.name_widget = Entry(fr[0] ,width=15)#유저이름 입력란

        self.name_label.pack(side=LEFT)#위치왼쪽 배치
        self.name_widget.pack(side=LEFT)#위치왼쪽 배치
        self.recv_label.pack(side=LEFT)#위치왼쪽 배치
        self.send_btn.pack(side=RIGHT, padx=20)#위치오른쪽 배치
        self.chat_transcript_area.pack(side=LEFT, padx=2, pady=2)
        self.send_label.pack(side=RIGHT)
        self.enter_text_widget.pack(side=LEFT ,padx=2 ,pady=2)

    def listen_thread(self):

        t = Thread(target=self.receive_message, args=(self.client_socket,))#쓰레드가 실행할 함수를 target으로 지정 입력파라미터는 args에 입력
        t.start()#쓰레드 실행

    def receive_message(self, so):#메세지 받기

        while True:
            buf = so.recv(256)#메세지 저장
            if not buf:#메세지가 없으면
                break#break
            self.chat_transcript_area.insert('end' ,buf.decode('utf-8' ) +'\n')#대화방에 추가하고
            self.chat_transcript_area.yview(END)#
        so.close()

if __name__ == "__main__":#메인모듈일시
    ip = input("server IP addr:")#아이피 입력받는 문장
    if ip == '':#아이피를 비워둘시
        ip = '127.0.0.1'#자기자신과 연결되는 아이피 자동입력
    port = 2500#포트는 서버와 같아야함
    ChatClient(ip, port)#함수 실행
    mainloop()
