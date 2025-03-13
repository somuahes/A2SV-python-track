if __name__ == '__main__':
    n=int(input())
    arr=map(int,input().split())
    scores=set(arr)
    sort_scores=sorted(scores)
    runner_up=sort_scores[-2]
    print(runner_up)
    
