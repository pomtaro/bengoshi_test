import requests
import json


class Flow:

    debt_companies = ""
    debt_prices = ""
    pay_per_month = ""
    impressions = {
        "とても良かったよ！": 0,
        "イマイチだね": 0,
        "二度と使わない！": 0
    }

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
                    "常に借金を意識させられている。",
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
        ],

        "1社": [
            {
                "method": "record_debt_companies"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                             "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer3-5/"
                             "layer4_question.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでね。",
                "buttons": ["0~100万", "100~500万", "500~1000万", "1000~2000万", "2000万以上"]
            }
        ],

        "2社": [
            {
                "method": "record_debt_companies"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                             "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer3-5/"
                             "layer4_question.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでね。",
                "buttons": ["0~100万", "100~500万", "500~1000万", "1000~2000万", "2000万以上"]
            }

        ],

        "3社以上": [
            {
                "method": "record_debt_companies"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                             "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer3-5/"
                             "layer4_question.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでね。",
                "buttons": ["0~100万", "100~500万", "500~1000万", "1000~2000万", "2000万以上"]
            }

        ],

        "0~100万": [
            {
                "method": "record_debt_prices"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                             "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer3-5/"
                             "layer5_question.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでね。",
                "buttons": ["0~1万", "1~5万", "5~10万", "10万以上"]
            }
        ],

        "100~500万": [
            {
                "method": "record_debt_prices"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                             "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer3-5/"
                             "layer5_question.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでね。",
                "buttons": ["0~1万", "1~5万", "5~10万", "10万以上"]
            }
        ],

        "500~1000万": [
            {
                "method": "record_debt_prices"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                             "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer3-5/"
                             "layer5_question.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでね。",
                "buttons": ["0~1万", "1~5万", "5~10万", "10万以上"]
            }
        ],

        "1000~2000万": [
            {
                "method": "record_debt_prices"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                             "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer3-5/"
                             "layer5_question.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでね。",
                "buttons": ["0~1万", "1~5万", "5~10万", "10万以上"]
            }
        ],

        "2000万以上": [
            {
                "method": "record_debt_prices"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                             "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer3-5/"
                             "layer5_question.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでね。",
                "buttons": ["0~1万", "1~5万", "5~10万", "10万以上"]
            }
        ],

        "0~1万": [
            {
                "method": "record_pay_per_month"
            },
            {
                "method": "send_quick_reply",
                "text": "質問は終わりだよ！\nセルフチェック結果を見てみよう！🤔",
                "buttons": ["見てみる"]
            }
        ],

        "1~5万": [
            {
                "method": "record_pay_per_month"
            },
            {
                "method": "send_quick_reply",
                "text": "質問は終わりだよ！\nセルフチェック結果を見てみよう！🤔",
                "buttons": ["見てみる"]
            }
        ],

        "5~10万": [
            {
                "method": "record_pay_per_month"
            },
            {
                "method": "send_quick_reply",
                "text": "質問は終わりだよ！\nセルフチェック結果を見てみよう！🤔",
                "buttons": ["見てみる"]
            }
        ],

        "10万以上": [
            {
                "method": "record_pay_per_month"
            },
            {
                "method": "send_quick_reply",
                "text": "質問は終わりだよ！\nセルフチェック結果を見てみよう！🤔",
                "buttons": ["見てみる"]
            }
        ],

        "見てみる": [
            {
                "method": "decide_consolidation_image"
            },
            {
                "method": "decide_consolidation_comment"
            },
            {
                "method": "send_message",
                "text": "チェック結果だよ🤔"
            },
            {
                "method": "send_image",
                "image_url": "Hello"  # decide_consolidation_image内でurlを定義している
            },
            {
                "method": "send_message",
                "text": ""  # decide_consolidation_comment内でtextを定義している
            },
            {
                "method": "send_quick_reply",
                "text": "借金を整理する方法はいくつかあって、借金の状況に応じてちゃんと選択することがとても重要なんだ🤔\n"
                        "どんな整理の方法があるか、確認してみよう！",
                "buttons": ["確認する"]
            }
        ],

        "確認する": [
            {
                "method": "decide_consolidation_recommendation"
            },
            {
                "method": "send_message",
                "text": "あなたにオススメの整理方法をぼくなりに考えてみたよ👌\n"
                        "他の整理方法も見てみてね"
            },
            {
                "method": "send_carousel",
                "titles": [],  # decide_consolidation_recommendation内で定義
                "subtitles": [],  # decide_consolidation_recommendation内で定義
                "image_urls": [],  # decide_consolidation_recommendation内で定義
                "buttons_titles": [[]]  # decide_consolidation_recommendation内で定義
            }
        ],

        "任意整理を詳しく見る": [
            {
                "method": "send_message",
                "text": "任意整理は一番手軽な借金整理の方法だよ👍"
            },
            {
                "method": "send_carousel_buttonless",
                "titles": [
                    "金利なしで元金だけ返済！",
                    "自分の代わりに交渉してくれる！",
                    "まずは1つからでもOK！"
                ],
                "subtitles": [
                    "元金だけ返せばよいから、返済の負担がすごく楽になるよ！",
                    "仕事をしている人でも安心！自分で交渉する必要はないんだ👌",
                    "任意整理するもの、しないものを選ぶことができるよ！"
                ],
                "image_urls": [
                    "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                    "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer8/"
                    "%E4%BB%BB%E6%84%8F%E6%95%B4%E7%90%86%E3%81%AE%E6%83%85%E5%A0%B11.png",
                    "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                    "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer8/"
                    "%E4%BB%BB%E6%84%8F%E6%95%B4%E7%90%86%E3%81%AE%E6%83%85%E5%A0%B12.png",
                    "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                    "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer8/"
                    "%E4%BB%BB%E6%84%8F%E6%95%B4%E7%90%86%E3%81%AE%E6%83%85%E5%A0%B13.png"
                ]
            },
            {
                "method": "send_quick_reply",
                "text": "最後に、セルフチェックとぼくのアシスタントぶりはどうだったかな？\nアンケートで教えてほしいな😄",
                "buttons": ["アンケートに答える"]
            }
        ],

        "個人再生を詳しく見る": [
            {
                "method": "send_message",
                "text": "個人再生は財産を残しながら借金を大幅に減額できることが特徴だよ👍"
            },
            {
                "method": "send_carousel_buttonless",
                "titles": [
                    "原則、借金を1/5に！",
                    "財産を手元に残すことができる！",
                    "債権者からの強制執行を止めることができる！"
                ],
                "subtitles": [
                    "元金のすべてを返さなくていい！減らした借金を分割で返済しよう。",
                    "大事な財産を手放す必要はない！安心して借金返済に集中できる。",
                    "取り立てはもちろん、給料の差し止めなども止めることができる。"
                ],
                "image_urls": [
                    "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                    "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer8/"
                    "%E5%80%8B%E4%BA%BA%E5%86%8D%E7%94%9F%E3%81%AE%E6%83%85%E5%A0%B11.png",
                    "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                    "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer8/"
                    "%E5%80%8B%E4%BA%BA%E5%86%8D%E7%94%9F%E3%81%AE%E6%83%85%E5%A0%B12.png",
                    "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                    "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer8/"
                    "%E5%80%8B%E4%BA%BA%E5%86%8D%E7%94%9F%E3%81%AE%E6%83%85%E5%A0%B13.png"
                ]
            },
            {
                "method": "send_quick_reply",
                "text": "最後に、セルフチェックとぼくのアシスタントぶりはどうだったかな？\nアンケートで教えてほしいな😄",
                "buttons": ["アンケートに答える"]
            }

        ],

        "自己破産を詳しく見る": [
            {
                "method": "send_message",
                "text": "自己破産は借金を全て無くせることが特徴だよ👍"
            },
            {
                "method": "send_carousel_buttonless",
                "titles": [
                    "借金を帳消し！",
                    "債権者からの強制執行を止めることができる！",
                    "生活に必要な最低限の資産は残せる！"
                ],
                "subtitles": [
                    "借金がどれだけあっても関係なし！1からやり直そう👌",
                    "取り立てはもちろん、給料の差し止めなども止めることができる。",
                    "身ぐるみ剥がされる訳ではない！最低限のものは残すことができるんだ。"
                ],
                "image_urls": [
                    "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                    "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer8/"
                    "%E8%87%AA%E5%B7%B1%E7%A0%B4%E7%94%A3%E3%81%AE%E6%83%85%E5%A0%B11.png",
                    "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                    "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer8/"
                    "%E8%87%AA%E5%B7%B1%E7%A0%B4%E7%94%A3%E3%81%AE%E6%83%85%E5%A0%B12.png",
                    "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                    "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer8/"
                    "%E8%87%AA%E5%B7%B1%E7%A0%B4%E7%94%A3%E3%81%AE%E6%83%85%E5%A0%B13.png"
                ]
            },
            {
                "method": "send_quick_reply",
                "text": "最後に、セルフチェックとぼくのアシスタントぶりはどうだったかな？\nアンケートで教えてほしいな😄",
                "buttons": ["アンケートに答える"]
            }

        ],

        "アンケートに答える": [
            {
                "method": "send_message",
                "text": "ありがとう😄"
            },
            {
                "method": "send_image",
                "image_url": "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                             "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer9/"
                             "%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88.png"
            },
            {
                "method": "send_quick_reply",
                "text": "下から選んでね。",
                "buttons": ["とても良かったよ！", "イマイチだね", "二度と使わない！"]
            }
        ],

        "とても良かったよ": [
            {
                "method": "record_impression"
            }
        ],

        "イマイチだね": [
            {
                "method": "record_impression"
            }
        ],

        "二度と使わない！": [
            {
                "method": "record_impression"
            }
        ]
    }

    def message_is(self, message_text):  # メッセージが辞書に存在するか判定
        if message_text in self.flow_dict.keys():
            return True
        else:
            return False

    def read_item_numbers(self, message_text):  # 要素数を判定
        if self.message_is(message_text):
            item_numbers = len(self.flow_dict[message_text])
            return item_numbers
        else:
            return False

    def read_method(self, message_text, item_number):  # methodを判定する
        if self.message_is(message_text):
            method = self.flow_dict[message_text][item_number]["method"]
            return method
        else:
            return False

    def execute_method(self, recipient_id, message_text, access_token):
        if self.message_is(message_text):

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
                elif method == "send_carousel":
                    titles = self.flow_dict[message_text][item_number]["titles"]
                    subtitles = self.flow_dict[message_text][item_number]["subtitles"]
                    image_urls = self.flow_dict[message_text][item_number]["image_urls"]
                    buttons_titles = self.flow_dict[message_text][item_number]["buttons_titles"]
                    self.send_carousel(recipient_id, titles, subtitles, image_urls, buttons_titles, access_token)
                elif method == "send_carousel_buttonless":
                    titles = self.flow_dict[message_text][item_number]["titles"]
                    subtitles = self.flow_dict[message_text][item_number]["subtitles"]
                    image_urls = self.flow_dict[message_text][item_number]["image_urls"]
                    self.send_carousel_buttonless(recipient_id, titles, subtitles, image_urls, access_token)
                elif method == "record_debt_companies":
                    self.record_debt_companies(message_text)
                elif method == "record_debt_prices":
                    self.record_debt_prices(message_text)
                elif method == "record_pay_per_month":
                    self.record_pay_per_month(message_text)
                elif method == "decide_consolidation_image":
                    self.decide_consolidation_image()
                elif method == "decide_consolidation_comment":
                    self.decide_consolidation_comment()
                elif method == "decide_consolidation_recommendation":
                    self.decide_consolidation_recommendation()
                elif method == "record_impression":
                    self.record_impression(message_text)



        else:
            text = "エラー"
            self.send_message(recipient_id, text, access_token)

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

    def send_carousel(self, recipient_id, titles,  subtitles, image_urls, buttons_titles, access_token):

        params = {
            "access_token": access_token
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

    def record_debt_companies(self, message_text):
        self.debt_companies = message_text

    def record_debt_prices(self, message_text):
        self.debt_prices = message_text

    def record_pay_per_month(self, message_text):
        self.pay_per_month = message_text

    def decide_consolidation_group(self, debt_prices, pay_per_month):
        if debt_prices == "0~100万":
            if pay_per_month == "0~1万":
                return "individual rehabilitation"
            elif pay_per_month == "1~5万" or pay_per_month == "5~10万" or pay_per_month == "10万以上":
                return "voluntary liquidation"
        elif debt_prices == "100~500万":
            if pay_per_month == "0~1万":
                return "personal bankruptcy"
            elif pay_per_month == "1~5万":
                return "individual rehabilitation"
            elif pay_per_month == "5~10万" or pay_per_month == "10万以上":
                return "voluntary liquidation"
        elif debt_prices == "500~1000万":
            if pay_per_month == "0~1万":
                return "personal bankruptcy"
            elif pay_per_month == "1~5万" or pay_per_month == "5~10万":
                return "individual rehabilitation"
            elif pay_per_month == "10万以上":
                return "voluntary liquidation"
        elif debt_prices == "1000~2000万":
            if pay_per_month == "0~1万" or pay_per_month == "1~5万":
                return "personal bankruptcy"
            elif pay_per_month == "5~10万" or pay_per_month == "10万以上":
                return "individual rehabilitation"
        elif debt_prices == "2000万以上":
            if pay_per_month == "0~1万" or pay_per_month == "1~5万" or pay_per_month == "5~10万":
                return "personal bankruptcy"
            elif pay_per_month == "10万以上":
                return "individual rehabilitation"

    def decide_consolidation_image(self):
        consolidation_group = self.decide_consolidation_group(self.debt_prices, self.pay_per_month)

        urls_dict = {
            "voluntary liquidation": "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                                     "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer6/"
                                     "%E4%BB%BB%E6%84%8F%E6%95%B4%E7%90%86_60%25.png",
            "individual rehabilitation": "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                                         "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer6/"
                                         "%E5%80%8B%E4%BA%BA%E5%86%8D%E7%94%9F_80%25.png",
            "personal bankruptcy": "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                                   "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer6/"
                                   "%E8%87%AA%E5%B7%B1%E7%A0%B4%E7%94%A3_100%25.png"
        }

        if consolidation_group == "voluntary liquidation":
            self.flow_dict["見てみる"][3]["image_url"] = urls_dict["voluntary liquidation"]
        elif consolidation_group == "individual rehabilitation":
            self.flow_dict["見てみる"][3]["image_url"] = urls_dict["individual rehabilitation"]
        elif consolidation_group == "personal bankruptcy":
            self.flow_dict["見てみる"][3]["image_url"] = urls_dict["personal bankruptcy"]

    def decide_consolidation_comment(self):
        consolidation_group = self.decide_consolidation_group(self.debt_prices, self.pay_per_month)

        comments_dict = {
            "voluntary liquidation": "あなたの深刻度は60％！\n"
                                     "早めに借金を整理していけば、返済の負担を大きく減らすことができるよ👌",
            "individual rehabilitation": "あなたの深刻度は80％！\n"
                                         "でも安心して、財産を保持したまま大きく借金を減額する方法だってあるんだ👌",
            "personal bankruptcy": "あなたの深刻度は100％！\n"
                                   "今すぐにでも行動を起こさないとまずい！でも少し待って、まずは借金の整理について見ていこう👌"
        }

        if consolidation_group == "voluntary liquidation":
            self.flow_dict["見てみる"][4]["text"] = comments_dict["voluntary liquidation"]
        elif consolidation_group == "individual rehabilitation":
            self.flow_dict["見てみる"][4]["text"] = comments_dict["individual rehabilitation"]
        elif consolidation_group == "personal bankruptcy":
            self.flow_dict["見てみる"][4]["text"] = comments_dict["personal bankruptcy"]

    def decide_consolidation_recommendation(self):
        consolidation_group = self.decide_consolidation_group(self.debt_prices, self.pay_per_month)

        urls_dict = {
            "voluntary liquidation_recommended": "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/"
                                                 "pic_bot/%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%"
                                                 "E5%83%8F/layer7/%E4%BB%BB%E6%84%8F%E6%95%B4%E7%90%86_%E3%82%AA%"
                                                 "E3%82%B9%E3%82%B9%E3%83%A1.png",
            "individual rehabilitation_recommended": "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/"
                                                     "pic_bot/%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%"
                                                     "E5%83%8F/layer7/%E5%80%8B%E4%BA%BA%E5%86%8D_%E3%82%AA%E3%82%B9%"
                                                     "E3%82%B9%E3%83%A1.png",
            "personal bankruptcy_recommended": "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                                               "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer7/"
                                               "%E8%87%AA%E5%B7%B1%E7%A0%B4%E7%94%A3_%E3%82%AA%E3%82%B9%E3%82%B9%E3%83%"
                                               "A1.png",
            "voluntary liquidation_other": "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                                           "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer7/"
                                           "%E4%BB%BB%E6%84%8F%E6%95%B4%E7%90%86_%E3%81%9D%E3%81%AE%E4%BB%96.png",
            "individual rehabilitation_other": "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                                               "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer7/"
                                               "%E5%80%8B%E4%BA%BA%E5%86%8D%E7%94%9F_%E3%81%9D%E3%81%AE%E4%BB%96.png",
            "personal bankruptcy_other": "https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/"
                                         "%E5%80%9F%E9%87%91%E3%83%9C%E3%83%83%E3%83%88%E7%94%BB%E5%83%8F/layer7/"
                                         "%E8%87%AA%E5%B7%B1%E7%A0%B4%E7%94%A3_%E3%81%9D%E3%81%AE%E4%BB%96.png"
        }

        if consolidation_group == "voluntary liquidation":
            self.flow_dict["確認する"][2]["titles"] = ["任意整理",
                                                   "個人再生",
                                                   "自己破産"]
            self.flow_dict["確認する"][2]["subtitles"] = ["任意整理は最小限のリスクで借金の負担を減らす方法だよ。",
                                                      "個人再生は財産を残しながら借金を大きく減らすことができるんだ。",
                                                      "自己破産は借金をすべて無くすことができる！"]
            self.flow_dict["確認する"][2]["image_urls"] = [urls_dict["voluntary liquidation_recommended"],
                                                       urls_dict["individual rehabilitation_other"],
                                                       urls_dict["personal bankruptcy_other"]]
            self.flow_dict["確認する"][2]["buttons_titles"] = [["任意整理を詳しく見る"],
                                                           ["個人再生を詳しく見る"],
                                                           ["自己破産を詳しく見る"]]
        elif consolidation_group == "individual rehabilitation":
            self.flow_dict["確認する"][2]["titles"] = ["個人再生",
                                                   "任意整理"
                                                   "自己破産"]
            self.flow_dict["確認する"][2]["subtitles"] = ["個人再生は財産を残しながら借金を大きく減らすことができるんだ。",
                                                      "任意整理は最小限のリスクで借金の負担を減らす方法だよ。",
                                                      "自己破産は借金をすべて無くすことができる！"]
            self.flow_dict["確認する"][2]["image_urls"] = [urls_dict["individual rehabilitation_recommended"],
                                                       urls_dict["voluntary liquidation_other"],
                                                       urls_dict["personal bankruptcy_other"]]
            self.flow_dict["確認する"][2]["buttons_titles"] = [["個人再生を詳しく見る"],
                                                           ["任意整理を詳しく見る"],
                                                           ["自己破産を詳しく見る"]]
        elif consolidation_group == "personal bankruptcy":
            self.flow_dict["確認する"][2]["titles"] = ["自己破産",
                                                   "任意整理",
                                                   "個人再生"]
            self.flow_dict["確認する"][2]["subtitles"] = ["自己破産は借金をすべて無くすことができる！",
                                                      "任意整理は最小限のリスクで借金の負担を減らす方法だよ。",
                                                      "個人再生は財産を残しながら借金を大きく減らすことができるんだ。"]
            self.flow_dict["確認する"][2]["image_urls"] = [urls_dict["personal bankruptcy_recommended"],
                                                       urls_dict["voluntary liquidation_other"],
                                                       urls_dict["individual rehabilitation_other"]]
            self.flow_dict["確認する"][2]["buttons_titles"] = [["自己破産を詳しく見る"],
                                                           ["任意整理を詳しく見る"],
                                                           ["個人再生を詳しく見る"]]

    def record_impression(self, message_text):
        if message_text == "とても良かったよ！":
            self.impressions["とても良かったよ！"] = self.impressions["とても良かったよ！"] + 1
        elif message_text == "イマイチだね":
            self.impressions["イマイチだね"] = self.impressions["イマイチだね"] + 1
        elif message_text == "二度と使わない！":
            self.impressions["二度と使わない！"] = self.impressions["二度と使わない！"] + 1

