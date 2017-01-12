import os
import platform
import ctypes

gfx_lib = 0
if (platform.system() == "Linux"):
	gfx_lib = ctypes.CDLL(os.path.join(os.getcwd(), "libgfx.so"))
elif (platform.system() == "Windows"):
	gfx_lib = ctypes.CDLL(os.path.join(os.getcwd(), "libgfx.dll"))

def helloWorld():
	gfx_lib.HelloWorld()

def setupRenderer():
	gfx_lib.SetupRenderer()

def distroyRenderer():
	gfx_lib.DistroyRenderer();
