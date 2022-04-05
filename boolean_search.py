from inverted_index import inverted_index_map


def evaluate_and_expression(expression, tokens):
	'''
	:rtype: bool
	'''
	expr_tokens = expression.split('&')
	for token in expr_tokens:
		if token not in tokens:
			return False
	return True


def boolean_search(query):
	'''
	:type query: str
	:rtype: list
	'''
	suitable_pages = []
	query = query.replace(' ', '')
	and_list = query.split('|')
	_, page_tokens_map = inverted_index_map('pages', get_doc_tokens=True)
	for page in page_tokens_map.keys():
		page_boolean = False
		for and_expression in and_list:
			page_boolean = page_boolean or evaluate_and_expression(and_expression, page_tokens_map[page])
		if page_boolean:
			suitable_pages.append(page)
	return sorted(suitable_pages)
