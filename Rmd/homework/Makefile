include ../../make.inc

MD		=	$(HOMEWORK_DIR)/homework1.md										\
			$(HOMEWORK_DIR)/homework2.md										\
			$(HOMEWORK_DIR)/homework3.md										\
			$(HOMEWORK_DIR)/homework4.md										\
			$(HOMEWORK_DIR)/homework5.md										\
			$(HOMEWORK_DIR)/homework6.md										\
			$(HOMEWORK_DIR)/homework7.md
MD_EXT	=	$(HOMEWORK_DIR)/%.md : %.Rmd

all : $(ALL_FILES)

clean :
	$(call cleanup)

$(HOMEWORK_DIR) :
	$(call setup_build_directory)

$(MD) : $(MD_EXT) | $(HOMEWORK_DIR)
	$(call rmarkdown_render,$(MD_OUTPUT))
