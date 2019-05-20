include ../../make.inc

CLASS_NUMBER	=	$(notdir $(patsubst %/,%,$(CURDIR)))

JUPYTER_NB2PDF	=	$(OUTPUT_DIR)/$(CLASS_NUMBER)_notebook.pdf
JUPYTER_NB2RST	=	$(OUTPUT_DIR)/$(CLASS_NUMBER)_notebook.rst

all : $(OUTPUT_DIR) $(ALL_FILES)

clean :
	$(call cleanup)

$(OUTPUT_DIR) :
	$(call setup_build_directory)

$(JUPYTER_NB2PDF) : $(JUPYTER_NB2PDF_EXT) | $(OUTPUT_DIR)
	$(call nbconvert,pdf,$(OUTPUT_DIR))

$(JUPYTER_NB2RST) : $(JUPYTER_NB2RST_EXT) | $(OUTPUT_DIR)
	$(call nbconvert,rst,$(OUTPUT_DIR))
