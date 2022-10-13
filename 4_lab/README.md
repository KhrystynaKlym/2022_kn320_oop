# Звіт до роботи №4
## Тема: Віртуальні середовища
### Мета роботи: Навчитись працювати з віртуальними середовищами.
---
## **Виконання роботи**

***- Результати виконання завдань:***



> Ізольовані віртуальні середовища - це сукупність Python інтерпретатора, бібліотек та скриптів ізольована від інших інсталяцій.


### **Основи роботи з сторонніми бібліотеками**
1. Для роботи з сторонніми бібліотеками їх потрібно спочатку встановити. Для їх встановлення є інструмент PIP (`Python Install Package`). Перевірила, чи інструмент PIP (`Python Install Package`) встановлений на комп'ютері:
    ```
    pip -V
    # Після успішного виконання команди виконайте
    pip --help
    ``` 
Скріншот виконання команди `pip -V`:

 ![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_1.png "Команда `pip -v`")

Скріншот виконання команди `pip --help`:

 ![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_2.png "Команда `pip --help`")


2. :star: Передивилася, які дії можна зробити за допомогою `pip`. Перевірила, які бібліотеки вже інстальовані на моєму комп'ютері за допомогою команди `pip list`:

Скріншот виконання команди `pip list`:

 ![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_3n.png "Команда `pip list`")


3. Будь-яку сторонню бібліотеку можна встановити на комп'ютер за допомогою `pip install` команди та зразу почати її використовувати, наприклад встановимо бібліотеки [numpy](https://numpy.org/doc/stable/user/absolute_beginners.html) та [requests](https://requests.readthedocs.io/en/latest/):


Бібліотека [numpy](https://numpy.org/doc/stable/user/absolute_beginners.html):
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_4.png "Бібліотека `numpy`")

```
    pip install numpy
    python #Зайдіть в пайтон інтерпретатор
    a = np.arange(6)
    a2 = a[np.newaxis, :]
    a2.shape
    print(a2)
```
Скріншот виконання команд:
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_5.png "Робота з бібліотекою `numpy`")
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_6.png "Виконання команди ` pip show numpy`")
____

Бібліотека [requests](https://requests.readthedocs.io/en/latest/):

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_7.png "Інсталювання бібліотеки `requests`")

```
    pip install requests
    python #Зайдіть в пайтон інтерпретатор
    import requests
    r = requests.get('https://google.com')
    print(r.text)
    print(r.status_code)
    print(r.encoding)
```
Скріншот виконання команд:
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_8.png "Робота з бібліотекою `requests`")
    
4. :star: Ознайомилась ще із методами, які є в бібліотеці [requests, та спробувала їх використати](https://requests.readthedocs.io/en/latest/user/quickstart/)

Наприклад, можна переглянути заголовки відповіді сервера:

```
    import requests
    url = 'https://api.github.com/some/endpoint'
    headers = {'user-agent': 'my-app/0.0.1'}
    r = requests.get(url, headers=headers)
    r.headers
```
Скріншот виконання команд:
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_9.png "Заголовки відповіді сервера")


5. Даний спосіб інсталяції робить бібліотеку загальнодоступною для даної системи. Будь-яке оновлення бібліотеки буде застосоване до всіх Python проектів на комп'ютері

```
    pip show requests
    pip install requests==2.1
    pip show requests
    pip uninstall requests
```
Скріншот виконання команд:

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_10.png "Результат виконання команд")

---
____

### **Робота у віртуальному середовищі** 
1. [Віртуальні середовища в Python](https://docs.python.org/3/library/venv.html) - це ізольовані середовища для роботи з 'замороженою' версією Python та його бібліотек. Середовище створюється для кожного проекту окремо і буде мати ті самі характеристики незалежно, де та на якій системі буде запущено;
2. Створила `VENV` за допомогою команди:

    ```
    python -m venv ./my_env
    ```
Скріншот виконання команд:

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_11.png "Створення `VENV`")

 :fire: Щоб не комітити всі створені файли в репозиторій, створила файл `.gitignore` у кореневій папці та вказала в ньому папки, які потрібно ігнорувати `4_lab/khrystyna/`.

Активувала своє віртуальне середовище за допомогою команди:

    ```
    source my_env/Scripts/activate
    ```
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_12.png "Активація віртуального середовища")

    ```
    pip list
    ```
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_13.png "Команда `list`")

Інсталюю бібліотеку `numpy`

    ```
    pip install numpy    
    pip list
    ```
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_14.png "Інсталяція `numpy` та виконання команди `list`")

Виконую наступні команди: інсталяція бібліотеки `requests`, команда `list`, деактивація мого віртуального середовища та команда показати `requests`:
    ```
    pip install requests
    pip list
    deactivate
    pip show requests
    ```

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_15.png "Інсталяція `requests`, `list`, деактивація середовища та виконання команди `show requests`")

3. :star: Оскільки командою `deactivate` ми деактивували наше віртуальне середовище (`khrystyna`), то остання команда вивела на екран інформацію про бібліотеку `requests`, яка знаходиться локально на комп'ютері `c:\program files\python310\lib\site-packages` (!!! а не у віртуальному середовищі !!!).

---
___
### **Робота з Pipenv**
1. [Pipenv](https://pipenv.pypa.io/en/latest/) - це інструмент для спрощення інсталяції сторонніх бібліотек та створення віруального середовища для кожного проекту. Для його інсталяції застосувала команду:
    ```
    pip install pipenv
    # Після успішного виконання команди виконала
    pipenv --help
    ``` 

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_16.png "Інсталяція `pipenv`")

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_17.png "Команда `pipenv --help`")

2. :star: За допомогою `pipenv` можна виконувати наступні команди:

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_18.png "Інсталяція `pipenv`")

3. Для створення нового середовища та інсталяції бібліотек виконала наступні команди:
    ```
    pipenv --python 3.10
    ```

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_19.png "Інсталяція `python 3.10`")

Інсталяція віртуального середовища `pipenv`:
    
    ```
    pipenv install
    ```

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_20.png "Інсталяція `pipenv`")

Команда `pipenv --venv`:

    ```
    pipenv --venv
    ```

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_21.png "Команда `pipenv --venv`")

Заходимо у віртуальне середовище та запустимо файл `4lab.py`:

    ```
    pipenv shell
    ```

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_22.png "Команда `pipenv shell` та виконання програми `4lab.py`")

Команди:

    ```
    pipenv run python -V
    pipenv install requests
    ```

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_23.png "Команди `pipenv run python -V` та `pipenv install requests`")

4. :star: У мене створився файл `Pipfile`. У ньому вказуються вимоги до пакетів для нашого додатку або бібліотеки Python, як для розробки, так і для виконання.
В `Pipfile.lock` вказується, на основі пакетів, які представленні в `Pipfile`, яку конкретну версію треба використовувати, щоб уникнути ризиків автоматичного оновлення пакетів, які є залежними один від одного, і щоб не порушити дерево залежностей наших пакетів.

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_24.png "Файл `Pipfile`")

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_30.png "Файл `Pipfile.lock`")

5. Створила пайтон файл `lab.py` та запиcала в нього наступну програму:
    ```python
    import requests

    response = requests.get('https://httpbin.org/')
    for line in response.iter_lines():
        print(line)
    ```
6. :star: Запуск програми з Visual Studio. 

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_25.png "Файл `Pipfile`")

    Запуск програми з командної стрічки. 
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_26.png "Файл `Pipfile`")  
    
    Запуск програми зайшовши у віртуальне середовище за допомогою команди `pipenv shell`.

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_27.png "Файл `Pipfile`")

7. :star: Вибрала бібліотеку `anime` на [Pypi](https://pypi.org/) та інсталювала її у віртуальному середовищі.

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_28.png "Інсталяція `anime`")

Вибрала щу одну бібліотеку `flask` на [Pypi](https://pypi.org/) та інсталювала її у віртуальному середовищі.

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_29.png "Інсталяція `flask`")

Скопіювала та запустила приклад програми, яка виводить на екран повідомлення `Hello world`

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_31.png "Програма ``Hello world``")

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_32.png "Результат роботи програми")

8. Visual Studio дозволяє змінити Python інтерпретатор для запуску через кнопку `Run` (трикутник :arrow_forward:). Для цього викликаю командну палітру з меню `View -> Command Palette...` та в ній набираю `Python: Select interpreter`. Visual Studio відображає всі доступні інтерпретатори.

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_33.png "Вибір інтерпретатора")

9. :star: Змінила інтерпретатор Python та виконала скрипт через кнопку `Run`.

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_34.png "Виконання скрипта через кнопку `Run`")

---
___
### **Робота зі змінними середовищами**
1. Середовища також можна параметризувати за допомогою змінних середовища (*Environment Variables*). Для цього у папці створюю файл `.env` із заданими змінними у форматі `KEY=VALUE`. Pipenv автоматично розпізнає ці файли та робить їх доступними всередині середовища. 

```python
import os
os.environ['HELLO']
```
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/4_lab/screenshots/Screenshot_35.png "Виконання коду")
______
______
_____
  
### ***Висновок:***

- попрацювала із сторонніми бібліотеками :heavy_check_mark:
- попрацювала у віртуальному середовищі :heavy_check_mark:
- попрацювала з Pipenv :heavy_check_mark:
- ознайомилася зі змінними середовищами :heavy_check_mark:
- дала відповіді на поставлені запитання :heavy_check_mark:
- роботу оформила. Все гуд :heavy_check_mark:
- все вдалося, всі завдання виконані :heavy_check_mark:
- завдяки Вашому детальному поясненню жодних складностей не виникло :ok_hand:  ***АЛЕ !!!!! ДУЖЕ ЧАСТО Visual Studio під Windows працює некоректно (особливо з віртуальними середовищами) і доводиться багато чого робити з командного рядка та ще й в режимі адміністратора або шукати в Google, як це зробити під Windows!!!!***
- так, подобається; це зручний формат здачі роботи :thumbsup:
- поки що побажань нема, все ГУД :smiley:
---