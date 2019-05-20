include ../../make.inc

MD		=	$(FINAL_PROJECT_DIR)/final_project.md
MD_EXT	=	$(FINAL_PROJECT_DIR)/%.md : %.Rmd

all : $(ALL_FILES)

clean :
	$(call cleanup)

$(HOMEWORK_DIR) :
	$(call setup_build_directory)

$(MD) : $(MD_EXT) | $(FINAL_PROJECT_DIR)
	$(call rmarkdown_render,$(MD_OUTPUT))
