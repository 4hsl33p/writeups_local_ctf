# 5 is just a number

Из описания можно понять, что речь идёт о md5.

```sh
$ echo "84ea34d615c6043cc40949cca6d97233" > task.txt && hashcat -a 0 -m 0 task.txt rockyou.txt
```
    84ea34d615c6043cc40949cca6d97233:blessed1

Флаг - *4hsl33p{blessed1}*
