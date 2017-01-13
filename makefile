CXX := g++

ARG_WARNING := -Wall -Wextra -Wpedantic
ARG_INCLUDE := -Idependencies/include
ARG_DEBUG   := -g -O0
ARG_RELEASE := -O3
ARG_LINK    := -Ldependencies/lib64 -lSDL2 -lGL -lGLEW

DEBUG_ARGS    = $(ARG_WARNING) $(ARG_DEBUG)
RELEASE_ARGS  = $(ARG_WARNING) $(ARG_RELEASE)
ARGS = $(DEBUG_ARGS)

MODULE_LIST   := .
MODULE_OUTPUT := $(addprefix obj/, $(MODULE_LIST))
SRC_LIST    := $(foreach mod,$(MODULE_LIST),$(wildcard src_gfx/$(mod)/*.cpp))
OBJ_LIST    := $(patsubst src_gfx/%.cpp,obj/%.o,$(SRC_LIST))

.PHONY: debug release clean program

debug: program

release: ARGS = $(RELEASE_ARGS)
release: program

program: $(MODULE_OUTPUT)
program: libgfx.so

obj/%.o: src_gfx/%.cpp
	@echo $(CXX) $^
	@$(CXX) $< $(ARG_WARNING) $(ARGS) $(ARG_INCLUDE) -fPIC -c -o $@

libgfx.so: $(OBJ_LIST)
	@echo Linking $@
	@$(CXX) $^ $(ARG_WARNING) $(ARGS) $(ARG_LINK) -shared -o $@

define make-obj-dirs
$1:
	mkdir -p $$@
endef

$(foreach mods,$(MODULE_OUTPUT),$(eval $(call make-obj-dirs,$(mods))))

clean:
	rm -rf obj
	rm -f libgfx.so
