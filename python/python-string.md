# Python String

## upper, lower

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
