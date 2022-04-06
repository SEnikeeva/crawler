import math
from functools import cmp_to_key

from boolean_search import boolean_search
from embeddings import make_vector
from tf_idf import get_lemmas_tf_idf_map


def make_comparator(weights):
	def compare(a, b):
		return weights[a] - weights[b]

	return compare


def calculate_page_weight(page_dict, search_dict):
	sum_ = 0
	sum_a = 0
	sum_b = 0
	for token in search_dict.keys():
		sum_ += page_dict[token] * search_dict[token]
		sum_a += page_dict[token] * page_dict[token]
		sum_b += search_dict[token] * search_dict[token]
	if sum_ == 0 or sum_a == 0 or sum_b == 0:
		return 0
	return sum_ / (math.sqrt(sum_a) * math.sqrt(sum_b))


def search(query):
	pages_weights = {}
	search_vector = make_vector(query)
	suitable_pages = boolean_search(query)
	for page in suitable_pages:
		pages_weights[page] = calculate_page_weight(get_lemmas_tf_idf_map(page), search_vector)
	ranged_pages = sorted(suitable_pages, key=cmp_to_key(make_comparator(pages_weights)), reverse=True)
	return ranged_pages, [pages_weights[page] for page in ranged_pages]

# ans = search('transformers|computer&vision')
