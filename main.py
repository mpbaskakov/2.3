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
    files = [f for f in os.listdir(".") if f.endswith('.json')]
    return files


def delete_small_words(listname):
    listname = [word for word in listname if len(word) >= 6]
    return listname


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


if __name__ == "__main__":
    count_words()
