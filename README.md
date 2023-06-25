# <div align="center"> NVI Solutions LLC test </div>
Сервис для распознования изображений


## Технологии
[![Python version](https://img.shields.io/badge/Python-3.11-green)](https://www.python.org/)
[![Flask version](https://img.shields.io/badge/Flask-2.3.2-green)](https://flask.palletsprojects.com/en/2.3.x/)
[![TorchVision](https://img.shields.io/badge/TorchVision-0.15.2-green)](https://pytorch.org/vision/stable/index.html)


## Запуск приложения:
Клонировать репозиторий на локальный пк:
```
git clone https://github.com/mAXxtor/NVI-Solutions-LLC-test.git
```
Перейти в рабочую директорию:
```
cd NVI-Solutions-LLC-test
```
Создать и активировать виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```
Установить зависимости:
```
pip install -r requirements.txt
```
Запустить приложение:
```
flask run
```

## Использование приложения:
После запуска приложения перейдите на страницу http://127.0.0.1:5000  
Выберите и загрузите изображение (максимальный размер 16Mb)  
На экране отобразится результат распознования изображения:
- Ширина изображения в px
- Высота изображения в px
- Категория классификатора (используется модель )
