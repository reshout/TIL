# Exploring RxJava 2 for Android by Jake Wharton

https://speakerdeck.com/jakewharton/exploring-rxjava-2-for-android-gotocph-october-2016

## Why Reactive?

- **전체 시스템을 동기화된 커뮤니케이션으로만 모델링 하는 것은 불가능하다!**
- 안드로이드에서 비동기 프로그래밍할 때 문제점
  - 비동기 메서드를 순차적으로 호출하도록 구현하면 callback hell 발생
  - 리스너 객체를 호출하는 쓰레드는 메인 쓰레드가 아닐 수 있으므로 runOnUiThread 사용해야 함
  - 리스너가 호출된 시점에 Activity가 유효하지 않을 수 있으므로 `isDestroy`로 확인해야 함

## RxJava

- A set of classes for **representing sources of data**
- A set of classes for **listening to data sources**
- A set of methods for modifying and composing the data.

### Sources

- **Usually do work when you start or stop listening**
- **Just an implementation of the Observer pattern**
- Sync or async
- Single item, many items or empty
- Terminates with an error or succeeds to completion
- May never terminate
