class Dictionary:
    def __init__(self):
        # 辞書オブジェクトを作成
        self.__load_history()
    
    # ファイルを読み込み、辞書オブジェクトを作成するメソッド
    def __load_history(self):
        with open('data/frontale.txt', 'r', encoding = 'utf_8'
                  ) as file:
            # 1行ずつ読み込んでリストにする
            lines = file.readlines()
        # 末尾の改行を取り除いた行データを保持するリスト
        new_lines = []
        # ファイルデータのリストから1行データを取り出す
        for line in lines:
            # 末尾の改行文字(\n)を取り除く
            line = line.rstrip('\n')
            # 空文字をチェック
            if (line!=''):
                # 空文字以外をリストnew_linesに追加
                new_lines.append(line)
        # 行データの単語とその意味を要素にするリスト
        separate = []
        # 末尾の改行を取り除いたリストから1行データを取り出す
        for line in new_lines:
            # タブで分割して質問と答えのリストを作る
            sp = line.split('\t')
            # リストseparateに追加する
            separate.append(sp)
        # 「質問:答え」のかたちで辞書オブジェクトにする
        self.__history = dict(separate)

    # 辞書ファイルに書き込むメソッド
    def save(self):
        write_lines = []
        for key, val in self.history.items():
            write_lines.append(key + '\t' + val + '\n')
        with open('data/world_history.txt', 'w', encoding = 'utf_8') as f:
            f.writelines(write_lines)

    # __historyのゲッター
    def get_history(self):
        return self.__history
    # __historyのセッター
    def set_history(self, history):
        self.__history = history

    # historyプロパティの定義
    history = property(get_history, set_history)		
#=================================================
# プログラムの実行ブロック
#=================================================
if __name__  == '__main__':
    
    # 辞書オブジェクトDictionaryを生成
    dictionary = Dictionary()
    print(dictionary.history)
    dictionary.save()

