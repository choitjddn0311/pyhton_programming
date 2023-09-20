import json
import requests
import time
import urllib

from random import *

TOKEN = "6647455306:AAGBJT5KFhUgX7wyvKBgPQhO73t2fN48mI0"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

gamelist={}

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def echo_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            # print(gamelist) #for debuging
            if(text == "/numgame"): #게임 시작 지점
                send_message("넘버 게임을 시작합니다. 숫자를 입력해주세요", chat) #실제 텔레그램에 전송되는 문구 when? > send /numgame
                rn  =randrange(1,101,1) # 숫자를 1~100 사이중 하나를 랜덤으로 뽑고 rn 이라는 변수에 넣어서 활용
                count = 1 #텔레그램에 입력한 횟수를 확인하는 변수
                print("game started with", chat, "/ rannum", rn) #터미널 상에 나의 chat아이디와 rn를 보여줌
                gamelist[chat] = [rn, count , False]  # Q, A, Success?  gamelist 리스트에 rn count False 를 넣어둠
            elif(text == "/stop"): #text로 /stop을 입력할 경우
                send_message("게임을 중단합니다. ", chat) #텔레그램에 게임을 중단합니다를 전송
                gamelist[chat] = [] #???
            elif(text == "/start"): # text로 /start를 입력할 경우
                print("new user:", chat) #터미널에 new user라는 문구와 함께 나의 chat id를 출력함
                send_message(
                    "반갑습니다. 넘버게임 봇입니다. 게임을 시작하기 원하시면 /numgame 명령을 입력하세요. 게임을 멈추고 싶을 때는 언제든 /stop 명령을 입력하면 됩니다. ", chat) #/start를 입력할경우 게임안내를 해주는 문구가 출력됨
            elif(len(gamelist[chat]) > 1 and not gamelist[2]): #만약에 gamelist에 있는 chat id가 1보다 크거나 아니면 False가 아니면
                num = int(text) #num 라는 변수안에 text로 입력받은 값을 int로 받음
                print(gamelist) #터미널에 gamelist 를 출력함..
                print(chat, "entered", num   ) 
                if (num == gamelist[0]): #입력받은 값이 rn와 같으면 
                    send_message("정답입니다" , chat) #텔레그램으로 정답입니다 라는 문구를 전송함
                    gamelist[chat[1]] +=1 #count 에 1을 더함 why? 1번 시도를 했으니까
                elif (num < gamelist[0]): #만약 입력받은 값이 rn 보다 작으면 
                    send_message("up",chat) #up을 텔레그램으로 전송함
                    gamelist[chat[1]] +=1 #count 에 1을 더함 why? 1번 시도를 했으니까
                elif (num > gamelist[0]): #만약 입력받은 값이 rn 보다 크면 
                    send_message("down" , chat) #down을 텔레그램으로 전송함
                gamelist[0] = num #gamlist에 0번 인덱스 rn과 num이 같으면
                succeed = False
                feedback = ""
                for number in gamelist[0]:
                    if number == text:
                        feedback += number 
                    else:
                        feedback += "enter another number"
                        succeed = True
                gamelist[0] = succeed
                send_message(feedback, chat)

                if num == gamelist[chat[0]]:
                    send_message("맞췄습니다!!!", chat)
                    print(chat, "finished a game")
                    gamelist[chat] = []
        except Exception as e:
            print(e)

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()