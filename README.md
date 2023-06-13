# Автоматизация тестирования API

Этот проект содержит автотесты для проверки работоспособности API-эндпоинтов.

### Технические требования:

- API url https://jsonplaceholder.typicode.com/
- Методы, требующие проверки:
  GET /posts, POST /posts, DELETE /posts
- Методы могут принимать параметры userId, id, title, body
- В качестве языка программирования используйте python
- Добавьте в README инструкцию по поднятию проекта
- Используйте библиотеку requests, а также pytest

### Установка и запуск:

1. Склонируйте репозиторий

```sh
git clone
```

2. Перейдите в каталог проекта

```sh
cd qa-test-assignment
```

3.  Создайте и активируйте виртуальное окружение (необязательно, но рекомендуется)

```sh
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate  # Для Windows
```

4. Установите зависимости

```sh
pip install -r requirements.txt
```

5. Запустите тесты:

```sh
pytest
```
