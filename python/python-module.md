# Python Module

## 모듈 사용하기

`import`가 모듈을 찾는 순서

1. 내장 모듈
1. `sys.path`에 정의된 디렉토리에서 해당 모듈이 있는지 검색

**모듈을 첫번째로 불러들였을 때, 모듈 내부 코드가 실행된다.**

```python
import sys

for i in sys.argv:
    print i

print sys.path
```

## from ... import

매번 `sys.`을 입력하지 않으려면 `from sys import argv` 같은 구문 사용 가능

```python
from math import sqrt
print "Square root of 16 is", sqrt(16)
```

이름 충돌을 피하고 프로그램을 좀 더 읽기 쉽게 작성하는 관점에서는 가능하면 `import` 사용을 권장

## 모듈의 name 속성

모든 모듈은 `__name__` 속성을 가지며, 이를 참조하여 모듈이 `import` 되었는지 여부를 확인 가능

```python
if __name__ == '__main__':
    print 'This program is being run by itself'
else:
    print 'I am being imported from another module'
    print '__name__ is', __name__
```

## 새로운 모듈 작성하기

모든 파이썬 프로그램은 곧 모듈. `.py` 확장자 파일에 코드를 저장하면 그것이 모듈.

```python
# mymodule.py
def say_hi():
    print 'Hi, this is mymodule speaking.'

__version__ = '0.1'
```

```python
# mymodule_demo.py
import mymodule

mymodule.say_hi()
print 'Version', mymodule.__version__
```

`from mymodule import *`의 경우 모든 공개된 이름을 불러온다. `__`로 시작하는 이름은 불러오지 않는다.

## dir 내장 함수

```
>>> dir(sys)
```

현재 모듈에 선언된 속성들의 이름 목록

```
>>> a = 5
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'a']
>>> del a
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
```

## 패키지

모듈은 패키지에 포함됨. 파이썬 패키지는 단순한 폴더지만 이 폴더가 파이썬 모듈을 담고 있다는 것을 알려주는 역할을 하는 `init.py`를 포함. 패키지는 계층적으로 모듈을 관리할 수 있게 편의상 구성하는 것.

아래와 같이 패키지가 구성되어 있을 때,

```
game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py
```

```python
# echo.py
def echo_test():
    print ("echo")
```

```python
# render.py
def render_test():
    print ("render")
```

`echo_test()`를 호출하는 다양한 방법

```python
>>> import game.sound.echo
>>> game.sound.echo.echo_test()
echo
```

```python
>>> from game.sound import echo
>>> echo.echo_test()
echo
```

```python
>>> from game.sound.echo import echo_test
>>> echo_test()
echo
```

**도트 연산자(`.`)를 사용해서 `import a.b.c`처럼 `import`할 때 가장 마지막 항목인 `c`는 반드시 모듈 또는 패키지여야만 한다.**

## References

- [점프 투 파이썬 - 패키지](https://wikidocs.net/1418)
