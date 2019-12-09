### Installation (for python 3.7)

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

### Development

```bash
python manage.py runserver
```

### Description and Examples

For each person the API returns all attributes from the model + some other related objects. Related objects included:

    - `relatives` - array with all the relatives of this person
    - `farmer` - farmer object associated with this person, if this person is not a farmer this field is not included
    - `fieldman` - fieldman object associated with this person, if this person is not a fieldman this field is not included

For each farmer the API returns all attributes from the model, for `person` related object, only the id is included, not the whole `person` object.

Example response for the request GET `/api/persons/?format=json`

```json
[
    {
        "id": 1,
        "relatives": [
            {
                "id": 2,
                "relation_type": "WR",
                "person": 2
            }
        ],
        "farmer": {
            "id": 5,
            "farmer_code": "us1",
            "person": 1
        },
        "fieldman": {
            "id": 1,
            "person": 1
        },
        "first_name": "John",
        "middle_name": "Walter",
        "last_name": "Doe",
        "age": "52",
        "gender": "male"
    },
    {
        "id": 2,
        "relatives": [
            {
                "id": 1,
                "relation_type": "HR",
                "person": 1
            }
        ],
        "farmer": {
            "id": 6,
            "farmer_code": "us2",
            "person": 2
        },
        "first_name": "Hellen",
        "middle_name": "Marie",
        "last_name": "Doe",
        "age": "50",
        "gender": "female"
    }
]
```

Example response for the request GET `/api/persons/1/?format=json`

```json
{
    "id": 1,
    "relatives": [
        {
            "id": 2,
            "relation_type": "WR",
            "person": 2
        }
    ],
    "farmer": {
        "id": 5,
        "farmer_code": "us1",
        "person": 1
    },
    "fieldman": {
        "id": 1,
        "person": 1
    },
    "first_name": "John",
    "middle_name": "Walter",
    "last_name": "Doe",
    "age": "52",
    "gender": "male"
}
```

Example response for the request GET `/api/farmers/?format=json`

```json
[
    {
        "id": 5,
        "farmer_code": "us1",
        "person": 1
    },
    {
        "id": 6,
        "farmer_code": "us2",
        "person": 2
    }
]
```

Example response for the request GET `/api/farmers/5/?format=json`

```json
{
    "id": 5,
    "farmer_code": "us1",
    "person": 1
}
```
