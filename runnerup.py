if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    score=list(arr)
    winner=max(score)
    while winner in score:
        score.remove(winner)
    runner_up=max(score)
    print(runner_up)
    