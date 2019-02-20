
class Getstarted():

    def send_get_started(self, access_token):
        params = {
            "access_token": access_token
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
                    "text": "初めまして！😄\n"
                            "ぼくは借金セルフチェックアシスタントの福郎だよ！\n"
                            "借金にはとても大きな精神的苦痛があるけど、\n"
                            "借金を返済する人を支援する仕組みがちゃんとあるんだ！\n"
                            "\n"
                            "一人で悩まず、まずはぼくと話してみない？🤔ほいほい"
                }
            ]
        })

        requests.post("https://graph.facebook.com/v2.6/me/messenger_profile", params=params, headers=headers, data=data)
