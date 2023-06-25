# <div align="center"> NVI Solutions LLC test </div>
Сервис для распознования изображений


## Технологии
[![Python version](https://img.shields.io/badge/Python-3.11-green)](https://www.python.org/)
[![Flask version](https://img.shields.io/badge/Flask-2.3.2-green)](https://flask.palletsprojects.com/en/2.3.x/)
[![TorchVision](https://img.shields.io/badge/TorchVision-0.15.2-green)](https://pytorch.org/vision/stable/index.html)


## Запуск приложения:
Склонируйте репозиторий проекта в рабочую директорию на локальный ПК:
```
git clone https://github.com/mAXxtor/NVI-Solutions-LLC-test.git
```
Перейдите в директорию с проектом:
```
cd NVI-Solutions-LLC-test
```
Создайте и активируйте виртуальное окружение:  
***- Windows ***
```
python -m venv venv
source venv/Scripts/activate
```
***- MacOS ***
```
python3 -m venv venv
source venv/bin/activate
```
Установите зависимости для работы приложения:
```
pip install -r requirements.txt
```
Запустите веб-приложение:
```
flask run
```

## Использование приложения:
![](https://github.com/mAXxtor/NVI-Solutions-LLC-test/useapp.gif)
После запуска приложения перейдите на страницу http://127.0.0.1:5000  
Выберите и загрузите изображение (максимальный размер 16Mb)  
На экране отобразится результат распознования изображения:
- Ширина изображения в px
- Высота изображения в px
- Категория классификатора (используется модель )
