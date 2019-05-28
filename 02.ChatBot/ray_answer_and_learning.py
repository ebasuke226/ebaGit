import time

words = {}

def read():
    # グローバル変数を使用するための記述
    global words
    with open('data/English_words.txt', 'r', encoding = 'utf_8'
              ) as file:
        lines = file.readlines()      # ファイル終端までのすべてのデータを取得

    new_lines = []
    separate = []
    for line in lines:
        line = line.rstrip('\n')
        if (line!=''):
            new_lines.append(line)
    for line in new_lines:
        sp = line.split('\t')
        separate.append(sp)
    words = dict(separate)

def study():
    write_lines = []
    for key, val in words.items():
        write_lines.append(key + '\t' + val + '\n')
    write_lines.sort()
    with open('data/English_words.txt', 'w', encoding = 'utf_8') as f:
        f.writelines(write_lines)


#=================================================
# プログラムの起点
#=================================================
if __name__  == '__main__':
    read()
    print('単語の意味を答えるね')
    while True:
        word =input('>>>')
        if word == 'OK':
            study()
            print('バイバ～イ')
            break
        elif word in words:
            print('「' + words[word] + '」って意味だよ')
        else:
            print('わかんないよ～')
            meaning =input('意味を教えて>')
            while not meaning:
                meaning =input('意味を教えて>')
            words[word] = meaning
            print('記憶中......')
            time.sleep(3)
