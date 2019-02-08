# ポストバックの時に使用するクラス、主に悩み分類の役割
class Tree:
    top = ["性格の不一致", "浪費、借金", "DV",
           "浮気、男女問題", "その他"]
    layer0 = list(top)

    top = ["性格の不一致だね🤔\nもう少し詳しく教えてほしいな！", "浪費、借金だね🤔\nもう少し詳しく教えてほしいな！", "DVだね🤔\nもう少し詳しく教えてほしいな！",
           "浮気、男女問題だね🤔\nもう少し詳しく教えてほしいな！", "その他だね🤔\nもう少し詳しく教えてほしいな！"]
    text0 = list(top)

    A = ["金銭感覚、生活スタイル", "家事、育児、教育", "親族、友達付き合い",
         "思いやり", "一人の時間", "明確な理由はないけど嫌",
         "その他"]
    tA = ['金銭感覚、生活スタイルだね🤔\nおすすめのアドバイスを教えてあげるね！', '家事、育児、教育だね🤔\nおすすめのアドバイスを教えてあげるね！', '親族・友達付き合いだね🤔\nおすすめのアドバイスを教えてあげるね！',
          '思いやりだね🤔\nおすすめのアドバイスを教えてあげるね！', '一人の時間だね🤔\nおすすめのアドバイスを教えてあげるね！', '明確な理由はないんだね🤔\nおすすめのアドバイスを教えてあげるね！',
          'その他だね！\nおすすめのアドバイスを教えてあげるね！']
    B = ["遊び（キャバクラ、酒、ギャンブル）", "いらないものを買う、相談なく借金する", "借金を隠していた",
         "その他"]
    tB = ['遊んでばっかりなんだね🤔\nおすすめのアドバイスを教えてあげるね！', '少しはこっちの身にもなってほしいよね🤔\nおすすめのアドバイスを教えてあげるね！', 'もっといいもの隠しておいてほしいよね🤔\nおすすめのアドバイスを教えてあげるね！',
          'その他だね！\nおすすめのアドバイスを教えてあげるね！']
    C = ["精神的DV", "肉体的DV", "経済的DV、生活費を渡さない",
         "性的DV", "その他"]
    tC = ['あなたは一人じゃないよ🤔\nおすすめのアドバイスを教えてあげるね！', '暴力は絶対にダメ🤔\nおすすめのアドバイスを教えてあげるね！', 'お金って難しいよね🤔\nおすすめのアドバイスを教えてあげるね！',
          '恥ずかしくても一人で悩んじゃダメ🤔\nおすすめのアドバイスを教えてあげるね！', 'その他だね🤔\nおすすめのアドバイスを教えてあげるね！']
    D = ["浮気、不倫", "セックスレス", "性的DV",
         "その他"]
    tD = ['もうなにも信じれないよね🤔\nおすすめのアドバイスを教えてあげるね！', '話し合うことも重要かも🤔\nおすすめのアドバイスを教えてあげるね！', '恥ずかしくても一人で悩んじゃダメ🤔\nおすすめのアドバイスを教えてあげるね！',
          'その他だね🤔\nおすすめのアドバイスを教えてあげるね！']
    E = ["親戚、親族", "その他"]
    tE = ['無下にできないから大変だよね🤔\nおすすめのアドバイスを教えてあげるね！', 'その他だね🤔\nおすすめのアドバイスを教えてあげるね！']
    layer1 = list((A, B, C, D, E))
    text1 = list((tA, tB, tC, tD, tE))

    A1 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]
    A2 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]
    A3 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]
    A4 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]
    A5 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]
    A6 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]
    A7 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]
    B1 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]
    B2 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]
    B3 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]
    B4 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]
    C1 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]
    C2 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]
    C3 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]
    C4 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]
    C5 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]
    D1 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]
    D2 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]
    D3 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]
    D4 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]
    E1 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]
    E2 = ["豆知識1👌", "豆知識2👌", "豆知識3👌"]

    tA1 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']
    tA2 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']
    tA3 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']
    tA4 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']
    tA5 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']
    tA6 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']
    tA7 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']
    tB1 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']
    tB2 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']
    tB3 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']
    tB4 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']
    tC1 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']
    tC2 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']
    tC3 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']
    tC4 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']
    tC5 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']
    tD1 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']
    tD2 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']
    tD3 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']
    tD4 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']
    tE1 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']
    tE2 = ['ありがとうございます！無料相談もありますので、ぜひご検討ください！', 'またお時間があります時にいつでもご覧ください！']

    layer2 = list((list((A1, A2, A3, A4, A5, A6, A7)),
                   list((B1, B2, B3, B4)),
                   list((C1, C2, C3, C4, C5)),
                   list((D1, D2, D3, D4)),
                   list((E1, E2))))
    text2 = list((list((tA1, tA2, tA3, tA4, tA5, tA6, tA7)),
                  list((tB1, tB2, tB3, tB4)),
                  list((tC1, tC2, tC3, tC4, tC5)),
                  list((D1, D2, D3, D4)),
                  list((E1, E2))))

    #  性格の不一致の内訳
    sense_for_money = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E6%80%A7%E6%A0%BC%E3%81%AE%E4%B8%8D%E4%B8%80%E8%87%B4/%E9%87%91%E9%8A%AD%E6%84%9F%E8%A6%9A%E3%83%BB%E7%94%9F%E6%B4%BB%E3%82%B9%E3%82%BF%E3%82%A4%E3%83%AB/%E9%87%91%E9%8A%AD%E6%84%9F%E8%A6%9A%E3%83%BB%E7%94%9F%E6%B4%BB%E3%82%B9%E3%82%BF%E3%82%A4%E3%83%AB.png'
    housework_child_education = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E6%80%A7%E6%A0%BC%E3%81%AE%E4%B8%8D%E4%B8%80%E8%87%B4/%E5%AE%B6%E4%BA%8B%E3%83%BB%E8%82%B2%E5%85%90%E3%83%BB%E6%95%99%E8%82%B2/%E5%AE%B6%E4%BA%8B%E3%83%BB%E8%82%B2%E5%85%90%E3%83%BB%E6%95%99%E8%82%B2.png'
    relatives_friends_relations = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E6%80%A7%E6%A0%BC%E3%81%AE%E4%B8%8D%E4%B8%80%E8%87%B4/%E8%A6%AA%E6%97%8F%E3%83%BB%E5%8F%8B%E9%81%94%E4%BB%98%E3%81%8D%E5%90%88%E3%81%84/%E8%A6%AA%E6%97%8F%E3%83%BB%E5%8F%8B%E9%81%94%E4%BB%98%E3%81%8D%E5%90%88%E3%81%84.png'
    sympathy  = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E6%80%A7%E6%A0%BC%E3%81%AE%E4%B8%8D%E4%B8%80%E8%87%B4/%E6%80%9D%E3%81%84%E3%82%84%E3%82%8A/%E6%80%9D%E3%81%84%E3%82%84%E3%82%8A.png'
    personal_time = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E6%80%A7%E6%A0%BC%E3%81%AE%E4%B8%8D%E4%B8%80%E8%87%B4/%E4%B8%80%E4%BA%BA%E3%81%AE%E6%99%82%E9%96%93/%E4%B8%80%E4%BA%BA%E3%81%AE%E6%99%82%E9%96%93.png'
    none_clear_reasons = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E6%80%A7%E6%A0%BC%E3%81%AE%E4%B8%8D%E4%B8%80%E8%87%B4/%E6%98%8E%E7%A2%BA%E3%81%AA%E7%90%86%E7%94%B1%E3%81%AF%E3%81%AA%E3%81%84%E3%81%91%E3%81%A9%E5%AB%8C/%E6%98%8E%E7%A2%BA%E3%81%AA%E7%90%86%E7%94%B1%E3%81%AF%E3%81%AA%E3%81%84%E3%81%91%E3%81%A9%E5%AB%8C.png'
    other = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E3%81%9D%E3%81%AE%E4%BB%96/%E3%81%9D%E3%81%AE%E4%BB%96.png'

    #  浪費・借金の内訳
    hang_out = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E6%B5%AA%E8%B2%BB%E3%83%BB%E5%80%9F%E9%87%91/%E9%81%8A%E3%81%B3%EF%BC%88%E3%82%AD%E3%83%A3%E3%83%90%E3%82%AF%E3%83%A9%E3%83%BB%E3%82%AE%E3%83%A3%E3%83%B3%E3%83%96%E3%83%AB%E3%83%BB%E9%85%92%EF%BC%89/%E9%81%8A%E3%81%B3%EF%BC%88%E3%82%AD%E3%83%A3%E3%83%90%E3%82%AF%E3%83%A9%E3%83%BB%E3%82%AE%E3%83%A3%E3%83%B3%E3%83%96%E3%83%AB%E3%83%BB%E9%85%92%EF%BC%89.png'
    wastemoney_debt = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E6%B5%AA%E8%B2%BB%E3%83%BB%E5%80%9F%E9%87%91/%E3%81%84%E3%82%89%E3%81%AA%E3%81%84%E3%82%82%E3%81%AE%E3%82%92%E8%B2%B7%E3%81%86%E3%83%BB%E7%9B%B8%E8%AB%87%E3%81%AA%E3%81%8F%E5%80%9F%E9%87%91%E3%81%99%E3%82%8B/%E3%81%84%E3%82%89%E3%81%AA%E3%81%84%E3%82%82%E3%81%AE%E3%82%92%E8%B2%B7%E3%81%86%E3%83%BB%E7%9B%B8%E8%AB%87%E3%81%AA%E3%81%8F%E5%80%9F%E9%87%91%E3%81%99%E3%82%8B.png'
    hide_debt = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E6%B5%AA%E8%B2%BB%E3%83%BB%E5%80%9F%E9%87%91/%E5%80%9F%E9%87%91%E3%82%92%E9%9A%A0%E3%81%97%E3%81%A6%E3%81%84%E3%81%9F/%E5%80%9F%E9%87%91%E3%82%92%E9%9A%A0%E3%81%97%E3%81%A6%E3%81%84%E3%81%9F.png'
    other = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E3%81%9D%E3%81%AE%E4%BB%96/%E3%81%9D%E3%81%AE%E4%BB%96.png'

    #  DVの内訳
    mental_dv = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/DV/%E7%B2%BE%E7%A5%9E%E7%9A%84DV/%E7%B2%BE%E7%A5%9E%E7%9A%84DV.png'
    physical_dv = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/DV/%E8%82%89%E4%BD%93%E7%9A%84DV/%E8%82%89%E4%BD%93%E7%9A%84DV.png'
    economical_dv = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/DV/%E7%B5%8C%E6%B8%88%E7%9A%84DV/%E7%B5%8C%E6%B8%88%E7%9A%84DV.png'
    sexual_dv = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/DV/%E6%80%A7%E7%9A%84DV/%E6%80%A7%E7%9A%84DV.png'
    other = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E3%81%9D%E3%81%AE%E4%BB%96/%E3%81%9D%E3%81%AE%E4%BB%96.png'

    #  浮気・男女問題の内訳
    unfaithful_adultery = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E6%B5%AE%E6%B0%97%E3%83%BB%E7%94%B7%E5%A5%B3%E5%95%8F%E9%A1%8C/%E6%B5%AE%E6%B0%97%E3%83%BB%E4%B8%8D%E5%80%AB/%E6%B5%AE%E6%B0%97%E3%83%BB%E4%B8%8D%E5%80%AB.png'
    sexless =  'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E6%B5%AE%E6%B0%97%E3%83%BB%E7%94%B7%E5%A5%B3%E5%95%8F%E9%A1%8C/%E3%82%BB%E3%83%83%E3%82%AF%E3%82%B9%E3%83%AC%E3%82%B9/%E3%82%BB%E3%83%83%E3%82%AF%E3%82%B9%E3%83%AC%E3%82%B9.png'
    sexual_dv = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/DV/%E6%80%A7%E7%9A%84DV/%E6%80%A7%E7%9A%84DV.png'
    other = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E3%81%9D%E3%81%AE%E4%BB%96/%E3%81%9D%E3%81%AE%E4%BB%96.png'

    #   その他の内訳
    relatives = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E3%81%9D%E3%81%AE%E4%BB%96/%E8%A6%AA%E6%97%8F%E3%83%BB%E8%A6%AA%E6%88%9A/%E8%A6%AA%E6%97%8F%E3%83%BB%E8%A6%AA%E6%88%9A.png'
    other = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E3%81%9D%E3%81%AE%E4%BB%96/%E3%81%9D%E3%81%AE%E4%BB%96.png'

    iA = [sense_for_money, housework_child_education, relatives_friends_relations,
          sympathy, personal_time, none_clear_reasons,
          other]
    iB = [hang_out, wastemoney_debt, hide_debt,
          other]
    iC = [mental_dv, physical_dv, economical_dv,
          sexual_dv, other]
    iD = [unfaithful_adultery, sexless, sexual_dv,
          other]
    iE = [relatives, other]

    layer1_image = list((iA, iB, iC, iD, iE))

    #  豆知識
    tips= 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E8%B1%86%E7%9F%A5%E8%AD%98/%E8%B1%86%E7%9F%A5%E8%AD%98/%E8%B1%86%E7%9F%A5%E8%AD%98example.png'

    iA1 = [tips, tips, tips]
    iA2 = [tips, tips, tips]
    iA3 = [tips, tips, tips]
    iA4 = [tips, tips, tips]
    iA5 = [tips, tips, tips]
    iA6 = [tips, tips, tips]
    iA7 = [tips, tips, tips]
    iB1 = [tips, tips, tips]
    iB2 = [tips, tips, tips]
    iB3 = [tips, tips, tips]
    iB4 = [tips, tips, tips]
    iC1 = [tips, tips, tips]
    iC2 = [tips, tips, tips]
    iC3 = [tips, tips, tips]
    iC4 = [tips, tips, tips]
    iC5 = [tips, tips, tips]
    iD1 = [tips, tips, tips]
    iD2 = [tips, tips, tips]
    iD3 = [tips, tips, tips]
    iD4 = [tips, tips, tips]
    iE1 = [tips, tips, tips]
    iE2 = [tips, tips, tips]

    layer2_image = list((list((iA1, iA2, iA3, iA4, iA5, iA6, iA7)),
                         list((iB1, iB2, iB3, iB4)),
                         list((iC1, iC2, iC3, iC4, iC5)),
                         list((iD1, iD2, iD3, iD4)),
                         list((iE1, iE2))))

    #  レイヤーにまとめる
    layers = []
    layers.append(layer0)
    layers.append(layer1)
    layers.append(layer2)

    layers_images =  []
    layers_images.append('dummy')
    layers_images.append(layer1_image)
    layers_images.append(layer2_image)

    texts = []
    texts.append('dummy')
    texts.append(text0)
    texts.append(text1)
    texts.append(text2)


    def search_text(self, message_text):
        for layer0_number, text0 in enumerate(self.layer0):
            if text0 == message_text:
                return [layer0_number]
            for layer1_number, text1 in enumerate(self.layer1[layer0_number]):
                if text1 == message_text:
                    return [layer0_number, layer1_number]
                for layer2_number, text2 in enumerate(self.layer2[layer0_number][layer1_number]):
                    if text2 == message_text:
                        return [layer0_number, layer1_number, layer2_number]
        return 'no matching'

    def decide_buttons(self, indexes):
        if len(indexes) == 1:
            buttons = self.layers[len(indexes)][indexes[0]]
            return buttons
        elif len(indexes) == 2:
            buttons = self.layers[len(indexes)][indexes[0]][indexes[1]]
            return buttons
        else:
            return 'None Buttons'

    def decide_images(self, indexes):
        if len(indexes) == 1:
            images = self.layers_images[len(indexes)][indexes[0]]
            return images
        elif len(indexes) == 2:
            images = self.layers_images[len(indexes)][indexes[0]][indexes[1]]
            return images
        else:
            return 'None Images'

    def decide_text(self, indexes):
        if len(indexes) == 1:
            text = self.texts[len(indexes)][indexes[0]]
            return text
        elif len(indexes) == 2:
            text = self.texts[len(indexes)][indexes[0]][indexes[1]]
            return text
        elif len(indexes) == 3:
            text = self.texts[len(indexes)][indexes[0]][indexes[1]][indexes[2]]
            return text
        else:
            return 'None text'


# メッセージの時に使用するクラス、主に弁護士案内の役割
class Guidance:
    guide0 = ['役に立った！']
    guide1 = ['ホームページを見てみる！', '今はまだいいかな']
    guide2 = ['連絡してみる！', '今はまだいいかな']
    guide3 = ['OK👌']
    guide4 = ['OK👍', '修正する！']
    guide5 = ['送信する']

    layers = []
    layers.append(guide0)
    layers.append(guide1)
    layers.append(guide2)
    layers.append(guide3)
    layers.append(guide4)
    layers.append(guide5)


    texts_first_0 = ['お役に立てたようでよかった😄\n残念だけど、ぼくがアドバイスできるのはここまでなんだ😔']
    texts_second_0 = ['でも安心して👍\nもっと詳しいことは弁護士さんが教えてくれるよ！\n弁護士さんに相談するとこんないいことがあるよ👌']
    texts_third_0 = ['あなたの悩みにピッタリなオススメの弁護士さんがいるから、一度ホームページを見てみない？🤔']

    texts_first_1 = ['あなたにオススメの弁護士さんはこの人だよ😄', 'また時間がある時に見てみてね👍']
    texts_second_1 = ['無料相談もあるから安心だよ👍', '他の悩みに関するアドバイスが見たい時は、前のメッセージのボタンを押してみてね👍']
    texts_third_1 = ['この弁護士さんに直接連絡することもできるよ！👌', '第三者の専門家に話を聞いてもらうのは、すごく大事なことなんだ。\nまたいつでも相談してね👍']

    texts_first_2 = ['それでは連絡してみよう！\n次の4つが必要になるよ👌', 'また時間がある時に連絡してみてね👍']
    texts_second_2 = ['名前\nふりがな\nメールアドレス\n電話番号\nを順番に入力してね👍', '他の悩みに関するアドバイスが見たい時は、前のメッセージのボタンを押してみてね👍']
    texts_third_2 = ['入力に進んでいいかな？🤔', '第三者の専門家に話を聞いてもらうのは、すごく大事なことなんだ。\nまたいつでも相談してね👍']

    texts_first_3 = ['名前を入力してね🤔']
    texts_second_3 = ['ふりがなを入力してね🤔']
    texts_third_3 = ['メールアドレスを入力してね🤔']
    texts_fourth_3 = ['電話番号を入力してね🤔']

    texts_first_4 = ['それではオススメの弁護士さんに連絡してみよう！👍']  # 修正するはguide3に戻るため、ここでは要素なし

    texts_first_5 = ['弁護士さんにあなたのお悩みを送ったよ！👌']
    texts_second_5 = ['もしあなたのお悩みが、弁護士さんの得意分野だった場合は相談に乗ってくれるよ！']
    texts_third_5 = ['※ 必ずしもご相談に繋がらないことを、予めご了承下さい。']

    layers_texts_first = []
    layers_texts_first.append(texts_first_0)
    layers_texts_first.append(texts_first_1)
    layers_texts_first.append(texts_first_2)
    layers_texts_first.append(texts_first_3)
    layers_texts_first.append(texts_first_4)
    layers_texts_first.append(texts_first_5)
    layers_texts_second = []
    layers_texts_second.append(texts_second_0)
    layers_texts_second.append(texts_second_1)
    layers_texts_second.append(texts_second_2)
    layers_texts_second.append(texts_second_3)
    layers_texts_second.append('dummy')
    layers_texts_second.append(texts_second_5)
    layers_texts_third = []
    layers_texts_third.append(texts_third_0)
    layers_texts_third.append(texts_third_1)
    layers_texts_third.append(texts_third_2)
    layers_texts_third.append(texts_third_3)
    layers_texts_third.append('dummy')
    layers_texts_third.append(texts_third_5)
    layers_texts_fourth = []
    layers_texts_fourth.append('dummy')
    layers_texts_fourth.append('dummy')
    layers_texts_fourth.append('dummy')
    layers_texts_fourth.append(texts_fourth_3)


    # 弁護士相談メリット画像
    merit1 = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E5%BC%81%E8%AD%B7%E5%A3%AB%E3%81%AB%E7%9B%B8%E8%AB%87%E3%81%99%E3%82%8B%E3%83%A1%E3%83%AA%E3%83%83%E3%83%88/%E5%BC%81%E8%AD%B7%E5%A3%AB%E3%83%A1%E3%83%AA%E3%83%83%E3%83%881.png'
    merit2 = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E5%BC%81%E8%AD%B7%E5%A3%AB%E3%81%AB%E7%9B%B8%E8%AB%87%E3%81%99%E3%82%8B%E3%83%A1%E3%83%AA%E3%83%83%E3%83%88/%E5%BC%81%E8%AD%B7%E5%A3%AB%E3%83%A1%E3%83%AA%E3%83%83%E3%83%882.png'
    merit3 = 'https://raw.githubusercontent.com/pomtaro/bengoshi_test/master/pic_bot/%E5%BC%81%E8%AD%B7%E5%A3%AB%E3%81%AB%E7%9B%B8%E8%AB%87%E3%81%99%E3%82%8B%E3%83%A1%E3%83%AA%E3%83%83%E3%83%88/%E5%BC%81%E8%AD%B7%E5%A3%AB%E3%83%A1%E3%83%AA%E3%83%83%E3%83%883.png'

    images0 = [[merit1, merit2, merit3]]
    titles0 = [['メリット1👌', 'メリット2👌', 'メリット3👌']]
    subtitles0 = [['メリット1', 'メリット2', 'メリット3']]

    layers_images = []
    layers_images.append(images0)
    layers_titles = []
    layers_titles.append(titles0)
    layers_subtitles = []
    layers_subtitles.append(subtitles0)




    def search_text(self, message_text):
        for i, list in enumerate(self.layers):
            for j, text in enumerate(list):
                if text == message_text:
                    return [i, j]

    def decide_text_first(self, indexes):
        print(indexes)
        return self.layers_texts_first[indexes[0]][indexes[1]]

    def decide_text_second(self, indexes):
        return self.layers_texts_second[indexes[0]][indexes[1]]

    def decide_text_third(self, indexes):
        return self.layers_texts_third[indexes[0]][indexes[1]]

    def decide_text_fourth(self, indexes):
        return self.layers_texts_fourth[indexes[0]][indexes[1]]

    def decide_images(self, indexes):
        return self.layers_titles[indexes[0]][indexes[0]], self.layers_images[indexes[0]][indexes[0]], self.layers_subtitles[indexes[0]][indexes[0]]

    def decide_buttons(self, indexes):
        return self.layers[indexes[0]+1]











