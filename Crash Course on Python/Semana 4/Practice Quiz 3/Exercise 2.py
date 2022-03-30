def groups_per_user(groups):
    l = {}
    s = []
    v = [x for x in groups]
    for x in v:
        s.extend(groups[x])
    s = set(s)
    s = list(s)
    for i in s:
        for d in groups:
            if i in groups[d]:
                l[i] = l.get(i, []) + [d]
    return l

    

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))


def groups_per_user(groups):
    lst = []
    dit = {}
    for kind,user in groups.items():
        lst.extend(user)
    lst = set(lst)   # should be  list(set(lst))
    lst = list(lst)

    for i in lst:
        for x in groups:
            if i in groups[x]:
                dit[i] = dit.get(i,[]) + [x]

    return dit