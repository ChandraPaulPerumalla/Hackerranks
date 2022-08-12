'''If we want to add a single element to an existing set, we can use the .add() operation.
It adds the element to the set and returns 'None'.'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set1 =set()
for i in range(n):
    set1.add(input())
print(len(set1))
