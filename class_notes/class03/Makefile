include ../../make.inc

CLASS_NUMBER	=	$(notdir $(patsubst %/,%,$(CURDIR)))

XARINGAN		=	$(OUTPUT_DIR)/$(CLASS_NUMBER)_slides.html

all : $(OUTPUT_DIR) $(ALL_FILES)

clean :
	$(call cleanup)

$(OUTPUT_DIR) :
	$(call setup_build_directory)

$(XARINGAN) : $(XARINGAN_EXT) | $(OUTPUT_DIR)
	$(call rmarkdown_render,$(XARINGAN_OUTPUT))
