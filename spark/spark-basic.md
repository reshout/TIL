# Spark Basic

## Python Shell

```bash
bin/pyspark
```

```bash
IPYTHON=1 ./bin/pyspart
```

### Python Example

sc = Main entry point for Spark functionality

```python
>>> lines = sc.textFile("../README.md")
>>> lines.count()
99
>>> lines.first()
u'# Apache Spark'
```

## Logging

conf/log4j.properties

```
log4j.rootCategory=WARN, console
```
