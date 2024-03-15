# Ru_It_WordReminder
Приложение для ненавязчивого заучивания итальянских слов. Представляет из себя окно 500х200 поверх всех окон, в котором 1 раз в 10 секунд обновляется слово на русском языке и его перевод.

### Установка через GitHub:
1) Клонируем репозиторий себе
```
git@github.com:AlekseiViunik/Ru_It_WordReminder.git
```
2) Переходим в корневую папку репозитория
3) Активируем виртуальное окружение:<br/>

Для Linux:
```
python3 -m venv venv
source venv/bin/activate
```
Для Windows:
```
python -m venv venv
source venv/Scripts/activate
```
4) Устанавливаем зависимости:
```
pip install -r requirements.txt
```
5) Запускаем главный файл:

Для Linux:
```
python3 client.py
```
Для Windows:
```
python client.py
```
6) Есть так же возможность скомпилировать исполняемый файл с расширением .exe или .bin в зависимости от операционной системы. Для этого в зависимостях имеется Nuitka:

Для Linux:
```
python3 -m nuitka --windows-disable-console --follow-imports client.py
```
Для Windows:
```
python -m nuitka --windows-disable-console --follow-imports client.py
```





