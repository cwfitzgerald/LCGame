#include <GL/glew.h>
#include <SDL2/SDL.h>

#include "libgfx.hpp"
#include <iostream>

struct SDL_Context_t {
	SDL_Window* window;
	SDL_GLContext gl_context;
} sdl_context;

extern "C" LCG_DLLEXPORT int SetupRenderer() {
	SDL_SetMainReady();
	if (SDL_Init(SDL_INIT_VIDEO | SDL_INIT_TIMER) != 0) {
		std::cerr << "Unable to initalize SDL: " << SDL_GetError() << '\n';
		return 1;
	}

	sdl_context.window =
	    SDL_CreateWindow("LCGame", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 1280, 720, SDL_WINDOW_OPENGL);

	if (!sdl_context.window) {
		std::cerr << "SDL window creation failed: " << SDL_GetError() << '\n';
		return 2;
	}

	SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_CORE);
	SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 3);
	SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 3);
	SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1);

	sdl_context.gl_context = SDL_GL_CreateContext(sdl_context.window);

	SDL_GL_SetSwapInterval(0);

	glewExperimental = GL_TRUE;
	glewInit();

	glViewport(0, 0, 1280, 720);

	return 0;
}

extern "C" LCG_DLLEXPORT void DestroyRenderer() {
	SDL_GL_DeleteContext(sdl_context.gl_context);
	SDL_DestroyWindow(sdl_context.window);
	SDL_Quit();
}
