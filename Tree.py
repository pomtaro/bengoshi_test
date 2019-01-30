class Tree():
    top = ["労働について", "離婚・男女問題について", "借金について"]
    layer0 = list(top)

    A = ["給与について", "労働時間や休暇について", "人間関係のトラブル",
         "人事異動と就職・退職", "労働契約と社会保険・労災", "トラブルの相続先と解決方法",
         "上記にあてはまらない"]
    B = ["お金のトラブル", "離婚と子ども", "男女トラブル",
         "上記にあてはまらない"]
    C = ["借金の減額や見直し", "取り立てと差し押さえ", "身近な人の借金",
         "過去の借金", "借金の基礎知識", "上記にあてはまらない"]
    layer1 = list((A, B, C))

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
    C6 = ["ホームページを見てみる", "今は見ない"]
    layer2 = list((list((A1, A2, A3, A4, A5, A6, A7)),
                   list((B1, B2, B3, B4)),
                   list((C1, C2, C3, C4, C5, C6))))

    layers = []
    layers.append(layer0)
    layers.append(layer1)
    layers.append(layer2)

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

