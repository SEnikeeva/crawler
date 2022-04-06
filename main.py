from vector_search import search

while True:
	query = input().lower()
	pages, weights = search(query)
	if len(pages) == 0:
		print('Nothing was found.')
	for i in range(len(pages)):
		print('page: ' + 'file:///home/xiu-xiu/PythonProjects/crawler/htmls/' + str(
			pages[i]) + '.html, ' + 'weight: ' + str(weights[i]))
