
import os
import sys
import json
import time
import requests
from flask import Flask, request
from datetime import datetime
from Flow import Flow
from Get_started import Getstarted

app = Flask(__name__)

ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
VERIFY_TOKEN = os.environ["VERIFY_TOKEN"]

# idメモ
"""
ひがし：2476256932448282
"""

# Flowクラスの初期化
flow = Flow()

# Getstartedクラスの初期化
getstarted = Getstarted()
getstarted.send_get_started(ACCESS_TOKEN)


@app.route('/', methods=['GET'])
def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == VERIFY_TOKEN:  # os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():

    global info_step
    global view_count
    global customer_name, customer_name_sub, customer_address, customer_number

    data = request.get_json()
    print('***** post data *****')
    print(data)

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent us a message

                    sender_id = messaging_event["sender"]["id"]

                    if messaging_event["message"].get("text"):
                        message_text = messaging_event["message"]["text"]  # the message's text

                        # インジケータ
                        send_typing_on(sender_id)

                        # botの本体
                        flow.execute_method(sender_id, message_text, ACCESS_TOKEN)

                    else:
                        pass

                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("optin"):  # optin confirmation
                    pass

                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message

                    sender_id = messaging_event["sender"]["id"]
                    message_text = messaging_event["postback"]["title"]
                    return_id = messaging_event["postback"]["payload"]

                    # インジケータ
                    send_typing_on(sender_id)

                    # botの本体
                    flow.execute_method(sender_id, message_text, ACCESS_TOKEN)

    return "ok", 200


def send_url_image(recipient_id, title, subtitle, url_str, image_url):
    """
    :param recipient_id: string: bot送信する相手のID
    :param title: string: タイトル
    :param subtitle: string: サブタイトル
    :param url: string: リンク先のURL
    :param url_image: string: サムネイル画像が格納されているURL
    :return: POSTリクエスト
    """

    params = {
        "access_token": ACCESS_TOKEN  # os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": title,
                            "image_url": image_url,
                            "subtitle": subtitle,
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": url_str,
                                    "title": "View Website"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    })

    requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)




def send_buttons(recipient_id, text, buttons):
    """
    :param recipient_id: string: bot送信する相手のID
    :param title: string: タイトル
    :param subtitle: string: サブタイトル
    :param url: string: リンク先のURL
    :param url_image: string: サムネイル画像が格納されているURL
    :return: POSTリクエスト
    """

    params = {
        "access_token": ACCESS_TOKEN  # os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }

    buttons_postback = []

    for button in buttons:
        postback_dict = {
            "type": "postback",
            "title": button,
            "payload": "postback button payload : {}".format(button)
        }
        buttons_postback.append(postback_dict)

    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": text,
                    "buttons": buttons_postback
                }
            }
        }
    })

    requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)

def send_info_validation(recipient_id):
    text = 'お疲れ様😄\n入力は以上だよ！\nこの内容で合ってるかな？\nお名前 : {}\nふりがな : {}\nメールアドレス : {}\n電話番号 : {}'.format(customer_name, customer_name_sub, customer_address, customer_number)
    buttons = ['OK👍', '修正する！']
    send_quick_reply(recipient_id, text, buttons)


def send_ok_ng_buttons(recipient_id, sender_id):
    """
    :param recipient_id: string: bot送信する相手のID
    :param title: string: タイトル
    :param subtitle: string: サブタイトル
    :param url: string: リンク先のURL
    :param url_image: string: サムネイル画像が格納されているURL
    :return: POSTリクエスト
    """

    params = {
        "access_token": ACCESS_TOKEN  # os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }

    buttons_postback = []
    buttons = ['OK', 'NG']

    for button in buttons:
        postback_dict = {
            "type": "postback",
            "title": button,
            "payload": sender_id
        }
        buttons_postback.append(postback_dict)

    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": 'OK か NG か選択して下さい。',
                    "buttons": buttons_postback
                }
            }
        }
    })

    requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)


"""
登録しているIDへメッセージ
顧客からボットに送信された個人情報を、ボットから弁護士メッセンジャーへ送信する
顧客 -> ボット、ボット -> 弁護士
"""


def send_info_to_lawyer(recipient_id, customer_name, customer_name_sub, customer_address, customer_number, content):
    first_text = 'お客様からご連絡が届きました！'
    send_message(recipient_id, first_text)

    name_text = 'お名前 : ' + customer_name
    send_message(recipient_id, name_text)

    name_sub_text = 'ふりがな : ' + customer_name_sub
    send_message(recipient_id, name_sub_text)

    address_text = 'メールアドレス : ' + customer_address
    send_message(recipient_id, address_text)

    number_text = '電話番号 : ' + customer_number
    send_message(recipient_id, number_text)

    content_text = content
    send_message(recipient_id, content_text)


def send_typing_on(recipient_id):
    params = {
        "access_token": ACCESS_TOKEN  # os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }

    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "sender_action": "typing_on"
    })

    requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    time.sleep(0.5)


if __name__ == '__main__':
    #    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
