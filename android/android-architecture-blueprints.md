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

### Code

Activity에서 Presenter의 생성자에 Fragment 인스턴스 전달.

```java
mTasksPresenter = new TasksPresenter(
    Injection.provideTasksRepository(getApplicationContext()), tasksFragment);
```

Presenter의 생성자에서 View에 Presenter 인스턴스 전달

```java
public TasksPresenter(@NonNull TasksRepository tasksRepository, @NonNull TasksContract.View tasksView) {
    ...
    mTasksView.setPresenter(this);
}
```

Fragment에서 Presenter의 `start()` 호출

```java
@Override
public void onResume() {
    super.onResume();
    mPresenter.start();
}
```

Fragment는 이벤트 발생하면 Presenter의 메서드 호출

```java
fab.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View v) {
        mPresenter.addNewTask();
    }
});
```

Fragment에 의해 호출된 Presenter의 메서드는 business logic 수행 후 Fragment 메서드 호출

```java
@Override
public void completeTask(@NonNull Task completedTask) {
    checkNotNull(completedTask, "completedTask cannot be null!");
    mTasksRepository.completeTask(completedTask);
    mTasksView.showTaskMarkedComplete();
    loadTasks(false, false);
}
```

다른 화면으로 이동하는 경우 Fragment에서 `startActivty()` 호출

```java
@Override
public void showAddTask() {
    Intent intent = new Intent(getContext(), AddEditTaskActivity.class);
    startActivityForResult(intent, AddEditTaskActivity.REQUEST_ADD_TASK);
}
```

## MVP + Loaders

https://github.com/googlesamples/android-architecture/tree/todo-mvp-loaders/

![](https://github.com/googlesamples/android-architecture/wiki/images/mvp-loaders.png)

- Task Repository에서 데이터를 가져올 때, [Loader](https://developer.android.com/guide/components/loaders.html)를 사용
- Loader의 장점
  - 데이터의 비동기식 로딩을 제공합니다.
  - **데이터의 출처를 모니터링하여 그 콘텐츠가 변경되면 새 결과를 전달합니다.**
  - 구성 변경 후에 재생성된 경우, 마지막 로더의 커서로 자동으로 다시 연결됩니다. 따라서 데이터를 다시 쿼리하지 않아도 됩니다.
- Understandability: Loaders framework에 익숙해야 함 (not trivial)
- Testability: Loaders framework를 사용함으로써 Android framework에 big dependency 생겨 unit testing이 더 어려움
- Presenter는 TaskRepository에서 직접 task 데이터를 조회하는 대신 TaskLoader를 사용
- TaskLoader는 TaskRepository에 요청하여 데이터를 가져와 client에 전달
- Android Loader framework가 정의한 lifecycle을 따라서 초기 데이터를 가져오고 변경 사항을 반영하는 과정을 구현.
- 비동기로 데이터를 가져오는 과정을 안드로이드가 쓰레드 관리 포함하여 효율적으로 처리한다.

### Code

Presenter에서 loader 초기화 요청. 마지막 인자 this는 `LoaderManager.LoaderCallbacks<List<Task>>` 인터페이스를 구현한 Presenter 자신.

```java
@Override
public void start() {
    mLoaderManager.initLoader(TASKS_QUERY, null, this);
}
```

`initLoader`에 의해서 `onCreateLoader()`가 호출되며 여기서 시작하길 원하는 loader 인스턴스 반환.

```java
@Override
public Loader<List<Task>> onCreateLoader(int id, Bundle args) {
    mTasksView.setLoadingIndicator(true);
    return mLoader;
}
```

Loader에 의해 데이터 로딩이 끝나면, `onLoadFinished()` 메서드가 UI 쓰레드에서 호출된다.

```java
@Override
public void onLoadFinished(Loader<List<Task>> loader, List<Task> data) {
    mTasksView.setLoadingIndicator(false);

    mCurrentTasks = data;
    if (mCurrentTasks == null) {
        mTasksView.showLoadingTasksError();
    } else {
        showFilteredTasks();
    }
}
```

TaskLoader는 `AsyncTaskLoader<List<Task>>`를 상속하고, `loadInBackground()`를 구현함으로써 worker thread에서 data를 가져오도록 한다.

```java
@Override
public List<Task> loadInBackground() {
    return mRepository.getTasks();
}
```

이 메서드가 반환한 데이터는 `deliverResult()`로 전달되며 callback을 통해 최종적으로 client에 전달된다.

## MVP + DataBinding

## MVP + Clean Architecture

## MVP + Dagger2

## MVP + ContentProviders
