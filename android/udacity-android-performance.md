# Udacity - Android Performance

https://www.udacity.com/course/android-performance--ud825

## Lesson 1: Render

### Overdraw를 줄이자
- 불필요하게 화면에 보이지 않는 영역을 중복해서 그리는 일이 없도록
- 테마에 의해 그려지는 배경
- 중복하여 그려지는 배경색
- 불필요하게 두 번 그려지는 영역
- Custom View를 작성하는 경우 [clipRect()](https://goo.gl/eSebwI) 메서드를 활용해 화면에 그려질 필요가 있는 영역을 표시
- Settings > Developer options > Debug GPU overdraw

### 중첩 Layout을 피하자

- 그려질 내용이 바뀔 때마다 DisplayList를 다시 생성하고 실행해 화면에 그려야 한다.
- 계층 구조가 깊고 복잡할 수록 측정-레이아웃 단계에서 성능 문제 발생
- Hierarchy Viewer를 통해 뷰의 계층 구조를 파악하고 각 노드의 상대적 렌더링 성능 확인할 수 있음
- 레이아웃을 단순하고 평면적으로 구성할 수록 렌더링 성능에 유리함
- LinearLayout 보다 RelativeLayout을 활용하기

## Lesson 2A: Compute

## Lesson 2B: Memory

## Lesson 3: Battery
