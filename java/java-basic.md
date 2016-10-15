# Java Basic

## Object

https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html

- `boolean equals(Object obj)`
- `int hashCode()`
- `void notify()`
- `void wait()`

## Array

```java
int[] a = new int[10];
int[] b = new int[] { 1, 2, 3, 4, 5 };
for (int i = 0; i < a.length; i++) {
    System.out.println(a[i]);
}
```

```java
int[][] table = new int[5][10];
// table.length is 5
// table[0].length is 10
```

```java
int[][] table = { {1,2,3,4,5,6,7,8,9,10},
                  {2,3,4,5,6,7,8,9,10,1},
                  {3,4,5,6,7,8,9,10,1,2},
                  {4,5,6,7,8,9,10,1,2,3},
                  {5,6,7,8,9,10,1,2,3,4} };
```
