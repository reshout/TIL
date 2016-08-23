# Effective Java

## Item 12 Comparable 인터페이스의 구현을 고려하자

### 개요

[Comparable](https://docs.oracle.com/javase/8/docs/api/java/lang/Comparable.html)를 구현한다는 것은 자신의 인스턴스가 natural order를 따른다는 것을 의미

`compareTo(T o)`는 `Comparable` 인터페이스에 존재하는 유일한 메서드

`Comparable` 구현 객체의 배열은 아래와 같이 간단히 정렬 가능

```java
Arrays.sort(a);
```

자바 라이브러리의 모든 값 클래스는 `Comparable` 인터페이스를 구현

자바의 수많은 알고리즘 및 컬렉션 클래스들이 `Comparable` 인터페이스에 의존하므로 natural order를 갖는 클래스를 작성한다면 반드시 `Comparable` 인터페이스를 구현해야 한다.

### `compareTo(T o)` 메서드 구현할 때 지켜야 할 조항

- `this`와 `o`를 비교하여 `this`가 `o` 보다 작으면 음수 정수 값을, 같으면 0을, 크면 양의 정수 값을 반환
- `o`의 타입이 비교할 수 없는 타입이면 `ClassCastException` 예외 발생


모든 x, y에 대하여 다음 조항을 만족해야 한다.

> sgn(expr)는 expr이 음수면 -1, 0이면 0, 양수면 1을 반환

```
sgn(x.compareTo(y)) == -sgn(y.compareTo(x))
```

```
x.compareTo(y) > 0 && y.compareTo(z) > 0 이면, x.compareTo(z) > 0
```

```
x.compareTo(y) == 0 이면, 모든 z에 대해 sgn(x.compareTo(z)) == sgn(y.comareTo(z))
```

`compareTo` 메서드에서 동일 여부 검사할 때 `equals` 계약 조항(재귀성, 대칭성, 이행성)과 같은 제약을 따라야 한다. 따라서 인스턴스 생성 가능 클래스로부터 상속받아 새로운 값 컴포넌트를 추가한 서브 클래스가 `compareTo` 계약을 지키도록 만들 수 없다. (c.f. Item 8)

반드시 요구되는 것은 아니지만 다음 조항을 만족하는 것이 좋다.

```
(x.compareTo(y) == 0) == (x.equals(y))
```

- 일반적인 컬렉션(e.g. `Collection`, `Set`, `Map`)의 보편적 계약은 `equals` 메서드 관점
- 정렬 컬렉션(e.g. `TreeSet`, `TreeMap`)의 보편적 계약은 `compareTo` 메서드 관점

### `compareTo` 구현 방법

```java
public final class CaseInsensitiveString implements Comparable<CaseInsensitiveString> {
  public int compareTo(CaseInsensitiveString cis) {
    return String.CASE_INSENSITIVE_ORDER.compare(s, cis.s);
  }
  ...
}
```

- 객체 참조 필드는 `compareTo` 메서드 호출하여 비교
- 객체 참조 필드가 `Comparable` 인터페이스를 구현하고 있지 않거나 natural order를 따르지 않는 경우,  [Comparator](https://docs.oracle.com/javase/8/docs/api/java/util/Comparator.html) 인터페이스를 새로 구현하거나 이미 구현된 것을 사용
- 정수 타입의 기본형 필드는 관계 연산자 `<`와 `>`을 사용하자.
- 부동 소수점 필드는 관계 연산자 대신 `Double.compare`나 `Float.compare`를 사용
- 비교할 필수 필드가 여러 개인 경우 비교 순서가 중요. 우선되는 필드부터 시작해서 차례대로 비교.
