# Android Architecture Blueprints

https://github.com/googlesamples/android-architecture

- 안드로이드 프레임워크는 자유도가 높기 때문에 잘못된 아키텍처를 설계하기 쉽다.
- [The TODO app](https://github.com/googlesamples/android-architecture/wiki/To-do-app-specification)을 여러가지 다른 아키텍처로 구현한 예를 제시한다.
  - MVP
  - MVP + Loaders
  - MVP + DataBinding
  - MVP + Clean Architecture
  - MVP + Dagger2
  - MVP + ContentProviders
- [Samples at a glance](https://github.com/googlesamples/android-architecture/wiki/Samples-at-a-glance)

## MVP

https://github.com/googlesamples/android-architecture/tree/todo-mvp/

![](https://github.com/googlesamples/android-architecture/wiki/images/mvp.png)

- Model-View-Presenter pattern with no architectural frameworks
- 안드로이드의 Fragment를 MVP의 View로 활용
- App은 4개의 feature(Tasks, TaskDetail, AddEditTask, Statistics)로 구성
- 각 feature는 4개의 module로 구성
  - Contract: view와 presenter의 connection 정의
  - Activity: views, presenters 생성
  - Fragment: view interface 구현 (no business logic)
  - Presenter: presenter interface 구현 (business logic)
- Presenter의 생성자에 Fragment 인스턴스 전달. Presenter의 생성자에서 `View.setPresenter(this)` 호출
- Fragment.onResume에서 `Presenter.start()` 호출
- Fragment는 이벤트 발생하면 Presenter의 메서드 호출. Presenter의 메서드는 business logic 수행 후 Fragment 메서드 호출.
- 다른 화면으로 이동하는 경우 Fragment에서 `startActivty()` 호출

## MVP + Loaders

## MVP + DataBinding

## MVP + Clean Architecture

## MVP + Dagger2

## MVP + ContentProviders
