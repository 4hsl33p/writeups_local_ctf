# PPPPOST PPPPLLSSS

![Task](img/view_task.png)

Отправляем **POST** запрос - получаем флаг.

```sh
$ python3 -c "import requests as r;print(r.post('http://46.254.20.217:1000/task_2').text)" > req.txt && grep "4hsl33p" req.txt && rm req.txt"
```

Флаг - *4hsl33p{n0t_just_g3t}*