# print(f.read())

# print(f.read(size))

f = open('workfile', 'w', encoding="utf-8")

with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

# f.close()
# f.read()

f.read(size)
print(f.read())