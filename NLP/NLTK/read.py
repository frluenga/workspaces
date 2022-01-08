import re
import nltk
from bs4 import BeautifulSoup
from urllib import request
from nltk import word_tokenize


nltk.download('stopwords')

lines = []
def get_text(file):

    with open(file,mode='r',encoding='utf8') as f:
        for line in f:
            lines.append(line)
    
    return lines


def tokenize(file):
    text = get_text(file)
    tokenizer = nltk.RegexpTokenizer('\w+')
    tokens = []
    for line in text:
        tokens.append(tokenizer.tokenize(line))
    
    flatten = [w for l in tokens for w in l if len(w)>2]

    return flatten


def freq_words(url, n, encoding = 'utf8'):
    req = request.urlopen(url)
    html = req.read().decode(encoding)
    text = BeautifulSoup(html,'html.parser')
    tokens = re.findall('\w+', text)
    tokens = [t.lower() for t in tokens]
    fd = nltk.FreqDist(tokens)
    return [t for (t, _) in fd.most_common(n)]


if __name__ == '__main__':
    tokenize('book.txt')
