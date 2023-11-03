#Complain


* Docker Commands
```
docker compose up -d
docker compose down
docker compose ps
docker compose logs -f
docker exec -it complain-web-1 bash
docker exec -it complain-db-1 bash
```

*If you unable to delete user and getting "The above exception (relation "allauth_socialaccount" does not exist LINE 1: ...te_joined", "user_app_newuser"."weight_unit" FROM "allauth_s... ^ ) was the direct cause of the following exception:" error then run command which mentioned below

```
python manage.py makemigrations allauth
python manage.py migrate allauth

```

