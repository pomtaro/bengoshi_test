import requests
import json


class Flow:

    flow_dict = {
        "スタート": [
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                             "%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88/%E3%83%95%E3%82%AF%E3%83%AD%E3%82%A6_test.png"
            },
            {
                "method": "send_message",
                "text": "はじめまして😄\nぼくは借金セルフチェックアシスタントの福郎だよ！"
            },
            {
                "method": "send_message",
                "text": "実は日本で借金に悩んでいる人は30％ぐらいいるんだ🤔"
            },
            {
                "method": "send_carousel_buttonless",
                "titles": [
                    "バレたくない、気が晴れない",
                    "いつも不安、話したくない",
                    "とても不幸な気持ち"
                ],
                "subtitles": [
                    "家族や会社の人に言えず、とても閉塞的な気持ちになるよね。",
                    "常に頭の中に借金のことがあって、誰かと楽しく話す気にもなれないよね。",
                    "どうしようもない気持ちになることもあるよね。"
                ],
                "image_urls": [
                    "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                    "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer0/"
                    "%E3%83%90%E3%83%AC_%E6%B0%97%E5%88%86%E6%82%AA%202.png",
                    "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                    "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer0/"
                    "%E4%B8%8D%E5%AE%89_%E4%BC%9A%E8%A9%B1%E3%81%AA%E3%81%97%202.png",
                    "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                    "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer0/"
                    "%E7%AC%91%E9%A1%94%E3%81%AA%E3%81%97_%E5%BF%83%E8%B2%A7%202.png"
                ]
            },
            {
                "method": "send_quick_reply",
                "text": "借金の悩みはとても大きな精神的苦痛なんだ。\nあなたにも当てはまる？🤔",
                "buttons": ["当てはまる！"]
            }
        ]
    }

    def messgage_is(self, message_text):  # メッセージが辞書に存在するか判定
        if message_text in self.flow_dict.keys():
            return True
        else:
            return False

    def read_item_numbers(self, message_text):  # 要素数を判定
        if self.messgage_is(message_text):
            item_numbers = len(self.flow_dict[message_text])
            return item_numbers
        else:
            return False

    def read_method(self, message_text, item_number):  # methodを判定する
        if self.messgage_is(message_text):
            method = self.flow_dict[message_text][item_number]["method"]
            return method
        else:
            return False

    def execute_method(self, recipient_id, message_text, access_token):
        item_numbers = self.read_item_numbers(message_text)

        for item_number in range(item_numbers):
            method = self.read_method(message_text, item_number)

            if method == "send_message":
                text = self.flow_dict[message_text][item_number]["text"]
                self.send_message(recipient_id, text, access_token)
            elif method == "send_quick_reply":
                text = self.flow_dict[message_text][item_number]["text"]
                buttons = self.flow_dict[message_text][item_number]["buttons"]
                self.send_quick_reply(recipient_id, text, buttons, access_token)
            elif method == "send_image":
                image_url = self.flow_dict[message_text][item_number]["image_url"]
                self.send_image(recipient_id, image_url, access_token)
            elif method == "send_carousel_buttonless":
                titles = self.flow_dict[message_text][item_number]["titles"]
                subtitles = self.flow_dict[message_text][item_number]["subtitles"]
                image_urls = self.flow_dict[message_text][item_number]["image_urls"]
                self.send_carousel_buttonless(recipient_id, titles, subtitles, image_urls, access_token)

    def send_message(self, recipient_id, text, access_token):

        params = {
            "access_token": access_token
        }
        headers = {
            "Content-Type": "application/json"
        }
        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "text": text
            }
        })

        requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)

    def send_quick_reply(self, recipient_id, text, buttons, access_token):

        params = {
            "access_token": access_token
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

    def send_image(self, recipient_id, image_url, access_token):

        params = {
            "access_token": access_token
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

    def send_carousel_buttonless(self, recipient_id, titles, image_urls, subtitles, access_token):

        params = {
            "access_token": access_token
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






