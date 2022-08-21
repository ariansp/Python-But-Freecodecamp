set1 = {"orange", "banana", "apple", "citrus"}
set2 = {"mango", "cherry", "banana"}
set3 = {"orange"}

interception = set1 & set2
print(interception)
union = set1 | set2
print(union)
minus = set1 - set2
print(minus)
minus2 = set2 - set1
print(minus2)
mod = set1 > set3
print(mod)
print(tuple(set1))