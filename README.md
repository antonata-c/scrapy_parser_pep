# Асинхронный Парсер Python документации
### Описание проекта
Данный проект выполняет парсинг данных со страниц [PEP](https://peps.python.org/), переходит по ссылкам и собирает данные о каждом PEP.

### Технологии
- `Python 3.10`
- `Scrapy`
***
### Развертывание и запуск проекта
* #### Склонируйте репозиторий
```shell
git clone https://github.com/antonata-c/scrapy_parser_pep.git
```
```shell
cd scrapy_parser_pep
```

* #### Создайте и активируйте виртуальное окружение (для Linux/MacOS)
```shell
python3 -m venv venv
source venv/bin/activate
```
* #### Для Windows
```shell
python -m venv venv
source venv/Scripts/activate
```
* #### Установите зависимости
```shell
pip install --upgrade pip
pip install -r requirements.txt
```
***
### Запустите парсер
```shell
scrapy crawl pep
```
### Автор проекта
[Антон Земцов](https://github.com/antonata-c)