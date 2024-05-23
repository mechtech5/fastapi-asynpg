## Essentials

#### Run Project

```
uvicorn app.main:app --reload
```

#### When new packages are installed

```
poetry install
```

#### Alembic: to generate new revision

```
alembic -c alembic_local.ini revision --autogenerate -m "Your message"
alembic -c alembic_dev.ini revision --autogenerate -m "Your message"
alembic -c alembic_prod.ini revision --autogenerate -m "Your message"
alembic -c alembic_uat.ini revision --autogenerate -m "Your message"
```

#### Alembic: to update changes in DB

```
alembic -c alembic_local.ini upgrade head
alembic -c alembic_dev.ini upgrade head
alembic -c alembic_prod.ini upgrade head
alembic -c alembic_uat.ini upgrade head
```
