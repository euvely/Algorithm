from sys import stdin
n = int(stdin.readline())
Que = []
for i in range(1, n + 1):
    A = stdin.readline().split()

    if A[0] == "push":
        Que.append(A[1])
    
    if A[0] == "pop":
        if len(Que) != 0:
            print(Que.pop(0))
        else:
            print(-1)
            
    if A[0] == "size":
        print(len(Que))
        
    if A[0] == "empty":
        if len(Que) != 0:
            print(0)
        else:
            print(1)
            
    if A[0] == "front":
        if len(Que) != 0:
            print(Que[0])
        else:
            print(-1)
    
    if A[0] == "back":
        if len(Que) != 0:
            print(Que[-1])
        else:
            print(-1)
