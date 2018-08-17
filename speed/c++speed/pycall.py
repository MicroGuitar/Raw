import ctypes
a = ctypes.cdll.LoadLibrary
lib = a("./libpycall.so")
lib.main()