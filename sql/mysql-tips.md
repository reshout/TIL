# MySQL Tips

## Reset Root Password

http://www.litcoder.com/archives/495

```
$ sudo service mysql stop
```

/etc/mysql/my.conf 파일에 skip-grant-tables 추가

```
$ sudo service mysql start
$ mysql -uroot mysql
UPDATE user SET password=PASSWORD('password') WHERE user='root';
```
/etc/mysql/my.conf 파일에 skip-grant-tables 삭제

```
$ sudo service mysql restart
```
