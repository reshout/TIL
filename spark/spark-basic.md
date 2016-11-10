# Spark Basic

## Python Shell

```bash
bin/pyspark
```

```bash
IPYTHON=1 ./bin/pyspart
```

Python Shell에서는 SparkContext 객체가 sc라는 변수에 만들어진다.

```python
>>> lines = sc.textFile("../README.md")
>>> lines.count()
99
>>> lines.first()
u'# Apache Spark'
```

## Python Standalone Program

```bash
bin/spark-submit my_script.py
```

`SparkConf` 객체를 만들어 애플리케이션에 필요한 설정을 해야 `SparkContext` 생성 가능.

```python
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf=conf)
```

`SparkConf`를 생성할 때, 클래스터 URL과 애플리케이션 이름을 전달할 수 있다.

스파크를 셧다운하려면 `SparkContext`에서 `stop()` 메서드를 호출하거나 그냥 애플리케이션을 끝내면 된다.

## Setting

### Logging

conf/log4j.properties

```
log4j.rootCategory=WARN, console
```
