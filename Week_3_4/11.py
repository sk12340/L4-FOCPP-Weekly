setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

union_set = setA.union(setB)
print("Union:", union_set)
print("Union size:", len(union_set))

diff = setA - setB
print("Difference (A - B):", diff)

inter = setA.intersection(setB)
print("Intersection:", inter)

print("Is A subset of B?", setA.issubset(setB))

setB.discard(7)
print("B after removing 7:", setB)