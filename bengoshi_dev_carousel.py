"""
    基本形完成
    動作確認済み
"""

import os
import sys
import json
from datetime import datetime
import time
from Tree import Tree

import requests
from flask import Flask, request

app = Flask(__name__)

ACCESS_TOKEN = 'EAAHZBLbwxSdQBAGPjgg3IdGTl76jRSZAfHjjjhuq1B3vTHsfczRwMnHoZBEZADRa7Ui4fYNuVMO5aZCza4K582yQwo0gmV8sojNplVW0PGokf06QavX56sqpfC2PemspkASAo8sTPZC85vt12UpQvg0HxExAmffeKf27cvKGfrTwZDZD'
VERIFY_TOKEN = 'Verify_Token_Dev'

view_count = 0
info_step = 0

customer_name = ''
customer_name_sub = ''
customer_address = ''
customer_number = ''

lawyer_id = '2316784358340526'

"""
chatbot-dev : 'EAAFcwgncLV0BAPduIt9AjwsONBl2MWTlAWX7yVZCSLn28ew5qlDIaOoEZBdkDOYC4ZAwqYvEPdfzARRTRT2TBNgQfwSi1vZAeytZBoug3PSd8uykY5cr6BVrm5GKNY0ZBo4ORRZCsJDaaHJiMOFjMm9J2JcCZCdFPmwF61YtZA1ZCnlAZDZD'
弁護士bot : 'EAAHZBLbwxSdQBAGPjgg3IdGTl76jRSZAfHjjjhuq1B3vTHsfczRwMnHoZBEZADRa7Ui4fYNuVMO5aZCza4K582yQwo0gmV8sojNplVW0PGokf06QavX56sqpfC2PemspkASAo8sTPZC85vt12UpQvg0HxExAmffeKf27cvKGfrTwZDZD'
"""

tree = Tree()


def send_get_started():
    params = {
        "access_token": ACCESS_TOKEN  # os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "get_started": {
            "payload": "Welcome!"
        },
        "greeting": [
            {
                "locale": "default",
                "text": "開発用チャットボット"
            }
        ]
    })

    requests.post("https://graph.facebook.com/v2.6/me/messenger_profile", params=params, headers=headers, data=data)


send_get_started()


@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == VERIFY_TOKEN:  # os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
    # endpoint for processing incoming messaging events

    global info_step
    global view_count

    data = request.get_json()
    print('***** post data *****')
    print(data)
    #    log(data)  # you may not want to log every incoming message in production, but it's good for testing

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent us a message
                    """
                        ユーザからメッセージが送られた時に実行される
                    """

                    sender_id = messaging_event["sender"]["id"]
                    #                    recipient_id = messaging_event["recipient"]["id"]
                    #                    message_text = ""

                    if messaging_event["message"].get("text"):
                        message_text = messaging_event["message"]["text"]  # the message's text

                        send_typing_on(sender_id)  # インジケータ

                        if message_text == '労働について':
                            text = '具体的に以下からお選びください'
                            buttons = ['給与について', '労働時間や休暇について', '人間関係のトラブル', '人事異動と就職・退職', '労働契約と社会保険・労災',
                                       'トラブルの相続先と解決方法', '上記に当てはまるものがない']
                            send_quick_reply(sender_id, text, buttons)

                        elif message_text == '給与について' or message_text == '労働時間や休暇について' or message_text == '人間関係のトラブル' \
                                or message_text == '人事異動と就職・退職' or message_text == '労働契約と社会保険・労災':
                            text = 'お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？'
                            buttons = ['ホームページを見てみる', '今は見ない']
                            send_quick_reply(sender_id, text, buttons)

                        elif message_text == '離婚・男女問題について':
                            text = '具体的に以下からお選びください'
                            buttons = ['お金のトラブル', '離婚と子供', '男女トラブル', '上記に当てはまるものがない']
                            send_quick_reply(sender_id, text, buttons)

                        elif message_text == 'お金のトラブル' or message_text == '離婚と子供' or message_text == '男女トラブル' or message_text == '上記に当てはまるものがない':
                            text = 'お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？'
                            buttons = ['ホームページを見てみる', '今は見ない']
                            send_quick_reply(sender_id, text, buttons)

                        elif message_text == 'ホームページを見てみる':

                            view_count += 1

                            text = 'ありがとうございます！無料相談もありますので、ぜひご検討ください！'
                            title = 'ホームページのご案内'
                            subtitle = '無料相談のお申し込みもこちらから行えます！'
                            url_str = 'https://www.bengo4.com/'
                            image_url = 'https://www.bengo4.com/img/common/logo_fb_210_210.gif'
                            send_message(sender_id, text)
                            send_url_image(sender_id, title, subtitle, url_str, image_url)

                            text = '弊事務所の弁護士と直接やりとりすることもできます！'
                            buttons = ['直接やりとりする', '今はやめとく']
                            send_quick_reply(sender_id, text, buttons)

                        elif message_text == '直接やりとりする':
                            text = 'ありがとうございます！お名前、ふりがな、メールアドレス、電話番号が必要となります。'
                            send_message(sender_id, text)

                            text = 'お名前を送信してください。'

                            info_step = 1
                            send_message(sender_id, text)

                        elif info_step == 1:
                            text = 'ふりがなを送信してください。'

                            info_step = 2
                            global customer_name
                            customer_name = message_text

                            send_message(sender_id, text)

                        elif info_step == 2:
                            text = 'メールアドレスを入力してください。'

                            info_step = 3
                            global customer_name_sub
                            customer_name_sub = message_text

                            send_message(sender_id, text)

                        elif info_step == 3:
                            text = '電話番号を入力してください'

                            info_step = 4
                            global customer_address
                            customer_address = message_text

                            send_message(sender_id, text)

                        elif info_step == 4:
                            text = '必要な情報は以上です、ありがとうございました！'

                            info_step = 0
                            global customer_number
                            customer_number = message_text
                            send_message(sender_id, text)

                            text = '内容を確認してください。'
                            buttons = ['確認する', '修正する']
                            send_quick_reply(sender_id, text, buttons)

                        elif message_text == '確認する':
                            text = '以下の内容でよろしいですか？'
                            send_message(sender_id, text)
                            text = 'お名前 : {}'.format(customer_name)
                            send_message(sender_id, text)
                            text = 'ふりがな : {}'.format(customer_name_sub)
                            send_message(sender_id, text)
                            text = 'メールアドレス : {}'.format(customer_address)
                            send_message(sender_id, text)
                            text = '電話番号 : {}'.format(customer_number)
                            send_message(sender_id, text)

                            text = 'よろしければ、以下の「送信する」ボタンを押してください。'
                            buttons = ['送信する', '修正する']
                            send_quick_reply(sender_id, text, buttons)

                        elif message_text == '修正する':

                            text = 'お名前を送信してください。'

                            info_step = 1
                            send_message(sender_id, text)


                        elif message_text == '今はやめとく':
                            text = '最初から始める場合は、以下のボタンを押してください。'
                            buttons = ['最初から始める']
                            send_quick_reply(sender_id, text, buttons)

                        elif message_text == '今は見ない':
                            text = 'またお時間があります時にいつでもご覧ください！'
                            send_message(sender_id, text)

                            text = '他にお悩みはありませんか？'
                            buttons = ["労働について", "離婚・男女問題について", "借金について"]
                            send_quick_reply(sender_id, text, buttons)


                        elif message_text == '借金について':
                            text = '具体的な内容を、以下からお選びください'
                            buttons = ['借金の減額や見直し', '取り立てと差し押さえ', '身近な人の借金', '過去の借金', '借金の基礎知識', '上記に当てはまるものがない']
                            send_quick_reply(sender_id, text, buttons)

                        elif message_text == '借金の減額や見直し' or message_text == '取り立てと差し押さえ' or message_text == '身近な人の借金' or message_text == '過去の借金' or message_text == '借金の基礎知識' or message_text == '上記に当てはまるものがない':
                            text = 'お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？'
                            buttons = ['ホームページを見てみる', '今は見ない']
                            send_quick_reply(sender_id, text, buttons)

                        elif message_text == '最初から始める':
                            sender_id = messaging_event["sender"]["id"]
                            text = "お悩みを教えてください。"
                            buttons = ["労働について", "離婚・男女問題について", "借金について"]
                            send_quick_reply(sender_id, text, buttons)

                        elif message_text == 'カウント':
                            text = str(view_count)
                            send_message(sender_id, text)

                        elif message_text == '送信する':
                            content = 'テストコンテンツ'
                            send_info_to_lawyer(lawyer_id, customer_name, customer_name_sub, customer_address,
                                                customer_number, content)

                            text = 'OKかNGを押してください'
                            send_ok_ng_buttons(lawyer_id, sender_id, text)

                            text = '送信が完了しました。'
                            send_message(sender_id, text)
                            text = '内容を確認致しました後、お客様のご相談に対応可能な弁護士を検索致します。通常2〜3営業日以内にご返信致します。'
                            send_message(sender_id, text)
                            text = 'お客様のご相談に対応致しかねる場合もございます。ご理解とご了承をお願い致します。'
                            send_message(sender_id, text)

                        elif message_text == 'ポスト':
                            text = 'テスト'
                            buttons = ["A", "B", "C"]
                            send_buttons(sender_id, text, buttons)
                            buttons = ["D", "E", "F"]
                            send_buttons(sender_id, text, buttons)

                        elif message_text == 'カルーセル':
                            titles = ['carousel1', 'carousel2', 'carousel3']
                            image_urls = ['https://cdn.pixabay.com/photo/2016/11/14/03/35/lover-1822498_960_720.jpg',
                                          'https://cdn.pixabay.com/photo/2016/11/14/03/35/lover-1822498_960_720.jpg',
                                          'https://cdn.pixabay.com/photo/2016/11/14/03/35/lover-1822498_960_720.jpg']
                            subtitles = ['carousl1', 'carousel2', 'carousel3']
                            buttons_titles = [['button1'], ['button1', 'button2'], ['button1', 'button2', 'button3']]
                            send_carousel(sender_id, titles, image_urls, subtitles, buttons_titles)

                    else:
                        text = "すみません、もう一度選択してください。"
                        buttons = ["労働について", "離婚・男女問題について", "借金について"]
                        send_quick_reply(sender_id, text, buttons)

                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("optin"):  # optin confirmation
                    pass

                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message

                    sender_id = messaging_event["sender"]["id"]
                    message_text = messaging_event["postback"]["title"]
                    return_id = messaging_event["postback"]["payload"]

                    send_typing_on(sender_id)

                    if message_text == 'スタート':
                        text = "どのようなお悩みでしょうか？"
                        buttons = ["労働について", "離婚・男女問題について", "借金について"]
                        send_quick_reply(sender_id, text, buttons)

                    elif message_text == 'A':
                        text = 'A is selected'
                        send_message(sender_id, text)

                    elif message_text == 'B':
                        text = 'B is selected'
                        send_message(sender_id, text)

                    elif message_text == 'C':
                        text = 'C is selected'
                        send_message(sender_id, text)

                    elif message_text == 'D':
                        text = 'D is selected'
                        send_message(sender_id, text)

                    elif message_text == 'E':
                        text = 'E is selected'
                        send_message(sender_id, text)
                    elif message_text == 'F':
                        text = 'F is selected'
                        send_message(sender_id, text)

                    elif message_text == "NG":
                        text = '大変申し訳ございません。今回はお客様のご相談にお応えできる弁護士が見つかりませんでした。'
                        send_message(return_id, text)
                        text = '法的トラブルの総合解決所である、「法テラス」へご相談されることをご検討ください。'
                        title = '法テラスのご案内'
                        subtitle = '法テラスは国が設立した法的トラブルの総合案内所です。'
                        url_str = 'https://www.houterasu.or.jp/'
                        image_url = 'http://www.aaaqq.gr.jp/info/media/terasu.gif'
                        send_message(return_id, text)
                        send_url_image(return_id, title, subtitle, url_str, image_url)

                    elif message_text == "OK":
                        text = '弁護士に受理されました。弁護士からの連絡をお待ちください。'
                        send_message(return_id, text)

                    else:
                        text = "もう一度最初から始めてください。"
                        buttons = ["労働について", "離婚・男女問題について", "借金について"]
                        send_quick_reply(sender_id, text, buttons)


    return "ok", 200


def send_message(recipient_id, message_text):
    #    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

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
            "text": message_text,
        }
    })

    """
    ここでrequests.postを実行した時点で指定urlにリクエストを送信し、
    botがメッセージを送信している
    """
    requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)


#    if r.status_code != 200:
#        log(r.status_code)
#        log(r.text)


def send_quick_reply(recipient_id, text, buttons):
    """
    :param recipient_id: string
    :param text: string
    :param buttons: list; string
    :return: post
    """

    params = {
        "access_token": ACCESS_TOKEN  # os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }

    quick_replies = []

    for button in buttons:
        quick_dict = {
            "content_type": "text",
            "title": button,
            "payload": "payload: {}".format(button)
        }
        quick_replies.append(quick_dict)

    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": text,
            "quick_replies": quick_replies
        }
    })

    requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)


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

def send_carousel(recipient_id, titles, image_urls, subtitles, buttons_titles):

    """
    :param recipient_id: String:
    :param titles: List: String
    :param image_urls: List: String
    :param subtitles: List: String
    :param buttons_titles: List: List: String
    :return:
    """


    params = {
        "access_token": ACCESS_TOKEN  # os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }

    elements = []
    carousel_number = len(titles)

    for num in range(carousel_number):

        buttons = []

        for button_title in buttons_titles[num]:
            button_dict = {
                "type": "postback",
                "title": button_title,
                "payload": "payload : " + button_title
            }
            buttons.append(button_dict)

        carousel_dict = {
            "title": titles[num],
            "image_url": image_urls[num],
            "subtitle": subtitles[num],
            "buttons": buttons
        }
        elements.append(carousel_dict)

    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": elements
                }
            }
        }
    })


    """
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
                            "title": "Carousel Test",
                            "image_url": "https://cdn.pixabay.com/photo/2016/11/14/03/35/lover-1822498_960_720.jpg",
                            "subtitle": "Carousel Test",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "test1",
                                    "payload": "postback payload2"
                                }, {
                                    "type": "postback",
                                    "title": "test2" + "👍",
                                    "payload": "postback payload2"
                                }
                            ]
                        },
                        {
                            "title": "Carousel Test",
                            "image_url": "https://cdn.pixabay.com/photo/2016/11/14/03/35/lover-1822498_960_720.jpg",
                            "subtitle": "Carousel Test",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "test1",
                                    "payload": "postback payload2"
                                }, {
                                    "type": "postback",
                                    "title": "test2",
                                    "payload": "postback payload2"
                                }
                            ]
                        },
                        {
                            "title": "Carousel Test",
                            "image_url": "https://cdn.pixabay.com/photo/2016/11/14/03/35/lover-1822498_960_720.jpg",
                            "subtitle": "Carousel Test",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "test1",
                                    "payload": "postback payload2"
                                }, {
                                    "type": "postback",
                                    "title": "test2",
                                    "payload": "postback payload2"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    })
    """

    requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)


def send_ok_ng_buttons(recipient_id, sender_id, text):
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
                    "text": text,
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