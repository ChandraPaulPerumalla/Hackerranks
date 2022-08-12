Given the names and grades for each '''student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.'''

if __name__ == '__main__':
    dic={}
    s=list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in dic:
            dic[score].append(name)
        else:
            dic[score]=[name]
        if score not in s:
            s.append(score)
            
    m=min(s)
    s.remove(m)
    m1=min(s)
    dic[m1].sort()
    for i in dic[m1]:
        print(i)
