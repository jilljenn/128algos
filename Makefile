SLIDES_PDF=intro.pdf structures.pdf taxis.pdf graphes.pdf extras.pdf
FIGURES_DOT=$(wildcard *.dot)
FIGURES_PDF=$(FIGURES_DOT:.dot=.pdf) euler.pdf euler-paris.pdf levenshtein.pdf

all: $(FIGURES_PDF) $(SLIDES_PDF)

%.pdf: %.md
	pandoc -t beamer $< -o $@

%.pdf: %.tex
	xelatex $<

%.pdf: %.dot
	dot -Tpdf $< -o $@

clean:
	rm -f $(SLIDES_PDF)
