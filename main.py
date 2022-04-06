from data_reader import index_reader
from vector_search import search

while True:
	query = input().lower()
	pages, weights = search(query)
	idx_path = index_reader()
	if len(pages) == 0:
		print('Nothing was found.')
	for i in range(len(pages)):
		print(f"page: {idx_path[pages[i]]}, weight: {weights[i]}")
