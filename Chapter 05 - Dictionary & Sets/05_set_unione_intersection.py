s1={44,33}
s2={36,44,33,77}

print(s1.union(s2))
print(s1.intersection(s2))

print(s1.issubset(s2)) #all the elements of s1 are in s2
print(s2.issuperset(s1)) #all the elements of s2 are in s1