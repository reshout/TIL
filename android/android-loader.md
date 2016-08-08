# Android Loader

## State Machine

![Loaders State Machine](http://i.stack.imgur.com/7tGUY.png)

## Google's Overview

로더는 Android 3.0부터 도입된 것으로, 액티비티 또는 프래그먼트에서 비동기식으로 데이터를 쉽게 로딩할 수 있게 합니다. 로더의 특성은 다음과 같습니다.

  - 모든 Activity와 Fragment에 사용할 수 있습니다.
  - 데이터의 비동기식 로딩을 제공합니다.
  - 데이터의 출처를 모니터링하여 그 콘텐츠가 변경되면 새 결과를 전달합니다.
  - 구성 변경 후에 재생성된 경우, 마지막 로더의 커서로 자동으로 다시 연결됩니다. 따라서 데이터를 다시 쿼리하지 않아도 됩니다.

## My Overview

- 데이터베이스 또는 네트워크에서 데이터를 비동기로 가져오는 과정을 제대로 구현하기 어렵기 때문에 구글에서 프레임워크 제공
- 비동기로 데이터를 가져오는 작업을 위한 쓰레드 관리, 결과는 Main Thread로 전달
- 데이터 변경사항을 모니터링하여 변경된 데이터 전달 및 로딩 중 취소 operation 지원
- Activity, Fragment의 lifecycle에 따라 데이터 동기화

## Basic Flow

![](images/mvp-loaders.png)

## API Details

-  


## Reference

- https://developer.android.com/guide/components/loaders.html
