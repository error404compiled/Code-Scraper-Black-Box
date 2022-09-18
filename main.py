# cook your dish here
import os
import sys
import time
from collections import *
from itertools import *
from math import *
from queue import *
from heapq import *
from bisect import *
from io import BytesIO, IOBase

BUFSIZE = 8192
sys.setrecursionlimit(10**6)



class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
# input = lambda: sys.stdin.readline().rstrip("\r\n")
input_int = lambda: int(sys.stdin.readline().rstrip("\r\n"))
input_ints = lambda: map(int, sys.stdin.readline().rstrip("\r\n").split()) 
input_str = lambda: sys.stdin.readline().rstrip("\r\n")
input_strs = lambda: map(str, sys.stdin.readline().rstrip("\r\n").split())
input_arri = lambda: [int(_) for _ in sys.stdin.readline().rstrip("\r\n").split()]
input_arrs = lambda: [str(_) for _ in sys.stdin.readline().rstrip("\r\n").split()]

# from link import link_search
# from headers import head
# from content import link

# import requests, lxml
# from bs4 import BeautifulSoup
# import re
# import pandas as pd 

from content import code

def lang(n):
    if n=='c' or n=='C':
        return 0
    elif n=='c++' or n=="C++" or n=='CPP' or n=='cpp':
        return 1
    elif n=='JAVA' or n=='java':
        return 2
    elif n=='python' or n=="PYTHON" or n=='py':
        return 3
    else:
        return 0

def solve():
    arr = list(map(str, input("Enter the problem and langauage comma seprated : ").split(",")))
    k = 'geeksforgeeks '+ arr[0]
    l = lang((arr[1]).strip()) 
    url = code(k, l)
    if url:
        print(url)


def main():
    orig_stdin = sys.stdin
    orig_stdout = sys.stdout
    f1 = open("in.txt", 'r')
    f2 = open("out.txt", 'w') 
    sys.stdin = f1
    sys.stdout = f2
    start_time = time.time()
    
    t = 1
    # t = int(input())
    for _ in range(t):
        # print("CASE#"str(_ + 1) + ": ", end="")
        solve()
        end_time = time.time()
        # print(f"time : {(end_time-start_time)}")
        print()
    k = time.time()

    print(f"total time taken : {k-start_time}")

    sys.stdin = orig_stdin
    sys.stdout = orig_stdout
    f1.close()
    f2.close()


if __name__ == "__main__":
    main()