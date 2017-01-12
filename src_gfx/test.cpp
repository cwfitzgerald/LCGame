#include "util/dllexport.hpp"

#include <iostream>

extern "C" LCG_DLLEXPORT void HelloWorld() {
	std::cout << "Hello World!\n";
}
