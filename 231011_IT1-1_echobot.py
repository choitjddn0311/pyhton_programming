import json 
import requests
import time
import urllib

TOKEN = "" 
URL = "https://api.telegram.org/bot{}/".format(TOKEN) 


def get_url(url): #함수응답
    response = requests.get(url) #url 을 requests모듈로 가져와 response에 저장
    content = response.content.decode("utf8") #저장된 response값을 content에 유니코드로 변환해준다
    return content #content로 리턴


def get_json_from_url(url): #get_json_from_url 함수호출 받음
    content = get_url(url) #get_url함수를 content 변수에 지정하게됨
    js = json.loads(content) 
    return js


def get_updates(offset=None): #offset이라는 변수에 none을 지정해줌
    url = URL + "getUpdates" #url에 위에서 지정한 URL = "https://api.telegram.org/bot{}/".format(TOKEN) 이것을 이용해 url변수에 지정하게 됨
    if offset: #offset이 None이기에 실행안됨
        url += "?offset={}".format(offset)
    js = get_json_from_url(url) #get_json_from_url를 js변수에 넣어 호출
    return js #js로 리턴하게 된다


def get_last_update_id(updates): #get_last_update_id를 updates값으로
    update_ids = [] 
    for update in updates["result"]: #결과값 즉 chat_id가 들어있는 result의 값을 모두 updates로 불러온다
        update_ids.append(int(update["update_id"])) #update_ids라는 리스트안에 result의 값을 추가한다
    return max(update_ids) #최고의 아이디값을 max함수로 리턴한다


def echo_all(updates): #updates를 통해
    for update in updates["result"]: #result값을 updates로 가져오고
        text = update["message"]["text"] #text에 돌려주고
        chat = update["message"]["chat"]["id"] #chat에 돌려준다
        send_message(text, chat) #send_message를 통해 보내게 된다



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
    last_update_id = None #last_update_id를 None로 빈 값으로 지정하게 됨
    while True: #while문 진입
        updates = get_updates(last_update_id)  #last_update_id가 None기 때문에 get_updates함수를 호출하게됨
        if len(updates["result"]) > 0: #
            last_update_id = get_last_update_id(updates) + 1 #last_update_id 변수에 마지막 업데이트된 id값에 1을 추가해 
            echo_all(updates) #echo_all 부분을 호출한다
        time.sleep(0.5) 


if __name__ == '__main__': #가장먼저 코드가 실행되는 부분
    main() #main함수 출력
