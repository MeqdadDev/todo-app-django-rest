# ToDo App using Django REST Framework

This is an API for a Todo app built with Django REST Framework (DRF).

### Data Models:

* Category: id, title
* TodoTask: id, title, description, due date, tags, category



## API Reference

### Registration and Login
#### User Registration

```http
  POST /todo/register
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required** |
| `email`      | `string` | **Required** |
| `password`      | `string` | **Required** |

Body Example:
```
{
    "username": "meqdad",
    "email": "me@meqdad.me",
    "password": "AddYourPassHere"
}
```

#### User Login
```http
  POST /todo/login
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required** |
| `password`      | `string` | **Required** |

Body Example:
```
{
    "username": "meqdad",
    "password": "PutYourAddedPassHere"
}
```

Response Sample:
```
{
    "expiry": "2022-04-30T07:05:04.536584Z",
    "token": "026e2a8bd276aa1915361a3efc97d883229eba3ec79d98e32f39d13b619772fd"
}
```

#### User Logout
```http
  POST /todo/logut
```


### Categories
#### Get all categories

```http
  GET /todo/all_categories
```

Response Sample:
```
[
    {
        "id": 1,
        "title": "Consultation"
    },
    {
        "id": 2,
        "title": "Learning"
    },
    {
        "id": 3,
        "title": "Sport"
    }
]
```

#### Add Category

```http
  POST /todo/category_create
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` | **Required**. Title of category |

Body Example:
```
{
    "title": "Sport"
}
```

#### Edit Category

```http
  PUT /todo/category_edit/<int:id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Optional**. ID of category |
| `title`      | `string` | **Required**. Title of category |

Body Example:
```
{
    "title": "Gaming"
}
```

#### Delete Category

```http
  DELETE /todo/category_delete/<int:id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. ID of category |


#### List Tasks for Specific Category

```http
  GET /todo/category_tasks/<int:id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. ID of category |

Response Sample where id=6:
```
[
    {
        "id": 4,
        "title": "Call of Duty",
        "description": "Play time on Call of Duty game",
        "due_date": "2022-04-29T20:20:41Z",
        "tags": "",
        "category": 6
    },
    {
        "id": 5,
        "title": "Super Mario",
        "description": "Play time on Super Mario game",
        "due_date": "2022-04-29T20:21:15Z",
        "tags": "",
        "category": 6
    }
]
```


### Tasks
#### Get all Todo Tasks

```http
  GET /todo/all_tasks
```

Response Sample:
```
[
    {
        "id": 1,
        "title": "Learning English Lang.",
        "description": "Learning English Language",
        "due_date": "2022-04-29T18:00:00Z",
        "tags": "education",
        "category": 2
    },
    {
        "id": 2,
        "title": "Morning Workout",
        "description": "Play some workouts at the morning",
        "due_date": "2022-04-29T18:00:00Z",
        "tags": "lifestyle",
        "category": 3
    }
]
```

#### Add Todo task

```http
  POST /todo/task_create
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` | **Required**. |
| `description`      | `integer` | **Required**. |
| `due_date`      | `dateTime` | **Required**. |
| `tags`      | `string` | **Optional**. |
| `category`      | `int` | **Required**. |

Body Example:
```
{
        "title": "Reading a book",
        "description": "Reading a book about Software Development",
        "due_date": "2022-04-30T11:30:00Z",
        "tags": "learning",
        "category": 2
}
```

#### Edit Todo task

```http
  PUT /todo/task_edit/<int:id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` | **Required**. |
| `description`      | `integer` | **Required**. |
| `due_date`      | `dateTime` | **Required**. |
| `tags`      | `string` | **Optional**. |
| `category`      | `int` | **Required**. |

Body Example:
```
{
        "title": "Reading a book",
        "description": "Reading a book about Software Development",
        "due_date": "2022-04-30T11:30:00Z",
        "tags": "learning",
        "category": 2
}
```

#### Delete Todo Task

```http
  DELETE /todo/task_delete/<int:id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. ID of task |


#### List Task Details

```http
  DELETE /todo/task_details/<int:id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. ID of task |


Response Sample where id=4:
```
[
    {
        "id": 4,
        "title": "Call of Duty",
        "description": "Play time on Call of Duty game",
        "due_date": "2022-04-29T20:20:41Z",
        "tags": "",
        "category": 6
    }
]
```
