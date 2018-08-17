import ctypes
import time
dll = ctypes.cdll.LoadLibrary
lib = dll("./libcppcall.so")
t = time.time()
lib.read()
print time.time()- t