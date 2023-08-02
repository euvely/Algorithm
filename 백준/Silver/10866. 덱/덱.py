from sys import stdin
from collections import deque
N = int(stdin.readline())
myDeque = deque()

for i in range(1,N+1):
    A = stdin.readline().split()
    if A[0] == "push_front": myDeque.appendleft(int(A[1]))
    elif A[0] == "push_back": myDeque.append(int(A[1]))
    elif A[0] == "pop_front":
        if len(myDeque) != 0: print(myDeque.popleft())
        else: print(-1)
    elif A[0] == "pop_back":
        if len(myDeque) != 0: print(myDeque.pop())
        else: print(-1)
    elif A[0] == "size": print(len(myDeque))
    elif A[0] == "empty":
        if len(myDeque) != 0: print(0)
        else: print(1)
    elif A[0] == "front":
        if len(myDeque) != 0: print(myDeque[0])
        else: print(-1)    
    elif A[0] == "back":
        if len(myDeque) != 0: print(myDeque[-1])
        else: print(-1)