# Python String

https://docs.python.org/3.4/library/string.html

## upper, isupper()

```python
>>> 's'.islower()
True
>>> 's'.upper()
'S'
```

## split, join

```python
>>> tokens = 'this is a string'.split(sep=' ')
>>> tokens
['this', 'is', 'a', 'string']
>>> '-'.join(tokens)
'this-is-a-string'
```

## format

```python
>>> first_name = 'Gunwoo'
>>> second_name = 'Kim'
>>> 'Hello %s %s! You just delved into python.' % (first_name, second_name)
'Hello Gunwoo Kim! You just delved into python.'
>>> 'Hello {0} {1}! You just delved into python.'.format(first_name, second_name)
'Hello Gunwoo Kim! You just delved into python.'
```

```python
>>> '{:02d}'.format(1)
'01'
>>> '{:.5f}'.format(1/3)
'0.33333'
```

## slice

```python
>>> s = 'abcdefg'
>>> s[3:]
'defg'
>>> s[:3]
'abc'
>>> s[-1]
'g'
>>> s[:-1]
'abcdef'
```
