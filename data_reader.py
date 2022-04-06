import os


def historically_justified(data_folder):
    data = ''
    files = os.listdir(data_folder)
    for f_ in files:
        with open(f"{data_folder}/{f_}", 'r') as f:
            data += f.read()
    return data


def lemmas_reader(lemmas_path='lemmas.txt'):
    lemma_tokens = {}
    token_lemma = {}
    with open(lemmas_path, 'r') as f:
        for line in f.readlines():
            words = line.split()
            lemma_tokens[words[0]] = words[1:]
            for token in words[1:]:
                token_lemma[token] = words[0]

    return lemma_tokens, token_lemma


def index_reader(index_path='index.txt'):
    idx_path = {}
    with open(index_path, 'r') as f:
        for line in f.readlines():
            words = line.split()
            idx_path[int(words[0].split('.')[0])] = words[1]
    return idx_path
