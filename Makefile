all:
	# pandoc -t beamer intro.md -o intro.pdf
	# pandoc -t beamer structures.md -o structures.pdf
	# pandoc -t beamer taxis.md -o taxis.pdf
	pandoc -t beamer graphes.md -o graphes.pdf
	# pandoc -t beamer extras.md -o extras.pdf
	# open intro.pdf
	# open structures.pdf
	# open taxis.pdf
	open graphes.pdf
	# open extras.pdf

levenshtein:
	dot -Tpdf levenshtein.dot > levenshtein.pdf
	open levenshtein.pdf
