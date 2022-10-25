# Звіт до роботи №5
## Тема: Тестування
### Мета роботи: Навчитись працювати з тестуванням на Python.
---
## **Виконання роботи**

***- Результати виконання завдань:***


1. Для роботи створимо декілька Python файлів. 
---

### Перевірка assert
1. `assert` - це перевірка певних тверджень та встановлення працездатності коду. Твердження дозволяють перевірити правильність коду, перевіряючи, чи виконуються певні умови.

    Наприклад, після виконання даного коду виводиться повідомлення про помилку, оскільки число повинне бути більшим від нуля.
```Python
    number = -1
    assert number > 0, "число має бути більшим за нуль!"
```
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_1.png "Повідомлення про помилку!")

    Після виконання даного коду, виводиться повідомлення про помилку, оскільки, значення `name` повинно містити символи таблиці ASCII, а значення маси має бути числом.

```python
class Animal:
    def __init__(self, name:str, mass) -> None:
        assert name.isascii(), "Значення name повинно містити символи таблиці ASCII"
        self.name = name

    a = Animal("Tiger")
    print(a.name)
    b = Animal("Тигр")
    print(b.name)
```

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_2.png "Повідомлення про помилку!")

Після виконання цього коду, виводиться повідомлення про помилку, оскільки, значення `mass` повинно бути числом типу `float`.

```python
        class Animal:
        def __init__(self, name:str, mass) -> None:
            assert name.isascii(), "Значення name повинно містити символи таблиці ASCII"
            self.name = name
            # Можна assert замінити на IF
            if isinstance(mass, float):
             self.mass = mass
            else:
              raise AssertionError("Маса має бути введена цифрами")

        a = Animal("Monkey", '40.5')
        print(a.name, a.mass)
```

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_3.png "Повідомлення про помилку!")


2. :star: Створила власний крок `assert` та зробила тестові превірки при введенні даних з клавіатури. Для цього використала метод `input`:

    ```python
    a = input("Введіть число: ")
    assert a.isdigit(), "Потрібно ввести число!"
    print(f"введене число: {a}")
    ```
    Коли ввела число, то програма працює коректно і виводить введене число на екран:
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_4.png "Нема помилки!")

    Коли ввела ім'я Khrystyna, то програма вивела повідомлення про помилку а саме, що треба ввести число, а не слово. 

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_5.png "Ввід слова!")

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_6.png "Повідомлення про помилку!")

3. В ООП методи `assert` найкраще виконувати для перевірки (валідації) правильності вводу аргументів. Для прикладу маємо простий клас, в якому здійснюємо валідацію даних перед тим як створювати об'єкт. Умовою валідації може бути будь-який вираз Python який повертає значення True/False.

    ```python
    class Figure:
        def __init__(self, type, length) -> None:
            assert length > 0, "Довжина має бути більшою за 0!"
            assert type in ["квадрат", "прямокутник", "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
            self.type = type
            self.length = length

    a = Figure("квадрат", 12)
    print(a.type, a.length)
    b = Figure("трикутник", 10)
    print(b.type, b.length)
    c = Figure("прямокутник", 1)
    print(c.type, c.length)
    ```
3. :star: Виконаємо код наведений вище для різних об'єктів.
    Програма не видає помилку у випадках, коли вводимо фігуру із переліку дозволених (квадрат, прямокутник чи трикутник) та довжину більшу від нуля.  

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_7.png "Нема помилки!")

Коли ж вводимо назву фігури, якої нема у переліку дозволених фігур або ж довжину рівну нулю, то виводиться повідомлення про помилку: `"Дозволені фігури: квадрат, прямокутник, трикутник"` або `"Довжина має бути більшою за 0!"`

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_8.png "Повідомлення про помилку!")

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_9.png "Повідомлення про помилку!")

4. Перевірки можна організовувати і іншими способами, наприклад з використанням умовного розгалуження. Якщо дані введені невірно, можна викликати клас помилки.

    ```python
    class Name:
        def __init__(self, name) -> None:
            if name not in ["Богдан", "Анонім"]:
                raise ValueError("Дозволені імена: Богдан, Анонім")
            self.name = name

    a = Name("Бодько")
    ```
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_10.png "Повідомлення про помилку!")

5. :star: Додала власне ім'я (`Христина`) в перевірку, та створила такий об'єкт. Додала ще один аргумент в клас (хоббі) та здійснила валідацію, чи хоббі є введено (поле не пусте).
    ```python
    class Name:
        def __init__(self, name:str, hobby) -> None:
            if name not in ["Христина", "Богдан", "Анонім"]:
                raise ValueError("Дозволені імена: Христина, Богдан, Анонім")
            if not hobby:
                raise ValueError("Поле 'hobby' пусте! Введіть своє хоббі!!!")
            
            self.name = name
            self.hobby = hobby
    a = Name("Христина", "Танці")
    print(a.name, a.hobby)
    b = Name("Христинка", "Танці")
    print(b.name, b.hobby)
    с = Name("Христина", "")
    print(с.name, с.hobby)
    ```
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_11.png "Працює коректно!")

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_12.png "Повідомлення про помилку у введеному імені!")

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_13.png "Повідомлення про помилку з полем 'hobby'!")


---

### Юніт тести
> Це перевірка малої частини коду, юніта. Найчастіше це порівняння між введеними даними та результатом виконання якоїсь частини програми.
1. Найпростіше використовувати вбудовану бібліотеку для юніт тестів `unittest`. Зазвичай юніт тести створюються в окремому файлі, однак в межах проекту, який має бути протестованим.

Створила файл `tests.py`.

Виконати тести можна двома способами:
   1. Оскільки, у програмі є блок з викликом бібліотеки `unittest.main()`, то програму можна викликати з Visual Studio Code через кнопку `Run` (трикутник :arrow_forward:) або через регулярний Python файл:
```bash
   python test.py
```
    
```python
    import unittest

    from lab5 import Animal

    class TestMyApp(unittest.TestCase):
        def test_if_object_created(self):
            name = "Monkey"
            mass = 40.5
            obj = Animal(name, mass)
            self.assertEqual(obj.name, name)
            self.assertEqual(obj.mass, mass)
            self.assertIsInstance(obj, Animal)
            self.assertNotIsInstance(obj, str)

        def test_mock(self):
            self.assertTrue(False)

    if __name__ == '__main__':
    unittest.main(verbosity=2)
```

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_14.png "Виконання юніт тестів командою 'Run` з Visual Studio")
Тут із двох виконаних тестів один провалився.

2. У випадку, якщо немає запуску `unittest.main()`, то треба виконати команду з явним викликом бібліотеки `unittest` (для більш детального виводу можна додати опцію `-v` або `--verbose`):
   ```bash
   python -m unittest
   ```
Щоб виконати тести з консолі, закоментую рядки

```python
        #if __name__ == '__main__':
        #unittest.main(verbosity=2)
```

    В консолі перейду в папку `5_lab` (cd 5_lab) та введу команду:
```
        python -m unittest
```
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_15.png "Виконання юніт тестів з консолі")
Як бачимо, тут виконали два тести, один з яких виконався успішно, а один провалився.

2. Створюю простий клас з двома пропертями та навмисно зроблю помилку в ньому. Для коректної роботи з тестами назву файл `app.py`. Це буде потрібно для імпорту бібліотек (класів).
    ```python
    class Figure:
        FIGURES = ["квадрат", "прямокутник", "трикутник"]
        def __init__(self, type, length) -> None:
            assert length > 0, "Довжина має бути більшою за 0!"
            assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
            self.type = type
            self.length = length

        @property
        def get_figure_type(self):
            return self.type

        @property
        def get_figure_length(self):
            return self.type # робимо помилку
    ```

3. Створюю юніт тести у файлі `tests1.py` та спробую перевірити тестовий клас `Figure`, щоб все працювало правильно. Для цього у методі `setUp` за допомогою бібліотеки `random` створюю об'єкт та перевіряю, чи правильно працюють методи:
    ```python
    import unittest
    from random import choice, randint

    from app import Figure # назва файлу з нашим класом повинна бути app.py

    class TestFigure(unittest.TestCase):
        def setUpClass(cls):
            """Виконається лише раз на початку тестів
            """
            pass
        
        def setUp(self) -> None:
            """Виконується кожного разу коли запускається тест
            """
            self.figure = choice(Figure.FIGURES)
            self.length = randint(1, 10)
            self.obj = Figure(self.figure, self.length)
            return super().setUp()

        def tearDown(self) -> None:
            del self.obj
            return super().tearDown()

        def test_figure_type(self):
            print(f"Тестуємо вивід, має бути: {self.figure} == {self.obj.get_figure_type}")
            self.assertEqual(self.figure, self.obj.get_figure_type, "Властивість get_figure_type повертає неправильну фігуру!")

        def test_figure_lengh(self):
            self.assertEqual(self.length, self.obj.get_figure_length, "Властивість get_figure_length повертає неправильну довжину!")
        
        def test_obj(self):
            with self.assertRaises(AssertionError):
                Figure("коло", 1) # Спробуємо створити об'єкт з недозволеними параметрими, в нас має бути помилка AssertionError


    if __name__ == '__main__':
        unittest.main() # unittest.main(verbosity=2) щоб був більш детальний вивід
    ```
4. Виконую тести двома способами:
   1. виклик з Visual Studio Code через кнопку `Run` (трикутник :arrow_forward:):
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_16.png "Виконання юніт тестів командою 'Run` з Visual Studio")   

   2. виклик напряму з консолі виконанням команди з явним викликом бібліотеки `unittest`. Для детальнішого виводу можна додати опцію `-v` або `--verbose`:
   
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_17.png "Виконання юніт тестів з консолі") 

5. :fire: При виконанні юніт тестів з'явилася папка `__pycache__`, яку не треба комітити в репозиторій, тому додаю її в `.gitignore`.

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_18.png "Файл `.gitignore`") 
---

### Юніт тести з використання бібліотеки PyTest
> PyTest це стороння бібліотета для тестування коду
1. Оскільки, це стороння бібліотека, то інсталюю її. Для цього:. Бібліотеки для юніт тестів краще ставити в `--dev` середовище.
    ```
    pip install pytest
    ```
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_19.png "Інсталювання бібліотеки `pytest`") 

Запустимо з терміналу `pytest tests.py`

![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_21.png "Запуск `pytest tests.py`") 

2. Дана бібліотека може працювати як з вбудованими тестами, які ми вже маємо, так і з будь-якими функціями, які розпочинаються з слова `test_`. Для прикладу зроблю простий тест та поміщу всередині того ж файлу, де і наш клас `Figure`:
    - створюю простий тест у файл `app.py`:
    ```python
    def test_app_triangle():
        """Test if we create triangle figure.
        """
        fig = "трикутник"
        triangle = Figure(fig, 4)
        assert triangle.type == fig, f"Фігура має бути {fig}"
    ```
    - запускаю тести за допомогою `pytest`:
    ```
    pytest app.py
    ```
3. :star: Програма вивела:
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_22.png "Запуск `pytest app.py`")

Функція `test_app_triangle` виконалася!!!

___________

### Візуалізація результатів та покриття коду Coverage (pytest-cov)
> Допоміжна бібліотека для збору статистики покриття коду юніт тестами. Покриття тестами - це відношення між кількістю рядків, виконаних хоча б одним тестом, до загальної кількості рядків кодової бази.
1. Можна використовувати бібліотеку [coverage](https://coverage.readthedocs.io/en/6.5.0/) або плагін [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/readme.html).
    - для інсталяції потрібно виконати наступні команди:
    ```
    pip install coverage --dev
    # АБО
    pip install pytest-cov --dev
    ```
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_23.png "Інсталювання бібліотеки `coverage`")

2. Для виводу покриття коду тестами потрібно або використовувати новий інструмент `coverage`, або передавати аргументи у виклик `pytest`.
    - виклик `coverage`:
    ```
    coverage run -m pytest tests.py
    coverage run -m unittest discover
    coverage report
    ```
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_24.png "Формування `coverage report`")

3. :star: Для візуалізації результаів не в консолі, а через браузер - згенерувала звіт у форматі `html`. Отриманий файл є у звіті.
    ```
    coverage html
    ```       
![alt text](https://github.com/KhrystynaKlym/2022_kn320_oop/raw/main/5_lab/screenshots/Screenshot_25.png "Формування `coverage report`")
______
______
_____
  
### ***Висновок:***

- ознайомилась з перевірками `assert` :heavy_check_mark:
- попрацювала з юніт тестами :heavy_check_mark:
- попрактикувалася в роботі з юніт тестами із використанням бібліотеки `PyTest` :heavy_check_mark:
- ознайомилась із візуалізацією результатів та покриттям коду `Coverage (pytest-cov)` :heavy_check_mark:
- дала відповіді на поставлені запитання :heavy_check_mark:
- роботу оформила. Все гуд :heavy_check_mark:
- все вдалося, всі завдання виконані :heavy_check_mark:
- завдяки Вашому детальному поясненню жодних складностей не виникло :ok_hand:
- так, подобається; це зручний формат здачі роботи :thumbsup:
- поки що побажань нема, все ГУД :smiley:
---