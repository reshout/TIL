# Python Exception Handling

## 예외 처리

```python
try:
    text = raw_input('Enter something --> ')
except EOFError:
    print 'Why did you do an EOF on me?'
except KeyboardInterrupt:
    print 'You cancelled the operation.'
else:
    print 'You entered {}'.format(text)
```

- `except` 뒤에 0개, 1개, N개의 오류, 예외 나열 가능
- `except`에 의해 처리 되지 않은 오류나 예외가 발생한 경우 기본 파이썬 오류 핸들러 호출되어 프로그램 수행이 중단된다.
- `else` 절은 어떤 예외도 발생하지 않은 경우 호출된다.

## 예외 발생시키기

```python
class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = raw_input('Enter something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print 'Why did you do an EOF on me?'
except ShortInputException as ex:
    print ('ShortInputException: The input was ' + \
           '{0} long, excepted at least {1}')\
           .format(ex.length, ex.atleast)
else:
    print 'No exception was raised.'
```

- `raise`로 발생시킬 수 있는 오류나 예외는 `Exception` 클래스를 상속해야 한다.

## Try ... Finally

```python
import sys
import time

f = None
try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line,
        sys.stdout.flush()
        print 'Press ctrl+c now'
        time.sleep(2)
except IOError:
    print 'Could not find file poem.txt'
except KeyboardInterrupt:
    print '!! You cancelled the reading from the file.'
finally:
    if f:
        f.close()
    print '(Cleaning up: Closed the file)'
```

- 예외 발생 여부와 상관없이 `finally` 블럭은 실행된다.

## with

```python
with open('poem.txt') as f:
	for line in f:
		print line,
```

- `with`를 사용하면 `finally`를 사용해 자원을 해제하는 코드를 생략 가능하다.
- `with`는 시작과 끝에 전달된 객체의 `__enter__`, `__exit__` 함수가 호출된다.
