# Iteration patterns: enumerate and zip
words = ['red', 'green', 'blue']
for i, w in enumerate(words, start=1):
    print(i, w)

list1 = [10,20,30]
list2 = ['a','b','c']
for num, ch in zip(list1, list2):
    print(num, ch)
