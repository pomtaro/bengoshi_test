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
from Tree import Guidance


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

#  ツリークラスを初期化
tree = Tree()
guidance = Guidance()

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
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == VERIFY_TOKEN:  # os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():

    global info_step
    global view_count

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

                        # テキストサーチ
                        indexes = guidance.search_text(message_text)

                        # ボットテキストfirst
                        text_first = guidance.decide_text_first(indexes)
                        send_message(sender_id, text_first)

                        # ボットテキストsecond
                        text_second = guidance.decide_text_second(indexes)
                        send_message(sender_id, text_second)

                        # ボタンレスカルーセル送信
                        titles, image_urls, subtitles = guidance.decide_images(indexes)
                        send_carousel_buttonless(sender_id, titles, image_urls, subtitles)

                        # クイック返信送信
                        text =  guidance.decide_text_third(indexes)
                        buttons = guidance.decide_buttons(indexes)
                        send_quick_reply(sender_id, text, buttons)


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

                    if message_text == 'スタート' or message_text == 'Get Started':

                        url_startimage = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88/%E3%83%95%E3%82%AF%E3%83%AD%E3%82%A6_test.png'
                        send_image(sender_id, url_startimage)

                        text = 'はじめまして！\nぼくは離婚についてアドバイスする福郎だよ！'
                        send_message(sender_id, text)

                        text = 'まずは気になる項目を下から選んでみてね！'
                        send_message(sender_id, text)

                        titles = ["性格の不一致", "浪費、借金", "DV", "浮気、男女問題", "その他"]

                        mismatch_of_personality = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E6%80%A7%E6%A0%BC%E3%81%AE%E4%B8%8D%E4%B8%80%E8%87%B4/%E6%80%A7%E6%A0%BC%E3%81%AE%E4%B8%8D%E4%B8%80%E8%87%B42.png'
                        waste_debt = 'https://github.com/pomtaro/bengoshi_test/blob/master/pic_bot/%E6%B5%AA%E8%B2%BB%E3%83%BB%E5%80%9F%E9%87%91/%E6%B5%AA%E8%B2%BB%E3%83%BB%E5%80%9F%E9%87%91.png?raw=true'
                        dv = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/DV/DV2.png'
                        unfaithful_sexualproblem = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E6%B5%AE%E6%B0%97%E3%83%BB%E7%94%B7%E5%A5%B3%E5%95%8F%E9%A1%8C/%E6%B5%AE%E6%B0%97%E3%83%BB%E7%94%B7%E5%A5%B3%E5%95%8F%E9%A1%8C.png'
                        other = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E3%81%9D%E3%81%AE%E4%BB%96/%E3%81%9D%E3%81%AE%E4%BB%96.png'

                        image_urls = [mismatch_of_personality, waste_debt, dv, unfaithful_sexualproblem, other]
                        subtitles = ["性格の不一致", "浪費、借金", "DV", "浮気、男女問題", "その他"]
                        buttons_titles = [["性格の不一致"], ["浪費、借金"], ["DV"], ["浮気、男女問題"], ["その他"]]
                        send_carousel(sender_id, titles, image_urls, subtitles, buttons_titles)

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
                        indexes = tree.search_text(message_text)
                        if len(indexes) == 1:
                            text = tree.decide_text(indexes)
                            send_message(sender_id, text)

                            titles = tree.decide_buttons(indexes)
                            image_urls = tree.decide_images(indexes)
                            buttons_titles = []
                            for title in titles:
                                button = []
                                button.append(title)
                                buttons_titles.append(button)
                            subtitles = titles

                            send_carousel(sender_id, titles, image_urls, subtitles, buttons_titles)

                        elif len(indexes) == 2:
                            text = tree.decide_text(indexes)
                            send_message(sender_id, text)

                            image_urls = tree.decide_images(indexes)
                            titles = tree.decide_buttons(indexes)
                            subtitles = titles
                            send_carousel_buttonless(sender_id, titles, image_urls, subtitles)

                            text = 'アドバイスは役に立ったかな？'
                            buttons = ['役に立った！']
                            send_quick_reply(sender_id, text, buttons)

    return "ok", 200


def send_message(recipient_id, message_text):

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

    requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)


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


def send_image(recipient_id, image_url):
    """
    画像を送るだけ
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
                "type": "image",
                "payload": {
                    "url": image_url,
                    "is_reusable": 'true'
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

    requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)


def send_carousel_buttonless(recipient_id, titles, image_urls, subtitles):
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

        carousel_dict = {
            "title": titles[num],
            "image_url": image_urls[num],
            "subtitle": subtitles[num]
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
