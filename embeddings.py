from nltk.stem import WordNetLemmatizer

from data_reader import lemmas_reader


def get_all_lemmas():
	tmp, _ = lemmas_reader()
	return tmp.keys()


def empty_lemmas_dict():
	dictionary = {}
	all_lemmas = get_all_lemmas()
	for token in all_lemmas:
		dictionary[token] = 0
	return dictionary


def make_vector(query):
	lemmas = set()
	dictionary = empty_lemmas_dict()
	vector = {}
	all_lemmas = get_all_lemmas()
	query = query.replace(' ', '')
	query = query.replace('|', '&')
	query_words = query.split('&')
	lemmatized_words = []
	for i in range(len(query_words)):
		lemmatized_words.append(WordNetLemmatizer().lemmatize(query_words[i]))
	filtered_lemmatized_words = list(filter(lambda x: x in all_lemmas, lemmatized_words))
	for word in filtered_lemmatized_words:
		dictionary[word] = dictionary[word] + 1
		lemmas.add(word)

	for token in all_lemmas:
		vector[token] = 0
	for token in lemmas:
		vector[token] = dictionary[token] / float(len(filtered_lemmatized_words))
	return vector
