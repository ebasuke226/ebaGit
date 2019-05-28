from responder import *
from dictionary import *
from e_words_dictionary import *

# Rayの本体クラス
class Ray:
    def __init__(self):
        # 辞書オブジェクトDictionaryを生成
        self.__dictionary = Dictionary()
        
        # 応答オブジェクトを生成
        self.__res_history = HistoryResponder(self.__dictionary)

        # 学習オブジェクトを生成
        self.__study_history = StudyHistoryResponder(self.__dictionary)

        #
        self.__words_dictionary = WordsDictionary()
        
        # もうひと科目の応答オブジェクトを生成
        self.__res_word = WordResponder(self.__words_dictionary)

        # もうひと科目の学習オブジェクトを生成
        self.__study_word = StudyWordResponder(self.__words_dictionary)

    def dialogue(self, input, subject, study, what):
        # 川崎のモードであり、かつ最初の質問であれば実行される
        if subject == 0 and study == 0:
            # 応答オブジェクトをself.responderに代入
            self.responder =  self.res_history
        # 川崎モードであり、答えが入力されたときに実行される
        elif subject == 0 and study == 1:
            # 学習オブジェクトをself.responderに代入
            self.responder =  self.study_history

        # もうひと科目のモードであり、かつ最初の質問であれば実行される
        elif subject == 1 and study == 0:
            # 応答オブジェクトをself.responderに代入
            self.responder =  self.res_word
        # もうひと科目のモードであり、答えが入力されたときに実行される
        elif subject == 1 and study == 1:
            # 学習オブジェクトをself.responderに代入
            self.responder =  self.study_word
        # 応答を返す
        return self.responder.response(input, what)
		
    def save(self):
        """ Dictionaryのsave()を呼ぶ中継メソッド
        """
        self.dictionary.save()
        self.words_dictionary.save()

    # dictionaryプロパティ
    @property
    def dictionary(self):
        return self.__dictionary

    # res_historyプロパティ
    @property
    def res_history(self):
        return self.__res_history

    # study_historyプロパティ
    @property
    def study_history(self):
        return self.__study_history

    # words_dictionaryプロパティ
    @property
    def words_dictionary(self):
        return self.__words_dictionary

    # res_wordプロパティ
    @property
    def res_word(self):
        return self.__res_word

    # study_wordプロパティ
    @property
    def study_word(self):
        return self.__study_word

#=================================================
# プログラムの実行ブロック
#=================================================
if __name__  == '__main__':
    
    ray = Ray()
    ans = ray.dialogue('世界四大文明', 0, 0, '')
    print(ans)

    ans = ray.dialogue('アレクサンドロス大王の後継者', 0, 0, '')
    print(ans)

    ans = ray.dialogue('ディアドコイ', 0, 1, 'アレクサンドロス大王の後継者')
    print(ans)
    print(ray.dictionary.history)

    ans = ray.dialogue('distinct', 1, 0, '')
    print('words==', ans)
    print(type(ray.responder))

    ans = ray.dialogue('variation', 1, 1, '変化、変動')
    print(ans)
    print(ray.words_dictionary.words)

    ray.save()
