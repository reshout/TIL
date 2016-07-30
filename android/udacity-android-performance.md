# Udacity - Android Performance

https://www.udacity.com/course/android-performance--ud825

## Lesson 1: Render

### Overdraw를 줄이자

- 다른 화면에 가려서 보이지 않는 영역을 그리는 일이 없도록
- 불필요하게 같은 영역을 여러번 그리는 일이 없도록
- 불필요한 배경을 그리는 일이 없도록
- Custom View를 작성하는 경우 [clipRect()](https://goo.gl/eSebwI) 메서드를 활용해 화면에 그려질 필요가 있는 영역을 표시
- Tool: Settings > Developer options > Debug GPU overdraw

### 중첩 Layout을 피하자

- 그려질 내용이 바뀔 때마다 DisplayList를 다시 생성하고 실행해 화면에 그려야 한다.
- 계층 구조가 깊고 복잡할 수록 측정-레이아웃 단계에서 성능 문제 발생
- 레이아웃을 단순하고 평면적으로 구성할 수록 렌더링 성능에 유리함
- LinearLayout 보다 RelativeLayout을 활용하기
- Tool: Hierarchy Viewer를 통해 뷰의 계층 구조를 파악하고 각 노드의 상대적 렌더링 성능 확인할 수 있음

## Lesson 2A: Compute

### 성능 문제 2종류

1. 느린 함수
1. 느린 코드가 여기저기 흩어져 있는 경우 → Trace View로 profiling

### Batching and Caching

모든 성능 향상 방법은 사실상 batching과 caching을 변경한 것 뿐  

#### Batching

- 실행할 때마다 걸리는 오버헤드 줄이기
- 데이터를 준비하는 단계에서 수행
- `Set.contains()`: 한 번만 정렬하고 그 결과를 저장한 후 원소 찾기

#### Caching

- 여러 번 반복하는 계산의 결과값이 매번 같을 때 저장 후 참조

### Blocking the UI Thread

- 함수의 성능만큼 함수가 어디서 실행되는지도 중요
- UI callback이 16ms안에 return하지 못하면 렌더링 프레임을 놓쳐 렉 발생
- UI thread의 렌더링 작업이 5초 이상 이상 멈추면 ANR 발생
- **그림을 그리는데 필수적이지 않은 작업은 독립적인 쓰레드로 옮기기**

### Container Performance

## Lesson 2B: Memory

## Lesson 3: Battery
