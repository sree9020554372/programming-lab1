d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
print('d1 is',d1)
print('d2 is',d2)
print("merged one is:")
d=d1.copy()
d.update(d2)
print(d)