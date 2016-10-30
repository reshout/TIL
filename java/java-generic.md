# Java Generic

## Wilcards

특별한 의미가 있는 것은 아니다. 단순히 코드 내에서 제네릭 타입 T를 다시 참조할 필요가 없을 때, ?로 대신하는 것이다.

아래 2가지 버전의 코드는 의미상 같다.

```java
<T extends Vehicle> int totalFuel(List<T> list) { ... }
```

```java
int totalFuel(List<? extends Vehicle> list) { ... }
```

## extends vs super

```java
public class GenericTest {
    public static void main(String[] args) {
        List<? extends Fruit> fruitExtendedList = new ArrayList<>();

        Fruit fruit = fruitExtendedList.get(0);
        Melon melon = fruitExtendedList.get(0); // compile error
        WaterMelon waterMelon = fruitExtendedList.get(0); // compile error

        fruitExtendedList.add(new Fruit()); // compile error
        fruitExtendedList.add(new Melon()); // compile error
        fruitExtendedList.add(new WaterMelon()); // compile error

        List<? super Melon> melonSuperList = new ArrayList<>();

        Fruit fruit = melonSuperList.get(0); // compile error
        Object myObject = melonSuperList.get(0);

        melonSuperList.add(new Object()); // compile error
        melonSuperList.add(new Fruit()); // compile error
        melonSuperList.add(new Melon());
        melonSuperList.add(new WaterMelon());
    }
}

class Fruit {}
class Melon extends Fruit {}
class WaterMelon extends Melon {}
```

## References

- [Java Generics: extends, super and wildcards explained](http://onewebsql.com/blog/generics-extends-super)
