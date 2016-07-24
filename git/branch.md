# How to deal with Branch in Git?

## Remote Branch를 Local Branch로 가져오기

```sh
git checkout -b music origin/music
```

or

```sh
git checkout music
```

## Local Branch 생성 및 Remote Branch 생성

```sh
git checkout -b music
git push origin music
```

## Local / Remote 생성

```sh
git branch --set-upstream-to=origin/music music
```
