# <div align="center"> NVI Solutions LLC test </div>
Сервис для распознования изображений


## Технологии
[![Python version](https://img.shields.io/badge/Python-3.11-green)](https://www.python.org/)
[![Flask version](https://img.shields.io/badge/Flask-2.3.2-green)](https://flask.palletsprojects.com/en/2.3.x/)
[![TorchVision](https://img.shields.io/badge/TorchVision-0.15.2-green)](https://pytorch.org/vision/stable/index.html)


## Запуск приложения в Docker контейнере:
Авторизуйтесь в терминале на Docker Hub:
***- Windows***
```
docker login --username <username>
```
***- MacOS***
```
sudo docker login --username <username>
```
Загрузите образ проекта с Docker Hub:
***- Windows***
```
docker pull maxxtor/nvi_solutions_llc_test:v0.1
```
***- MacOS***
```
sudo docker pull maxxtor/nvi_solutions_llc_test:v0.1
```
Запустите контейнер:
***- Windows***
```
docker run -p 5000:5000 -d maxxtor/nvi_solutions_llc_test:v0.1
```
***- MacOS***
```
sudo docker run -p 5000:5000 -d maxxtor/nvi_solutions_llc_test:v0.1
```

## Запуск приложения локально:
Склонируйте репозиторий проекта в рабочую директорию на локальный ПК:
```
git clone https://github.com/mAXxtor/NVI-Solutions-LLC-test.git
```
Перейдите в директорию с проектом:
```
cd NVI-Solutions-LLC-test
```
Создайте и активируйте виртуальное окружение:  
***- Windows***
```
python -m venv venv
source venv/Scripts/activate
```
***- MacOS***
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
![](https://github.com/mAXxtor/NVI-Solutions-LLC-test/blob/main/useapp.gif)
После запуска приложения перейдите на страницу http://127.0.0.1:5000 или http://localhost:5000 (если запустили в Docker контейнере)  
Выберите и загрузите изображение (максимальный размер 16Mb, расширения *.png, *.jpg, *.jpeg)  
На экране отобразится результат распознования изображения:
- Ширина изображения в px
- Высота изображения в px
- Категория классификатора (используется модель resnet50)
