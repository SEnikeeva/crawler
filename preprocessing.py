import re

import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer


def get_tokens(data, is_set=True):
    data = data.lower()
    data = re.sub(r'https?://\S+', 'URL', data)
    data = re.sub(r'[^a-zA-Z]+', ' ', data)
    tokens_ = nltk.word_tokenize(data)
    tokens_ = list(set(tokens_)) if is_set else tokens_
    tokens = []
    for token in tokens_:
        if len(wordnet.synsets(token)) != 0:
            tokens.append(token)

    stop_words = set(stopwords.words('english'))
    tokens = list(set(tokens)) if is_set else tokens
    tokens = [word for word in tokens if word not in stop_words]
    if is_set:
        return list(set(tokens))
    else:
        return tokens


def group_by_lemma(tokens):
    lemma_tokens = {}
    lemmatizer = WordNetLemmatizer()
    for token in tokens:
        lemma = lemmatizer.lemmatize(token)
        if lemma_tokens.get(lemma) is None:
            lemma_tokens[lemma] = [token]
        else:
            lemma_tokens[lemma].append(token)
    return lemma_tokens
