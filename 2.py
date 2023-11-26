from collections import deque

def names_list():
    names=deque(['John','Oscar','Faith'])
    names.append('Eric')
    names.append('David')
    names.pop()
    names.popleft()
    return names

print(names_list())