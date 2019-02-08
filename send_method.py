

class Bot():

    def __init__(self, access_token):
        self.ACCESS_TOKEN = access_token


    def send_get_started(self):
        params = {
            "access_token": self.ACCESS_TOKEN  # os.environ["PAGE_ACCESS_TOKEN"]
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
                    "text": "開発用チャットボット : send_method test"
                }
            ]
        })

        requests.post("https://graph.facebook.com/v2.6/me/messenger_profile", params=params, headers=headers, data=data)
