import os

from preprocessing import get_tokens


def inverted_index_map(data_folder, get_doc_tokens=False):
    files = os.listdir(data_folder)
    _inverted_index_map = {}
    doc_tokens = {}
    for f_ in files:
        data = ''
        with open(f"{data_folder}/{f_}", 'r') as f:
            data += f.read()
            tokens = get_tokens(data)
            doc_tokens[int(f_.split('.')[0])] = tokens
            for token in tokens:
                if _inverted_index_map.get(token) is None:
                    _inverted_index_map[token] = [int(f_.split('.')[0])]
                else:
                    _inverted_index_map[token].append(int(f_.split('.')[0]))
    if get_doc_tokens:
        return _inverted_index_map, doc_tokens
    else:
        return _inverted_index_map


def main():

    data_folder = "pages"
    _inverted_index_map = inverted_index_map(data_folder)


if __name__ == '__main__':
    main()
