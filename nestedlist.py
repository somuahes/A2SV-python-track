if __name__ == '__main__':
    student=[]
    for _ in range(int(input())):
        name=input()
        grade=float(input())
        student.append([name,grade])
        
    set_grades=set(grade for name,grade in student)
    sort_grades=sorted(set_grades)
    second_lowest=sort_grades[1]
    names=sorted([name for name,grade in student if grade==second_lowest])
    
    for i in names:
        print(i)
   