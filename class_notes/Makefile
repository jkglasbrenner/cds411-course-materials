include ../make.inc

DIRS	=	class01																\
			class03																\
			class04

.PHONY : all clean $(DIRS)

all : $(DIRS)

clean :
	$(foreach dir,$(DIRS),cd $(dir) && $(MAKE) clean && cd ../;)

$(DIRS) :
	$(MAKE) -C $@
