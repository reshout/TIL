# android10/Android-CleanArchitecture

https://github.com/android10/Android-CleanArchitecture

## Overview

- Cloud에서 사용자 목록을 가져와 보여주고, 사용자를 선택하면 상세 정보를 보여주는 샘플앱을 Clean Architecture로 구현
- Domain layer의 use case와 상호작용하는 인터페이스를 RxJava의 `Subscriber` 인터페이스를 활용해 구현
- Dependency Injection을 위해 Dagger 2를 사용

### Architectural approach

![](https://camo.githubusercontent.com/923f431518bb20003a401768449e59469995657c/687474703a2f2f6665726e616e646f63656a61732e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031342f30392f636c65616e5f6172636869746563747572655f616e64726f69642e706e67)

### Architectural reactive approach

![](https://camo.githubusercontent.com/0bf8c53baf9bf62f8c85b983d49cef4e23539188/687474703a2f2f6665726e616e646f63656a61732e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031352f30372f636c65616e5f6172636869746563747572655f65766f6c7574696f6e2e706e67)

## Gradle modules

Layer 별로 별도의 Gradle 모듈로 구성되어 있다.

- `/domain`
  - Java
  - 다른 모듈에 의존하지 않음
- `/data`
  - Android Library
  - domain 모듈에 의존
- `/presentation`
  - Android Application
  - domain, data 모듈에 의존

## Package organization

Package를 구성하는 방식에는 2가지가 있다.

- Package by Layer
- Package by Feature

Package by Feature 방식이 패키지 내에서 cohesion, modularity을 높이고, 패키지 간 coupling을 줄이기 때문에 효과적이다.

![](http://fernandocejas.com/wp-content/uploads/2015/07/package_organization-795x1024.png)

그러나 이 프로젝트는 처음에 Package by Layer로 구현되었고, clean architecture를 보여주는 것이 주 목적이므로 그대로 두었다.

## References

- [Architecting Android…The evolution](http://fernandocejas.com/2015/07/18/architecting-android-the-evolution/)
- [Clean Architecture on Android - Sample App](https://www.youtube.com/watch?v=XSjV4sG3ni0&feature=youtu.be)
