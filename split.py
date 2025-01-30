
def split_and_join(line):
    spli=line.split(" ")
    line="-".join(spli)
    return line
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)