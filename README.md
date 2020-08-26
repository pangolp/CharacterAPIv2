# Character API v2

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
