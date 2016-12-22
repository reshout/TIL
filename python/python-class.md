# Python Class

**정수형 조차 `int` 클래스의 객체**

- 클래스는 새로운 형식을 정의
- 객체는 클래스의 인스턴스

클래스의 구성은 아래와 같다.

- **필드**
    - 인스턴스 변수
    - 클래스 변수: 클래스로부터 생성된 모든 인스턴스간에 공유
- **메서드** 
- **속성**: 필드 + 메서드

모든 클래스 멤버는 외부에 공개. 숨기고 싶다면 앞에 `__`를 붙이면 된다. 예. ``__privatevar``

클래스 메서드는 항상 첫 번째 매개변수로 객체 자신에 대한 참조가 할당된 `self`를 가진다. 메서드를 호출할 때 우리는 생략하지만 파이썬이 자동으로 값을 할당한다.

`MyClass` 클래스의 `myobject` 객체를 생성했을 때, `myobject.method1(arg1, arg2)`는 파이썬에 의해 자동으로 `MyClass.method1(myobject, arg1, arg2)`로 바뀐다.

```python
class Robot:
    population = 0 # A class variable

    def __init__(self, name):
        self.name = name
        print "(Initializing {})".format(self.name)
        Robot.population += 1

    def die(self):
        Robot.population -= 1
        if Robot.population == 0:
            print "{} was the last one".format(self.name)
        else:
            print "There are still {:d} robots working".format(Robot.population)

    def say_hi(self):
        print self.name

    @classmethod
    def how_many(cls):
        print "We have {:d} robots".format(cls.population)
```

```python
class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def tell(self):
        print 'name={}, age={}'.format(self.name, self.age)

class Teacher(SchoolMember):
    def __init__(self, name, age, sallery):
        SchoolMember.__init__(self, name, age)
        self.sallery = sallery
    def tell(self):
        SchoolMember.tell(self)
        print 'sallery={}'.format(self.sallery)

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
    def tell(self):
        SchoolMember.tell(self)
        print 'marks={}'.format(self.marks)

t = Teacher('Mrs. Kim', 50, 100000)
s = Student('Miss Choi', 17, 75)

members = [t, s]
for member in members:
    member.tell()
```

