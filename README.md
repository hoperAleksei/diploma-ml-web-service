# Diploma

## Инструкция по запуску

Для разработки проекта используется docker версии 24.

### Запуск проекта на [localhost:80](http://localhost)

```shell
docker compose up -d
```

### Установка последней версии миграции БД

```shell
docker compose server exec alembic upgrade head
```

В случае ошибки, работает другой способ:

```shell
docker compose server exec bash
```
И в контейнере, запустить:
```shell
alembic upgrade head
```
