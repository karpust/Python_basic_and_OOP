import re

# символьные классы:
s = 'Еда, еду, победа'
m = re.findall(r'[Ее]д[уа]', s)  # ['Еда', 'еду', 'еда']
# [набор символов] - ищет один символ из набора
# все перечисленные в наборе символы кроме \ ничего не делают.
# [ \t] - ищем 1 символ: пробел или таб
# [0-9][a-z] - ищет 2 символа рядом
# [-0-9] - ищет дефис или цифру от0 до9
# [^0-9] - все кроме цифр
# [а-яА-Я0-9]

''' ---------------------------- квантификаторы z{m, n}: ---------------------------------- '''
# где m-минимальное число совпадений с выражением
# n-максимальное
# выбирeт все где символ 'z' встречается от m до n раз.
# жадные(мажорные) квантификаторы тк ищут максим длину
# (те из ооо не выберут оо):
s = 'Google, Gooogle, Goooooogle'
m = re.findall(r'o{2,5}', s)  # ['oo', 'ooo', 'ooooo']
# минорные:
m = re.findall(r'o{2,5}?', s)  # ['oo', 'oo', 'oo', 'oo', 'oo']
# квантификаторы сокращенно:
# {m} - точное кол-во раз {m}
# {m,} - от m и больше {m,}?
# {,n} -  не более n раз {,n}?
m = re.findall(r'Go{,4}gle', s)
# ['Google', 'Gooogle']
phone = '89123456789'
m = re.findall(r'8\d{10}', phone)  # ['89123456789']
'''
? аналог {0,1}
* аналог {0,}
+ аналог {1,}
их минорные режимы: ??, *?, +?
'''
s = 'стеклянный, стекляный'
m = re.findall(r'стеклянн?ый', s)  # ['стеклянный', 'стекляный']
text = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001"
m = re.findall(r"\w+\s*=\s*[^;]+", text)
# ['author=Пушкин А.С.', 'title = Евгений Онегин', 'price =200', 'year= 2001']
s = "Картинка <img src='bg.jpg'> в тексте</p>"
m = re.findall(r"<img.*>", s)  # ["<img src='bg.jpg'> в тексте</p>"] *жадный
m = re.findall(r"<img.*?>", s)  # ["<img src='bg.jpg'>"] минорный
m = re.findall(r"<img.[^>]*", s)  # ["<img src='bg.jpg'"] так и с мажорным
m = re.findall(r"<img\s+[^>]*?src\s*=\s*[^>]*>", s)  # ["<img src='bg.jpg'>"]

''' ---------------------------- группировка и сохранение -----------------------------'''
# задача выделить данные в формате ключ:значение :
s = "lat = 5, lon=7, pi=3, a = 5"
# будет работать для всех ключей:
m = re.findall(r"\w+\s*=\s*\d+", s)  # ['lat = 5', 'lon=7', 'pi=3', 'a = 5']
# но нужны только ключи lat и lon:
m = re.findall(r"lat\s*=\s*\d+|lon\s*=\s*\d+", s)  # ['lat = 5', 'lon=7']
# уберем дублирование в выражении:
# несохраняющая группировка '?:' :
m = re.findall(r"(?:lat|lon)\s*=\s*\d+", s)  # ['lat = 5', 'lon=7']
# сохраняющая группировка:
m = re.findall(r"(lat|lon)\s*=\s*\d+", s)  # ['lat', 'lon'] - второй уровень
m = re.findall(r"((lat|lon)\s*=\s*\d+)", s)  # [('lat = 5', 'lat'), ('lon=7', 'lon')] - оба уровня
# отдельно сохраним ключи и значения:
m = re.findall(r"(lat|lon)\s*=\s*(\d+)", s)  # [('lat', '5'), ('lon', '7')]
m = re.findall(r"(lat|lon)\s*=\s*(?:\d+)", s)  # ['lat', 'lon'] - сохр только ключи

s = "Картинка <img src='bg.jpg'> в тексте</p>"
m = re.findall(r"<img\s+[^>]*src=[\"'](.+?)[\"']", s)  # ['bg.jpg']
# но если в пути ошибка, то тоже отработает:
s = "Картинка <img src='bg.jpg\"> в тексте</p>"
m = re.findall(r"<img\s+[^>]*src=[\"'](.+?)[\"']", s)  # ['bg.jpg']
# исправляем - ищем одинаковые кавычки:
m = re.findall(r"<img\s+[^>]*src=([\"'])(.+?)\1", s)  # []
# вместо индекса \1 подставится значение первой сохр группировки(отсчет с 1)
# исправили ошибку - отработает верно:
s = "Картинка <img src='bg.jpg'> в тексте</p>"
m = re.findall(r"<img\s+[^>]*src=([\"'])(.+?)\1", s)  # [("'", 'bg.jpg')]
# вместо индексов назнач имена сохр группировкам (?P<name>...) а обращаться (?P=name)
m = re.findall(r"<img\s+[^>]*src=(?P<quotes>[\"'])(.+?)(?P=quotes)", s)  # [("'", 'bg.jpg')]


''' ------------------------------------------- флаги и проверки --------------------------------------------'''
# найти слово как самостоятельное а не как часть другого:
s = "подоходный налог"
m = re.findall(r"прибыль|обретение|доход", s)  # ['доход'] нашел как часть слова
m = re.findall(r"прибыль|обретение|\bдоход\b", s)  # [] то что надо
m = re.findall(r"\bприбыль\b|\bобретение\b|\bдоход\b", s)  # [] но
# избавимся от функц дублирования, исп группировку:
# здесь проверка \b применяется к группе а не к слову:
# те сам символ \b в строке не ищется, а определяется граница слова в шаблоне, где он записан:
m = re.findall(r"\b(?:прибыль|обретение|доход)\b", s) # []

s = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1251">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Уроки по Python</title>
</head>
<body>
<script type="text/javascript">
let o = document.getElementById('id_div');
console.log(obj);
</script>
</body>
</html>"""
# выделить содержимое тега script:
m = re.findall(r"^<script.*?>([\w\W]+)", s, re.MULTILINE)
# ["\nlet o = document.getElementById('id_div');\nconsole.log(obj);\n</script>\n</body>\n</html>"]
m = re.findall(r"^<script.*?>([\w\W]+)(?=</script>)", s, re.MULTILINE)
# ["\nlet o = document.getElementById('id_div');\nconsole.log(obj);\n"]
# XY(?=Y) значит: найди X если за ним следует Y
# X(?=!Y) значит: найди X если за ним не следует Y
# ретроспективная проверка:
m = re.findall(r"^<script.*?>([\w\W]+)(?<=</script>)", s, re.MULTILINE)
# ["\nlet o = document.getElementById('id_div');\nconsole.log(obj);\n</script>"]
# XY(?<=Y) значит: найди XY если он заканчивается на Y
# (?<=Y)X значит: найди X если перед ним есть Y
# (?<=!Y)X значит: найди X если перед ним нет Y

# выбрать все пары ключ/значение:
m = re.findall(r"([-\w]+)[ \t]*=[ \t]*[\"']([^\"']+)(?<![ \t])", s, re.MULTILINE)
# [('http-equiv', 'Content-Type'), ('content', 'text/html; charset=windows-1251'),
# ('name', 'viewport'), ('content', 'width=device-width, initial-scale=1.0'),
# ('type', 'text/javascript')]
s = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type " content="text/html; charset=windows-1251">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Уроки по Python</title>
</head>
<body>
<p align=center>Hello World!</p>
</body>
</html>"""
# проверка на наличие группирующего выражения:
# (?(id|name)do_if_group_exsixts)
# (?(id|name)do_if_group_exsixts|do_if_group_not_exsixts)
m = re.findall(r"([-\w]+)[ \t]*=[ \t]*(?P<q>[\"'])?(?(q)([^\"']+(?<![ \t]))|([^ \t>]+))", s, re.MULTILINE)
# [('http-equiv', '"', 'Content-Type', ''), ('content', '"', 'text/html; charset=windows-1251', ''),
# ('name', '"', 'viewport', ''), ('content', '"', 'width=device-width, initial-scale=1.0', ''),
# ('align', '', '', 'center')]

# исп флагов:
m = re.findall(r"""([-\w]+)             
                   [ \t]*=[ \t]*            
                   (?P<q>[\"'])?           
                   (?(q)([^\"']+(?<![ \t]))|([^ \t>]+))""",
                   s, re.MULTILINE|re.VERBOSE)
# запись флагов внутри выражения (?flags)
s = "Python, python, PYTHON"
m = re.findall(r"(?im)python", s)
# ['Python', 'python', 'PYTHON']

''' --------------------------------------- Match object, его методы -------------------------------------------------'''
s = "<font color=#CC0000>"
m = re.search(r"(\w+)=(#[\da-fA-F]{6})\b", s)
# <re.Match object; span=(6, 19), match='color=#CC0000'>

m.groups()  # вернет кортеж со всеми группами: ('color', '#CC0000')

# вернет группу в соотв с индексом: 0 - полное совпадение,
# др индексы соотв сохраняющим группам:
m.group(0)  # 'color=#CC0000'
m.group(1)  # 'color'
m.group(2)  # '#CC0000'
m.group(0, 1, 2)  # ('color=#CC0000', 'color', '#CC0000')

m.lastindex  # 2 - послед индекс сохран группы
m.start(1)  # 6 - позиция начала группы 1
m.end(1)  # 11 - позиция конца группы 1
m.span(0)  # (6, 19) - начало и конец всего совпадения
m.span(1)  # (6, 11) - или группы
m.endpos  # 20 - послед позиция до кот шла проверка
m.pos  # 0 - начальная позиция с кот шел поиск
m.re  # вернет скомпилированный шаблон - re.compile('(\\w+)=(#[\\da-fA-F]{6})\\b')
m.string  # вернет анализируемую строку - '<font color=#CC0000>'

# шаблон с именованными группами:
m = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", s)
m.groupdict()  # {'key': 'color', 'value': '#CC0000'}
m.lastgroup  # 'value' - вернет последнюю группу или None если их нет

# сформировать строку из групп где:
# \g<name> - обращение к группе по имени,
# \1, \2, - обращение к группе по номеру:
m.expand(r"\g<key>:\g<value>")  # 'color:#CC0000'

''' ----------------------------------------- функции модуля re -----------------------------------------'''
# все методы написаны на С(быстрые)

# re.match(pattern, string, flags=0)
# ищет совпадение шаблона в начале строки.
# вернет match object или None если нет совпадений:
s = "+7(123)456-78-90"
m = re.match(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", s)
# <re.Match object; span=(0, 16), match='+7(123)456-78-90'>


# re.search(pattern, string, flags=0)
# поиск первого вхождения в тексте, удовлетв регулярному выражению(pattern)
s = "<font color=#CC0000 bg=#ffffff>"
m = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", s)
m.groups()  # ('color', '#CC0000') - нашел только первое ссответствие


# re.finditer(pattern, string, flags=0)
# возвращает итерируемый объект для перебора всех вхождений
for m in re.finditer(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", s):
    print(m.groups())  # ('color', '#CC0000')
                       # ('bg', '#ffffff')


# re.findall(pattern, string, flags=0)
# вернет список найденных вхождений, групп:
m = re.findall(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", s)
# [('color', '#CC0000'), ('bg', '#ffffff')]


# re.split(pattern, string, maxsplit=0, flags=0)
# разобьет строку по заданному шаблону:
s = """<point lon="40.8482" lat="52.6274" />
<point lon="40.8559" lat="52.6361" />; <point lon="40.8614" lat="52.651" />
<point lon="40.8676" lat="52.6585" />, <point lon="40.8672" lat="52.6626" />
"""
m = re.split(r"[\n;,]+", s)
# ['<point lon="40.8482" lat="52.6274" />', '<point lon="40.8559" lat="52.6361" />',
# ' <point lon="40.8614" lat="52.651" />', '<point lon="40.8676" lat="52.6585" />',
# ' <point lon="40.8672" lat="52.6626" />', '']


# re.sub(pattern, repl, string, count=0, flags=0)
# заменяет в строке найденные совпадения строкой или результатом
# работы функции repl и возвращает преобразованную строку.
s = """Москва Казань Тверь"""
# здесь repl - строка замены:
m = re.sub(r"\s*(\w+)\s*", r"<option>\1</option>\n", s)
# '<option>Москва</option>\n<option>Казань</option>\n<option>Тверь</option>\n'
# здесь repl - кастомная функция:
count = 0
def replFind(m):
    global count
    count += 1
    return f"<option value='{count}'>{m.group(1)}</option>\n"


m = re.sub(r"\s*(\w+)\s*", replFind, s)
# "<option value='1'>Москва</option>\n
# <option value='2'>Казань</option>\n
# <option value='3'>Тверь</option>\n"


# re.subn(pattern, repl, string, count=0, flags=0)
# заменяет в строке найденные совпадения строкой или результатом
# работы функции repl и возвращает преобразованную строку и число произведенных замен.
l, t = re.subn(r"\s*(\w+)\s*", r"<option>\1</option>\n", s)
# ('<option>Москва</option>\n<option>Казань</option>\n<option>Тверь</option>\n', 3)


# re.compile(pattern, flags=0)
# выполняет компиляцию регулярного выражения и возвращает его в виде экземпляра класса Pattern
# Компиляция регулярного выражения применяется, если один и тот же шаблон используется многократно.
s = """Москва Казань Тверь"""
count = 0
def replFind(m):
    global count
    count += 1
    return f"<option value='{count}'>{m.group(1)}</option>\n"


rx = re.compile(r"\s*(\w+)\s*")
lt = rx.subn(r"<option>\1</option>\n", s)
# ('<option>Москва</option>\n<option>Казань</option>\n<option>Тверь</option>\n', 3)
l = rx.sub(replFind, s)
# "<option value='4'>Москва</option>\n<option value='5'>Казань</option>\n<option value='6'>Тверь</option>\n"

