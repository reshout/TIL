# Python Basic

Python 3을 기준으로 문법, 자료구조, 함수를 정리한다.

### STDIN I/O and If-Else

```python
n = int(input().strip())
if n == 123:
  print('correct')
elif n < 0:
  print('negative')
else:
  print('incorrect')
```

### Arithmetic Operators

```python
>>> a = 5
>>> b = 3
>>> a / b
1.6666666666666667
>>> a // b
1
>>> a % b
2
```

### Loops

```python
n = int(input().strip())
for i in range(0, n): # 0, 1, 2, 3, 4
  print(pow(i, 2)) # 0, 1, 4, 9, 16
```

### Function

```python
def is_leap(year):
    leap = False

    if year % 4 == 0:
      leap = True
      if year % 100 == 0:
        leap = False
        if year % 400 == 0:
          leap = True

    return leap
```

### Map and Lambda Function

```python
print(*list(map(lambda x: x, range(1, int(input().strip()) + 1))), sep='')
```

```python
N = int(input())
fib = lambda n: n if n < 2 else fib(n - 1) + fib(n - 2)
print(list(map(lambda n: n ** 3, map(fib, range(N)))))
```

### Lists

```python
>>> l = []
>>> l.insert(0, 1)
>>> l.append(2)
>>> l.append(3)
>>> l
[1, 2, 3]
>>> len(l)
3
>>> l.remove(2)
>>> l.reverse() # l.sort()
>>> l
[3, 1]
>>> l.pop()
1
```

#### List Comprehensions

```python
>>> x = 1
>>> y = 1
>>> z = 1
>>> n = 2
>>> [[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if a + b + c != n]
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```

### Tuples

```python
>>> t = tuple([1, 1, 2, 2, 3, 3]) # tuple(iterable)
>>> t
(1, 1, 2, 2, 3, 3)
>>> t.count(2)
2
>>> t.index(1)
0
>>> t.index(2)
2
```

### Dictionary

```python
>>> d = {} # dict()
>>> d['key1'] = 'val1'
>>> d
{'key1': 'val1'}
>>> if 'key1' in d:
...   print(d['key1'])
...
val1
>>> del d['key1']
>>> d
{}
```
