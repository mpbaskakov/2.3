import chardet
import os.path
import json

def detect_encoding(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        s = result['encoding']
        return s

def find_news_files():
    files = os.listdir(".")
    for i in files:
        if i.endswith('.py'):
            files.remove(i)
    return files

def delete_small_words(listname):
    # listname = [word for word in listname if len(word) >= 6]
    newlist = []
    for i in listname:
        if len(i) >= 6:
            newlist.append(i)
    return newlist

def count_words():
    for i in find_news_files():
        with open(i, 'r', encoding=detect_encoding(i)) as f:
            file = json.load(f)
            words = []
            for n in file['rss']['channel']['items']:
                words += (n['description'].split(' '))
            words_long = delete_small_words(words)
            count_words = {i: words_long.count(i) for i in words_long}
            top_words = dict(sorted(count_words.items(), key=lambda item: item[1], reverse=True)[:10])
            print(top_words)

count_words()


