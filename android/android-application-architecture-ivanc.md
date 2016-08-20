# Android Application Architecture by Iván Carballo

https://labs.ribot.co.uk/android-application-architecture-8b6e34acda65#.rskyigleg

> Our journey from standard Activities and AsyncTasks to a modern MVP-based architecture powered by RxJava.

ribot team과 지난 3년 동안 안드로이드 앱을 개발하면서 사용한 architecture와 technologies는 계속 진화했다. 이 글은 architectural changes와 관련된 배움과 실수와 고민을 다룬다.

## The old times

- 2012년에는 basic structure를 사용했다.
- Network library를 사용하지 않았고, AsyncTasks를 사용했다.
- 아래 그림은 당시의 architecture를 나타낸다.

![](https://cdn-images-1.medium.com/max/800/1*TTtpcT4H80THBofnCtQ_Lw.png)

- `APIProvider`
  - REST API 통신 메서드 제공
  - `URLConnection` 및 `AsyncTasks` 사용
  - 결과는 callback을 통해 Activity로 전달
- `CacheProvider`
  - SharedPreferences와 SQLite database에 데이터 조회/저장 메서드 제공
  - 결과는 callback을 통해 Activity로 전달

### The problems

### Summary

## A new architecture driven by RxJava

## Integrating Model View Presenter
