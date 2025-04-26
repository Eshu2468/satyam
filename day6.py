# #list methods


# a=[1,2,3,5,6]
# a.append(4)
# print(a)


# b=[1,2]
# b.extend([3,4])
# print(b)

# c = [1,2,4]
# c.insert(2,3)
# print(c)

# d = [1,2,3,2]
# d.remove(2)
# print(d)

# e = [1,2,3]
# e.pop(0)
# print(e)

# f = [1,2,3,4,5]
# f.clear()
# print(f)

# g = [1,2,3]
# print(g.index(2))


# h = [1,2,2,2,3,3,3]
# print(h.count(3))

# i = [3,2,1]
# i.sort()
# print(i)


# j = [1,2,3]
# j.reverse()
# print(j)

# k=[1,2,3,4,5]
# kk=k.copy()
# print(kk)

# l=[1,2,3]
# del l[2]
# print(l)

# print(list('abc'))

# print(set([1,2,2,2,3,4,4,5,5,6,6,77,8]))

# squares = [x**2 for x in range(3)]
# print(squares)

# lst = ['a', 'b']
# for i, v in enumerate(lst): print(i, v)

# print(list(zip([1, 2], ['a', 'b'])))
# # Output: [(1, 'a'), (2, 'b')]

# print(any([0, 1]))

# print(all([1, 2, 3]))


# print(max([1, 2, 3]))
# print(min([1, 2, 3]))
# print(sum([1, 2, 3]))



d = {'a':1}
print(d.get('b','default'))

e = {'a':1,'b':2}
print(e.keys())

print(e.values())
print(e.items())
e.update({'b':3})

e.clear()
# e.popitem()

f =  {'a':1,'b':2}
f.fromkeys(['a','b'],0)
print(f)