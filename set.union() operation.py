'''The .union() operator returns the union of a set and the set of elements in an iterable.
Sometimes, the | operator is used in place of .union() operator, but it operates only on the set of elements in set.
Set is immutable to the .union() operation (or | operation).
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
n =int(input())
n1=set(map(int,input().split()))
m=int(input())
m1=set(map(int,input().split()))
ans=n1.union(m1)
count=0
for i in ans:
    count = count+1
print(count)
    
