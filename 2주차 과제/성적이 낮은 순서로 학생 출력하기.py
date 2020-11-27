db=dict()
for _ in range(int(input())):
    name,grade = input().split()
    db[name]=int(grade)
for key,val in sorted(db.items(), key=lambda x: x[1]):
    print("{key}".format(key=key),end=" ")