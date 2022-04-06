from data_reader import historically_justified
from preprocessing import get_tokens, group_by_lemma


def fetch_all_tokens():
	with open("tokens.txt", "r") as f:
		lines = [line.rstrip() for line in f]
		return lines


def main():
	data_folder = "pages"
	data = historically_justified(data_folder)
	tokens = get_tokens(data)
	lemma_tokens = group_by_lemma(tokens)

	with open("tokens.txt", 'w') as f:
		for token in tokens:
			f.write(f"{token}\n")

	with open("lemmas.txt", 'w') as f:
		for lemma, tokens_ in lemma_tokens.items():
			f.write(f"{lemma}")
			for token in tokens_:
				f.write(f" {token}")
			f.write('\n')


if __name__ == '__main__':
	main()
