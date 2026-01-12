
a = {'x': 5, 'y': 10}
b = {'z': 15, 'w': 20}
c = {'p': 25, 'q': 30}

merged = {}
for d in (a, b, c):
    merged.update(d)

merged['r'] = 35

for key in merged:
    merged[key] *= 2

if 'y' in merged:
    del merged['y']
    
total = 0
for value in merged.values():
    total += value
average = total / len(merged)

print("Final dictionary:", merged)
print("Average value:", average)