#pragma once

#if defined _MSC_VER
#define LCG_DLLEXPORT __declspec(dllexport)
#elif defined __GNUC__
#define LCG_DLLEXPORT
#endif
