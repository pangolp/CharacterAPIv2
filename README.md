# Character API v2

![character_example](https://user-images.githubusercontent.com/2810187/91328383-3c8d5b00-e79d-11ea-87b7-ff89f20248c9.png)

1. GET /character/<id>/
2. POST /character/<id>/rating/

### Docker
```
docker-compose run web python src/manage.py migrate
docker-compose build
docker-compose up
```

### Limpiar __pycache__ del proyecto.

```
find . -type d -name __pycache__ -exec rm -r {} \+
```
