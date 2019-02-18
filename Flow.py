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
                "method": "send_quick_reply",
                "text": "はじめまして😄\nぼくは借金セルフチェックアシスタントの福郎だよ！",
                "buttons": ["よろしく！"]
            }
        ],

        "Get Started": [
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                             "%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88/%E3%83%95%E3%82%AF%E3%83%AD%E3%82%A6_test.png"
            },
            {
                "method": "send_quick_reply",
                "text": "はじめまして😄\nぼくは借金セルフチェックアシスタントの福郎だよ！",
                "buttons": ["よろしく！"]
            }
        ],

        "よろしく！": [
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
        ],

        "当てはまる！": [
            {
                "method": "send_message",
                "text": "借金そのものは何も悪いことではないんだ。\n"
                        "でもこんなに精神的に辛いのはなぜなんだろう？🤔"
            },
            {
                "method": "send_quick_reply",
                "text": "それには1つ大きな原因があるんだ！",
                "buttons": ["原因ってなに？🤔"]
            }
        ],

        "原因ってなに？🤔": [
            {
                "method": "send_message",
                "text": "それは「取り立て」なんだ。"
            },
            {
                "method": "send_carousel_buttonless",
                "titles": [
                    "取り立てが精神的苦痛を引き起こす。",
                    "常に借金を意識させる。",
                    "取り立てと精神的苦痛はいつもセットだ！"
                ],
                "subtitles": [
                    "精神的に追い詰められる、常に借金のことばかり考えてしまう、電話・メールが怖い。",
                    "借金のことを忘れないようにさせられているんだ！",
                    "取り立てがあると嫌でも借金のことを考えてしまうんだ。"
                ],
                "image_urls": [
                    "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                    "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer1/"
                    "%E5%8E%9F%E5%9B%A0%E3%81%AF%E5%8F%96%E3%82%8A%E7%AB%8B%E3%81%A6%202.png",
                    "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                    "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer1/"
                    "%E5%80%9F%E9%87%91%E5%BF%98%E3%82%8C%E3%81%95%E3%81%9B%E3%81%AA%E3%81%84%202.png",
                    "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                    "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer1/"
                    "%E8%8B%A6%E7%97%9B%E3%81%AA%E3%81%8F%E3%81%AA%E3%82%89%E3%81%AA%E3%81%84%202.png"
                ]
            },
            {
                "method": "send_message",
                "text": "でも大丈夫👌\n例えば弁護士に相談したりすると、すぐに取り立てが止まるんだ！"
            },
            {
                "method": "send_quick_reply",
                "text": "取り立てが止まると、今では想像できないほど精神的に楽になるんだ🤔\nみんなの声を聞いてみよう！",
                "buttons": ["聞いてみる"]
            }
        ],

        "聞いてみる": [
            {
                "method": "send_carousel_buttonless",
                "titles": [
                    "不安が無くなり、冷静に考えられる。",
                    "ただただ嬉しい。",
                    "後回しは厳禁！"
                ],
                "subtitles": [
                    "冷静さを取り戻したら、返済にむけてしっかり考えることができるんだ。",
                    "前向きな気持ちが大事だよ！",
                    "多くの悩みは時間が解決してくれる、でも借金は別だ！"
                ],
                "image_urls": [
                    "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                    "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer2/"
                    "%E5%86%B7%E8%A3%BD%E3%81%AB%E8%80%83%E3%81%88%202.png",
                    "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                    "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer2/"
                    "%E5%AC%89%E3%81%97%E3%81%8B%E3%81%A3%E3%81%9F%202.png",
                    "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                    "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer2/"
                    "%E5%BC%81%E8%AD%B7%E5%A3%AB%E7%9B%B8%E8%AB%87%E4%BE%A1%E5%80%A4%E3%81%82%E3%82%8A%202.png"
                ]
            },
            {
                "method": "send_quick_reply",
                "text": "さあ、ぼくと一緒に第一歩を踏み出そう！👌\nまずはセルフチェックから始めよう！",
                "buttons": ["セルフチェックを始める"]
            }
        ],

        "セルフチェックを始める": [
            {
                "method": "send_message",
                "text": "それでは始めよう！👌\nチェック項目は3つだよ。"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                             "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer3-5/"
                             "layer3_question.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでね。",
                "buttons": ["1社", "2社", "3社以上"]
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

    def send_carousel_buttonless(self, recipient_id, titles, subtitles, image_urls, access_token):

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






