# Workmate Test Task

## Библиотеки

Для приложения используются библиотеки FastAPI и Sqlalchemy на движке Asyncpg

## Установки

### Запуск вне Docker

Необходимо создать файл __.env__ на подобии с __.env.template__

Создать виртуальное окружение __python -m venv .venv__ и установить зависимости __pip install app/requirements.txt__

Для запуска приложения использовать в терминале __uvicorn main:app__

### Запуск в Docker 

Использовать команду __docker-compose up__

## Использование

При первом запуске создаются 10 котят со случайными данными 

Просмотр всех котят - /cats
Также в этом методе реализована фильтрация котят по породе

Просмотр одного котенка - /cat/{id}

Измененение котенка - /cat/{id}

Удаление котенка - /cat/{id}

Создание котенка - /cat

Просмотр всех пород - /kinds
