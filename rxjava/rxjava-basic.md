# RxJava Basic

![](http://creately.com/jupiter/diagram/image/i4gy7ea02)

## Creating Observables

* [**`just( )`**](http://reactivex.io/documentation/operators/just.html) — convert an object or several objects into an Observable that emits that object or those objects
* [**`from( )`**](http://reactivex.io/documentation/operators/from.html) — convert an Iterable, a Future, or an Array into an Observable
* [**`create( )`**](http://reactivex.io/documentation/operators/create.html) — **advanced use only!** create an Observable from scratch by means of a function, consider `fromEmitter` instead
* [**`fromEmitter()`**](http://reactivex.io/RxJava/javadoc/rx/Observable.html#fromEmitter(rx.functions.Action1,%20rx.AsyncEmitter.BackpressureMode)) — create safe, backpressure-enabled, unsubscription-supporting Observable via a function and push events.
* [**`defer( )`**](http://reactivex.io/documentation/operators/defer.html) — do not create the Observable until a Subscriber subscribes; create a fresh Observable on each subscription
* [**`range( )`**](http://reactivex.io/documentation/operators/range.html) — create an Observable that emits a range of sequential integers
* [**`interval( )`**](http://reactivex.io/documentation/operators/interval.html) — create an Observable that emits a sequence of integers spaced by a given time interval
* [**`timer( )`**](http://reactivex.io/documentation/operators/timer.html) — create an Observable that emits a single item after a given delay
* [**`empty( )`**](http://reactivex.io/documentation/operators/empty-never-throw.html) — create an Observable that emits nothing and then completes
* [**`error( )`**](http://reactivex.io/documentation/operators/empty-never-throw.html) — create an Observable that emits nothing and then signals an error
* [**`never( )`**](http://reactivex.io/documentation/operators/empty-never-throw.html) — create an Observable that emits nothing at all

### just

- `Observable<T> just(T value)`
- `Observable<T> just(T t1, T t2)`
- ...
- `Observable<T> just(T t1, T t2, T t3, T t4, T t5, T t6, T t7, T t8, T t9, T t10)`

### from

- `Observable<T> from(java.util.concurrent.Future<? extends T> future)`
- `Observable<T> from(java.lang.Iterable<? extends T> iterable)`
- `Observable<T> from(T[] array)`
- `Observable<T> fromCallable(java.util.concurrent.Callable<? extends T> func)`

### fromEmitter

```AsyncEmitter```를 통해 원하는 시점에 데이터를 전달할 수 있다.

```java
@Experimental
public static <T> Observable<T> fromEmitter(Action1<AsyncEmitter<T>> emitter,
                                         AsyncEmitter.BackpressureMode backpressure)
```                              

```java
Observable.<Event>fromEmitter(emitter -> {
  Callback listener = new Callback() {
    @Override
    public void onEvent(Event e) {
      emitter.onNext(e);
      if (e.isLast()) {
        emitter.onCompleted();
      }
    }

    @Override
    public void onFailure(Exception e) {
      emitter.onError(e);
    }
  };
  AutoCloseable c = api.someMethod(listener);
  emitter.setCancellation(c::close);
}, BackpressureMode.BUFFER);
```

## Subscribing an Observable

- `Subscription subscribe()`
- `Subscription subscribe(Action1<? super T> onNext)`
- `Subscription subscribe(Action1<? super T> onNext, Action1<java.lang.Throwable> onError)`
- `Subscription subscribe(Action1<? super T> onNext, Action1<java.lang.Throwable> onError, Action0 onCompleted)`
- `Subscription subscribe(Observer<? super T> observer)`
- `Subscription subscribe(Subscriber<? super T> subscriber)`

## References

- [ReactiveX / RxJava](https://github.com/ReactiveX/RxJava)
- [wifi](https://github.com/ReactiveX/RxJava/wiki)
- [Javadoc](http://reactivex.io/RxJava/javadoc/rx/Observable.html)
- [Rx Design Guidelines (PDF)](http://go.microsoft.com/fwlink/?LinkID=205219)
