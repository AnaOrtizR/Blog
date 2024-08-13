# Proyecto Portafolio Blog

## Objetivo del proyecto:
    Generar un proyecto en python que me permita practicar mis habilidades de programación backend.

## Objetivo de la applicación:
    Permitir a los usuario crear sus propios artículos en un Blog, además de permitir comentar artículos de otros usuarios. 
    (\blog_ClassDiagram.jpg)
### Caso de uso
    Creación de artículo:
    Descripción:
        Usuario crea un nuevo artículo
    Precondiciones:
        - El usuario debe estar registrado en el sistema
    Detalle:
    - El usuario ingresa su nombre de usuario y contraseña
    - El usuario accede a su cuenta
    - El usuario ingresa a "Crear artículo"
    - El usuario introduce el título y cuerpo del artículo
    - El usuario selecciona una categoría para el artículo
    - El usuario publica el artículo
        

## Proyecto construido con: 
    Python 3.12.4
    Flask 3.0.3

## Pasos para la instalación:
    1° Clonar el proyecto en una ubicación de su comodidad.
    2° Abrir una consola (powershell o terminal del IDE).
    3° Ubicarse en la raiz del proyecto.
    4° Crear entorno virtual usando venv "python -m venv venv".
    5° Activar el entorno virtual "venv\Scripts\activate".
    6° Instalar las dependencias del archivo requirements.txt "pip install requirements.txt".
    7° Ejecutar comando "flask run" en su consola.

    Ahora estará listo para consumir la API.

## Endpoints disponibles:
### User:
#### List Users
    Verb: GET
    Path: /users/
    Respuesta esperada:
    [
    {
        "email": "whiskers@email.com",
        "id": 1,
        "passwd": "whiskers2233",
        "username": "theleftwhiskers"
    },
    {
        "email": "coffecup2572@email.com",
        "id": 2,
        "passwd": "passwd",
        "username": "coffecup2572"
    }
    ]

#### Create User
    Verb: POST
    Path: /users/new
    Payload:
    {
        "username":"newuser",
        "email":"example@email.com",
        "passwd":"Newuserp4$$wd"
    }
    Respuesta esperada:
    {
        "email": "example@email.com",
        "id": 5,
        "passwd": "passwd",
        "username": "newuser"
    }

#### Edit Username
    Verb: PUT
    Path: /users/editUsername/1
    Payload:
    {
        "username":"theleftwhiskers"
    }
    Respuesta esperada:
    {
        "email": "whiskers@email.com",
        "id": 1,
        "username": "theleftwhiskers"
    }

#### Edit Email
    Verb: PUT
    Path: /users/editEmail/1
    Payload:
    {
        "email":"whiskers@email.com"
    }
    Respuesta esperada:
    {
        "email": "whiskers@email.com",
        "id": 1,
        "username": "theleftwhiskers"
    }
#### Edit Password
    Verb: PUT
    Path: /users/editPasswd/1
    Payload:
    {
        "passwd":"whiskers2233"
    }
    Respuesta esperada:
    {
        "email": "whiskers@email.com",
        "id": 1,
        "passwd": "whiskers2233",
        "username": "theleftwhiskers"
    }

#### Delete User
    Verb: DELETE
    Path: /users/delete/3
    Respuesta esperada:
    {
        "Message": "User deleted successfully"
    }

### Category:
#### List category
    Verb: GET
    Path: /category/
    Respuesta esperada:
    [
    {
        "category": "fitness",
        "id": 1
    },
    {
        "category": "Deportes",
        "id": 2
    },
    {
        "category": "Belleza y cuidado",
        "id": 3
    },
    {
        "category": "Viajes",
        "id": 4
    },
    {
        "category": "Ocio",
        "id": 5
    }
    ]
#### Create category
    Verb: POST
    Path: /category/new
    Payload:
    {
        "category":"Ocio"
    }
    Respuesta esperada:
    {
        "category": "Ocio",
        "id": 5
    }

### Article:
#### List Articles
    Verb: GET
    Path: /articles/
    Respuesta esperada:
    [
    {
        "artContent": "3 weeks ago started my new hell",
        "artDatePosted": "Tue, 06 Aug 2024 20:43:07 GMT",
        "artDateUpdate": "Tue, 06 Aug 2024 22:43:29 GMT",
        "artTitle": "My fitness journey",
        "category_id": 1,
        "id": 1,
        "user_id": 1
    },
    {
        "artContent": "I went by plain.",
        "artDatePosted": "Mon, 12 Aug 2024 23:37:06 GMT",
        "artDateUpdate": "Mon, 12 Aug 2024 23:37:06 GMT",
        "artTitle": "My journey to the olimpics",
        "category_id": 2,
        "id": 3,
        "user_id": 1
    },
    {
        "artContent": "cookies will make you win.",
        "artDatePosted": "Mon, 12 Aug 2024 23:39:16 GMT",
        "artDateUpdate": "Mon, 12 Aug 2024 23:39:16 GMT",
        "artTitle": "The diet that make me win",
        "category_id": 2,
        "id": 4,
        "user_id": 1
    },
    {
        "artContent": "i washed my face every day .",
        "artDatePosted": "Mon, 12 Aug 2024 23:46:13 GMT",
        "artDateUpdate": "Mon, 12 Aug 2024 23:46:13 GMT",
        "artTitle": "My journey to a clean face",
        "category_id": 3,
        "id": 6,
        "user_id": 2
    }
    ]

#### Create Articles
    Verb: POST
    Path: /articles/new
    Payload: 
    {
        "artContent": "Im still thinking.",
        "artTitle": "My excercise plan",
        "category_id": 4,
        "user_id": 2
    }
    Respuesta esperada:
    {
        "artContent": "Im still thinking.",
        "artDatePosted": "Tue, 13 Aug 2024 03:01:58 GMT",
        "artDateUpdate": "Tue, 13 Aug 2024 03:01:58 GMT",
        "artTitle": "My excercise plan",
        "category_id": 4,
        "id": 10,
        "user_id": 2
    }

#### Edit Article
    Verb: PUT
    Path: /articles/editArticle/1
    Payload:
    {
        "artTile":"My long fitness journey",
        "artContent":"3 weeks ago started my new hell"
    }
    Respuesta esperada:
    {
        "artContent": "3 weeks ago started my new hell",
        "artDatePosted": "Tue, 06 Aug 2024 20:43:07 GMT",
        "artDateUpdate": "Tue, 13 Aug 2024 03:05:03 GMT",
        "artTitle": "My fitness journey",
        "category_id": 1,
        "id": 1,
        "user_id": 1
    }
#### Search by word
    Verb: POST
    Path: /articles/search
    Payload:
    {
        "word":"journey"
    }
    Respuesta Esperada:
    [
    {
        "artContent": "3 weeks ago started my new hell",
        "artDatePosted": "Tue, 06 Aug 2024 20:43:07 GMT",
        "artDateUpdate": "Tue, 13 Aug 2024 03:05:03 GMT",
        "artTitle": "My fitness journey",
        "category_id": 1,
        "id": 1,
        "user_id": 1
    },
    {
        "artContent": "I went by plain.",
        "artDatePosted": "Mon, 12 Aug 2024 23:37:06 GMT",
        "artDateUpdate": "Mon, 12 Aug 2024 23:37:06 GMT",
        "artTitle": "My journey to the olimpics",
        "category_id": 2,
        "id": 3,
        "user_id": 1
    },
    {
        "artContent": "i washed my face every day .",
        "artDatePosted": "Mon, 12 Aug 2024 23:46:13 GMT",
        "artDateUpdate": "Mon, 12 Aug 2024 23:46:13 GMT",
        "artTitle": "My journey to a clean face",
        "category_id": 3,
        "id": 6,
        "user_id": 2
    }
    ]
#### Search by category & Word
    Verb: POST
    Path: /articles/searchByCategory
    Payload:
    {
        "word":"plan",
        "artCategory":"1"
    }
    Respuesta esperada:
    [
    {
        "artContent": "I only eat cookies.",
        "artDatePosted": "Mon, 12 Aug 2024 23:33:51 GMT",
        "artDateUpdate": "Mon, 12 Aug 2024 23:33:51 GMT",
        "artTitle": "My diet plan",
        "category_id": 1,
        "id": 2,
        "user_id": 2
    },
    {
        "artContent": "Im still thinking.",
        "artDatePosted": "Tue, 13 Aug 2024 00:18:55 GMT",
        "artDateUpdate": "Tue, 13 Aug 2024 00:18:55 GMT",
        "artTitle": "My excercise plan",
        "category_id": 1,
        "id": 9,
        "user_id": 2
    }
    ]

#### Delete Article
    Verb: DELETE
    Path: /articles/delete/8
    Respuesta esperada:
    {
        "Message": "Article deleted successfully"
    }
### Comments:
#### List comments
    Verb: GET
    Path: /comments
    Respuesta esperada:
    [
    {
        "article_id": 1,
        "body": "que buen articulo!",
        "datePosted": "Tue, 06 Aug 2024 20:58:58 GMT",
        "id": 1,
        "user_id": 1
    },
    {
        "article_id": 1,
        "body": "Me motiva a empezar mi propio viaje",
        "datePosted": "Tue, 13 Aug 2024 03:19:06 GMT",
        "id": 2,
        "user_id": 2
    }
    ]
#### Create comments
    Verb: POST
    Path: /comments/new
    Payload:
    {
        "body":"Me motiva a empezar mi propio viaje",
        "user_id":"2",
        "article_id":"1"
    }
    Respuesta esperada:
    {
        "article_id": 1,
        "body": "Me motiva a empezar mi propio viaje",
        "datePosted": "Tue, 13 Aug 2024 03:19:06 GMT",
        "id": 2,
        "user_id": 2
    }
#### Delete comments
    Verb: DELETE
    Path: /comments/delete/2
    Respuesta esperada:
    {
        "Message": "Comment deleted successfully"
    }
