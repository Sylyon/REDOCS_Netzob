#-------------------------------------------------------------------------
# Edit this part according to the paper
FILENAME=pres
DEADLINE="Nov 01, 2017 07:00:00 (UTC)"
PAGELIMIT=
#-------------------------------------------------------------------------

PSFORMAT=letter
OUTPUT_DIR=output
REMAINING=`date -d @$$(( $$(date -d $(DEADLINE) +%s) - $$(date +%s) )) -u +"%d days %H hours and %M minutes"`
# +%s -d 20120115`)/86400

LATEX=pdflatex -interaction=batchmode -output-directory=$(OUTPUT_DIR)
LATEXV=pdflatex -output-directory=$(OUTPUT_DIR)
RERUN='There were undefined references'
BIBWARNING='Warning--I didn.t find a database entry'

TODOS=`cat *.tex | grep -v "[ \t]*%" | grep -o "\\fix{" | wc -l`

.PHONY: pdf ps tex status clean

all: pdf 

verbose:
	@echo -n "Compiling ......"
	@${LATEXV} $(FILENAME).tex 
	@echo -n  "Bibliography........"
	@bibtex -terse $(OUTPUT_DIR)/$(FILENAME)

pdf:	
	@echo -e "\033[33m >>> Deadline in " $(REMAINING) "\033[0m" 
	@if [ ! -d $(OUTPUT_DIR) ]; then mkdir $(OUTPUT_DIR); fi
	@if [ $(TODOS) -ne 0 ]; then echo "\033[31m !!! Still $(TODOS) TODOs left to address !!! \033[0m"; fi
	@echo "Compiling \"$(FILENAME).pdf\" :"
	@echo -n " Compiling (first pass)......["
	@${LATEX} $(FILENAME).tex > /dev/null; \
	 if [ $$? -ne 0 ]; then /bin/echo -e "\033[31mFAIL\033[0m]\033[31m"; \
	 grep -A 2 '^!' $(OUTPUT_DIR)/$(FILENAME).log; echo "\033[0mCheck $(OUTPUT_DIR)/$(FILENAME).log for more info about the errors"; exit 1; \
	 else /bin/echo -e "\033[32mOK\033[0m]";  fi
	@echo -n " Compiling (second pass).....["; ${LATEX} $(FILENAME).tex > /dev/null; \
	if [ $$? -ne 0 ]; then /bin/echo -e "\033[31mFAIL\033[0m]"; else /bin/echo -e "\033[32mOK\033[0m]";  fi;
	@echo -n "           (third pass)......["; ${LATEX} $(FILENAME).tex > /dev/null; \
	if [ $$? -ne 0 ]; then /bin/echo -e "\033[31mFAIL\033[0m]"; else /bin/echo -e "\033[32mOK\033[0m]";  fi;
	@echo -e "The paper now has\033[32m" `pdfinfo $(OUTPUT_DIR)/$(FILENAME).pdf  | sed -n "s/^Pages://p" | grep -o '[0-9]*'` "\033[0mpages out of\033[32m" $(PAGELIMIT) "\033[0m"

ps:	tex
	dvips -o $(FILENAME).ps -t $(PSFORMAT) $(FILENAME).dvi

tex:
	latex $(FILENAME).tex
	bibtex $(FILENAME)
	latex $(FILENAME).tex
	latex $(FILENAME).tex


clean:
	rm output/*
	rm -f *.dvi *.ps *.aux *.log *.bbl *.blg *~ *.out *.bak *.pdf

