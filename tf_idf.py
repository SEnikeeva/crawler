from data_reader import lemmas_reader
from inverted_index import inverted_index_map
from collections import Counter
import math


def count_tokens(doc_tokens, token_lemma):
    counter = {}
    for doc, tokens in doc_tokens.items():
        lemmas = list(set([token_lemma[token] for token in tokens]))
        counter[doc] = dict(counter=Counter(tokens), size=len(tokens), lemmas=lemmas)
    return counter


def main():
    data_folder = "pages"
    _inverted_index_map, doc_tokens = inverted_index_map(data_folder, get_doc_tokens=True, is_set=False)
    lemma_tokens, token_lemma = lemmas_reader()
    count_doc_tokens = count_tokens(doc_tokens, token_lemma)
    tf_idf_doc = {}
    tf_idf_doc_lemmas = {}

    for doc, params in count_doc_tokens.items():
        tf_idf_doc[doc] = []
        tf_idf_doc_lemmas[doc] = []
        with open(f"tf_idf_terms/{doc}.txt", 'w') as f:
            for token, amount in params['counter'].items():
                tf = amount / params['size']
                idf = math.log10(len(doc_tokens) / len(_inverted_index_map[token]))
                f.write(f"{token} {idf} {tf * idf}\n")

        with open(f"tf_idf_lemmas/{doc}.txt", 'w') as f:
            for lemma in params['lemmas']:
                sum_tokens = 0
                tokens_in = set()
                for token in lemma_tokens[lemma]:
                    if params['counter'].get(token) is not None:
                        sum_tokens += params['counter'][token]
                        tokens_in = tokens_in.union(_inverted_index_map[token])
                tf = sum_tokens / params['size']
                idf = math.log10(len(doc_tokens) / len(tokens_in))
                f.write(f"{lemma} {idf} {tf * idf}\n")


if __name__ == '__main__':
    main()
