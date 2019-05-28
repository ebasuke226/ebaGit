from dictionary import *
from e_words_dictionary import *

class Responder:
    def __init__(self, dictionary):

        self.__dictionary = dictionary

    def response(self, input, what):
        return ''

    # __dictionaryのゲッター
    def get_dictionary(self):
        return self.__dictionary
    # __dictionaryのセッター
    def set_dictionary(self, dictionary):
        self.__dictionary = dictionary

    # dictionaryプロパティの定義
    dictionary = property(get_dictionary, set_dictionary)		


class HistoryResponder(Responder):
    def response(self, input, what):
        if input in self.dictionary.history:
            return '「' + self.dictionary.history[input] + '」だよ'
        else:
            return('わかんないよ～答えを教えて!')

class StudyHistoryResponder(Responder):
    def response(self, input, what):
        self.dictionary.history[what] = input
        return '学習したよ～'

class WordResponder(Responder):
    def response(self, input, what):
        if input in self.dictionary.words:
            return '「' + self.dictionary.words[input] + '」だよ'
        else:
            return('わかんないよ～答えを教えて!')

class StudyWordResponder(Responder):
    def response(self, input, what):
        self.dictionary.words[what] = input
        return '学習したよ～'
#=================================================
# プログラムの実行ブロック
#=================================================
if __name__  == '__main__':
    
    # 辞書オブジェクトDictionaryを生成
    dictionary = Dictionary()
    history_resp = HistoryResponder(dictionary)
    ans = history_resp.response('世界四大文明', '')
    print(ans)
    study_resp = StudyHistoryResponder(dictionary)
    ans = study_resp.response('ディアドコイ', 'アレクサンドロス大王の後継者')
    print(dictionary.history)
    
    # 辞書オブジェクトWordsDictionaryを生成
    dictionary = WordsDictionary()
    word_resp = WordResponder(dictionary)
    ans = word_resp.response('anticipate', '')
    print(ans)
    study_word = StudyWordResponder(dictionary)
    ans = study_word.response('variation', '変化、変動')
    print(dictionary.words)
