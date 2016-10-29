# Java Data Structure

## Vector vs ArrayList vs LinkedList

어떤 연산이 자주 일어나느냐에 따라 ArrayList 또는 LinkedList 사용하기.

- Vector: 동기화 처리. Java 1.0에서 나온것으로 버전 하위 호환성을 위해 존재함.
- ArrayList: 인덱스 접근이 빠름. 추가/삭제 느림.
- LinkedList: 인덱스 접근 느림. 추가/삭제 빠름

ArrayList와 LinkedList에서 동기화 처리가 필요하다면 Collection.synchronizedList 사용.

## References

- [Java 의 Vector 와 ArrayList , Linked List 의 차이점](http://seeit.kr/36)
