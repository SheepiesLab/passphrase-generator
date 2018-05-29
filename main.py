import os
import struct
import argparse


def ppwgen_selector(words):
	random = struct.unpack("=I", os.urandom(4))[0] % len(words)
	return words[random]


def ppwgen_load(options):
	filename = "google-10000-english/google-10000-english"
	if options["usa"] == True:
		filename = filename + "-usa"
	if options["noswears"] == True:
		filename = filename + "-no-swears"
	filename = filename + ".txt"
	
	with open(filename, "r") as f:
		words = f.readlines()
		words = list(map(lambda word: word.strip(), words))
		if options["wordlen"]["min"] > 0:
			words = [word for word in words if len(word) >= options["wordlen"]["min"]]
		if options["wordlen"]["max"] > 0:
			words = [word for word in words if len(word) <= options["wordlen"]["max"]]
		
	return words


def main():
	parser = argparse.ArgumentParser(description="Generate password phrase from google-10000-english 10000 most frequent English words.")
	parser.add_argument('-u', '--usa', dest='usa', action='store_true', help='Use USA version of 10000 most frequent words.')
	parser.add_argument('-s', '--no-swears', dest='noswears', action='store_true', help='Exclude swear words.')
	parser.add_argument('-n', '--word-count', dest='wordcount', action='store', type=int, default=4, help='Number of words to form a pass phrase. (default: 4)')
	parser.add_argument('-X', '--max-word-length', dest='maxlen', action='store', nargs=1, type=int, default=0, help='Maximum number of letters in a word. (0 means unlimited, default: 0)')
	parser.add_argument('-M', '--min-word-length', dest='minlen', action='store', nargs=1, type=int, default=6, help='Minimum number of letters in a word. (0 means unlimited, default: 6)')

	args = parser.parse_args()
	
	words = ppwgen_load({
		"usa": args.usa,
		"noswears": args.noswears,
		"wordlen": {
			"min": args.minlen,
			"max": args.maxlen
		}
	})
	
	selected_words = []
	for i in range(args.wordcount):
		selected_words.append(ppwgen_selector(words))
	
	print(' '.join(selected_words))

if __name__ == "__main__":
	main()
