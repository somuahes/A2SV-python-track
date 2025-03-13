
if __name__ == '__main__':
    N=int(input())
    listt=[]
    for _ in range (N):
        command=input().split()
        if command[0]=="insert":
            listt.insert(int(command[1]),int(command[2]))
        elif command[0]=="print":
            print(listt)
        elif command[0]=="remove":
            listt.remove(int(command[1]))
        elif command[0]=="append":
            listt.append(int(command[1]))
        elif command[0]=="sort":
            listt.sort()
        elif command[0]=="pop":
            listt.pop()
        elif command[0]=="reverse":
            listt.reverse()  
