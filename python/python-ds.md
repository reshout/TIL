# Python Data Structure

네 종류의 자료 구조

- 리스트
- 튜플
- 사전
- 집합

## 리스트

순서대로 정리된 항목을 저장

```python
>>> shoplist = ['apple', 'mango', 'carrot', 'banana']
>>> len(shoplist)
4
>>> for item in shoplist:
...     print item
...
apple
mango
carrot
banana
>>> shoplist.append('rice')
>>> shoplist
['apple', 'mango', 'carrot', 'banana', 'rice']
>>> shoplist.sort()
>>> shoplist
['apple', 'banana', 'carrot', 'mango', 'rice']
>>> olditem = shoplist[0]
>>> del shoplist[0]
>>> olditem
'apple'
>>> shoplist
['banana', 'carrot', 'mango', 'rice']
```

## 튜플

여러 개의 객체를 모아 담는데 사용. 리스트와 비슷하지만 수정이 불가능.

```python
>>> zoo = ('python', 'elephant', 'penguin')
>>> len(zoo)
3
>>> new_zoo = 'monkey', 'camel', zoo
>>> new_zoo
('monkey', 'camel', ('python', 'elephant', 'penguin'))
>>> new_zoo[2]
('python', 'elephant', 'penguin')
>>> new_zoo[2][2]
'penguin'
>>> myempty = ()
>>> singleton = (2, )
```

## 열거형(iterative)

열거형의 예: 리스트, 튜플, 문자열

열거형의 두 가지 기능

1. 멤버십 테스트 (`in` and `not in`)
1. 인덱싱, 슬라이스 연산

```python
shoplist = ['apple', 'mango', 'carrot', 'banana']
shoplist[1:3]
shoplist[2:]
shoplist[1:-1]
shoplist[:] # 복사할 때 사용
shoplist[::2]
```

슬라이스의 세 번째 인수는 스텝.
 
## 집합

정렬되지 않은 단순 객체의 묶음. 멤버십 테스트를 통해 부분집합, 교집합을 구할 수 있다.

```python
>>> bri = set(['brazil', 'russia', 'india'])
>>> 'india' in bri
True
>>> bric = bri.copy()
>>> bric.add('china')
>>> bric.issuperset(bri)
True
>>> bri.remove('russia')
>>> bri & bric # OR bri.intersection(bric)
set(['brazil', 'india'])
```

## 문자열

문자열은 `str` 클래스의 객체.

```python
>>> name = 'Swaroop'
>>> name.startswith('Swa')
True
>>> 'a' in name
True
>>> name.find('war')
1
>>> delimiter = '_*_'
>>> mylist = ['Brazil', 'Russia', 'India', 'China']
>>> delimiter.join(mylist)
'Brazil_*_Russia_*_India_*_China'
```

