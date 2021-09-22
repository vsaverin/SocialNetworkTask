# Social Network Task


## Установка и настройка проекта

###### 1. Клонируйте репозиторий
```
git clone https://www.github.com/vsaverin/socialnetworktask.git
```

###### 2. Перейдите в папку проекта и активируйте виртуальное окружение
```
cd social_network_task
. ./venv/Scripts/activate
```

###### 3. Выполните установку необходимых библиотек из файла requirements.txt
```
pip install -r requirements.txt
```

###### 4. Выполните миграции
```
python manage.py migrate
```

###### 5. Запустите проект командой
```
python manage.py runserver
```

## Список поддерживаемых запросов

###### 1. Регистрация пользователя

Выполните POST запрос по адресу /api/users/
В тело запроса передайте основную информацию о пользователе:
```
{
    "user":{
        "username":"some_test_user",
        "email":"email@mail.ru",
        "password":"qweasdzxc"
    }
}
```

###### 2. Авторизация пользователя

Выполните POST запрос по адресу /api/users/login/
В тело запроса передайте email и пароль пользователя:
```
{
    "user":{
        "email":"email@mail.ru",
        "password":"qweasdzxc"
    }
}
```

При успешной авторизации будет получен ответ вида:
```
{
    "user": {
        "email": "email@mail.ru",
        "username": "some_test_user",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwiZXhwIjoxNjYzNjk2MDc4fQ.9QFSPdYPbzX0LruE2kpvswqaEf2XrK0UhkmBr35gfh4"
    }
}
```
**Обратите внимание, что для выполнения всех следующих запросов заголовке необходимо передать токен, полученный при авторизации**
```
"Authorization": "Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwiZXhwIjoxNjYzNjk2MDc4fQ.9QFSPdYPbzX0LruE2kpvswqaEf2XrK0UhkmBr35gfh4"
```

###### 3. Получение списка публикаций

Выполните GET запрос по адресу /api/users/posts
В ответ вы получите полный список публикаций:
```
[
    {
        "id": 1,
        "title": "Texas governor signs bill tightening restrictions on abortion-inducing drugs",
        "body": "(CNN)Abortion-inducing drugs in Texas will now be harder to obtain after the state's Republican governor recently signed restrictive legislation into law, weeks after another strict abortion law went into effect in the state.\r\n\r\nSenate Bill 4, signed into law by Gov. Greg Abbott on Friday, prohibits a person \"from providing an abortion‑inducing drug to a pregnant woman without satisfying the applicable informed consent requirements for abortions.\" The law requires physicians providing abortion drugs to comply with certain physician reporting requirements. Anyone who \"intentionally, knowingly, or recklessly violates\" the bill faces a state jail felony offense.\r\nA state jail felony offense is punishable by 180 days to two years to jail and a fine not exceeding $10,000, according to the state's penal code.",
        "owner": "user2"
    },
    {
        "id": 2,
        "title": "title - 2",
        "body": "Body of this test post",
        "owner": "user2"
    }
]
```

Для получение информации о конкретной публикации выполните GET запрос по адресу /api/users/posts/<id>

###### 4. Создание публикации

Выполните POST запрос по адресу /api/users/posts/
В тело запроса передайте заголовок и текст публикации:
```
{
    "title": "title - 3",
    "body": "Body of this test post"
}
```
В случае успешного создания публикации, вы получите ответ вида:
```
{
    "id": 5,
    "title": "title - 3",
    "body": "Body of this test post",
    "owner": "some_test_user"
}
```

###### 5. Поставить лайк на публикацию

Выполните POST запрос по адресу /api/users/posts/<id>/like/
В случае успешного выполнения запроса будет получен ответ вида:
```
{
    "id": 7,
    "user": 4,
    "post": 5
}
```

###### 6. Убрать лайк с публикации

Выполните DELETE запрос по адресу /api/users/posts/<id>/like/