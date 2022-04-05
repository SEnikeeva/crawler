import os

from preprocessing import get_tokens


def inverted_index_map(data_folder, get_doc_tokens=False, is_set=True):
    files = os.listdir(data_folder)
    _inverted_index_map = {}
    doc_tokens = {}
    for f_ in files:
        data = ''
        with open(f"{data_folder}/{f_}", 'r') as f:
            data += f.read()
            tokens = get_tokens(data, is_set=is_set)
            doc_tokens[int(f_.split('.')[0])] = tokens
            for token in tokens:
                doc_idx = int(f_.split('.')[0])
                if _inverted_index_map.get(token) is None:
                    _inverted_index_map[token] = [doc_idx]
                else:
                    if doc_idx not in _inverted_index_map[token]:
                        _inverted_index_map[token].append(doc_idx)
    if get_doc_tokens:
        return _inverted_index_map, doc_tokens
    else:
        return _inverted_index_map


def main():

    data_folder = "pages"
    _inverted_index_map = inverted_index_map(data_folder)


if __name__ == '__main__':
    main()
