include ../../make.inc

CLASS_NUMBER	=	$(notdir $(patsubst %/,%,$(CURDIR)))

all : $(OUTPUT_DIR) $(ALL_FILES)

clean :
	$(call cleanup)

$(OUTPUT_DIR) :
	$(call setup_build_directory)
