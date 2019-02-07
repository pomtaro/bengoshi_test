

class Tree():
    top = ["性格の不一致", "浪費、借金", "DV",
           "浮気、男女問題", "その他"]
    layer0 = list(top)

    top = ["性格の不一致ですね。もう少し詳しく教えてください。", "浪費、借金ですね。もう少し詳しく教えてください。", "DVですね。もう少し詳しく教えてください。",
           "浮気、男女問題ですね。もう少し詳しく教えてください。", "その他ですね。もう少し詳しく教えてください。"]
    text0 = list(top)

    A = ["金銭感覚、生活スタイル", "家事、育児、教育", "親族、友達付き合い",
         "思いやり", "一人の時間", "明確な理由はないけど嫌",
         "その他"]
    tA = ['お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？', 'お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？', 'お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？',
          'お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？', 'お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？', 'お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？',
          'お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？']
    B = ["遊び（キャバクラ、酒、ギャンブル）", "いらないものを買う、相談なく借金する", "借金を隠していた",
         "その他"]
    tB = ['お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？', 'お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？', 'お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？',
          'お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？']
    C = ["精神的DV", "肉体的DV", "経済的DV、生活費を渡さない",
         "性的DV", "その他"]
    tC = ['お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？', 'お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？', 'お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？',
          'お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？', 'お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？']
    D = ["浮気、不倫", "セックスレス", "性的DV",
         "その他"]
    tD = ['お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？', 'お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？', 'お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？',
          'お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？']
    E = ["親戚、親族", "その他"]
    tE = ['お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？', 'お客様のお力になれるかもしれません！一度ホームページをご覧になってみませんか？']
    layer1 = list((A, B, C, D, E))
    text1 = list((tA, tB, tC, tD, tE))

    A1 = ["ホームページを見てみる", "今は見ない"]
    A2 = ["ホームページを見てみる", "今は見ない"]
    A3 = ["ホームページを見てみる", "今は見ない"]
    A4 = ["ホームページを見てみる", "今は見ない"]
    A5 = ["ホームページを見てみる", "今は見ない"]
    A6 = ["ホームページを見てみる", "今は見ない"]
    A7 = ["ホームページを見てみる", "今は見ない"]
    B1 = ["ホームページを見てみる", "今は見ない"]
    B2 = ["ホームページを見てみる", "今は見ない"]
    B3 = ["ホームページを見てみる", "今は見ない"]
    B4 = ["ホームページを見てみる", "今は見ない"]
    C1 = ["ホームページを見てみる", "今は見ない"]
    C2 = ["ホームページを見てみる", "今は見ない"]
    C3 = ["ホームページを見てみる", "今は見ない"]
    C4 = ["ホームページを見てみる", "今は見ない"]
    C5 = ["ホームページを見てみる", "今は見ない"]
    D1 = ["ホームページを見てみる", "今は見ない"]
    D2 = ["ホームページを見てみる", "今は見ない"]
    D3 = ["ホームページを見てみる", "今は見ない"]
    D4 = ["ホームページを見てみる", "今は見ない"]
    E1 = ["ホームページを見てみる", "今は見ない"]
    E2 = ["ホームページを見てみる", "今は見ない"]

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

    layers = []
    layers.append(layer0)
    layers.append(layer1)
    layers.append(layer2)

    layers_images =  []
    layers_images.append('dummy')
    layers_images.append(layer1_image)

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
            buttons = self.layers_images[len(indexes)][indexes[0]]
            return buttons
        elif len(indexes) == 2:
            buttons = self.layers_images[len(indexes)][indexes[0]][indexes[1]]
            return buttons
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
