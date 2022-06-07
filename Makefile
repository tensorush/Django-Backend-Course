task-1:
	docker build -t task-1 ./1-LRU-Cache/ && docker run -it task-1

task-2:
	docker-compose -f ./2-Nginx-Gunicorn-Servers/docker-compose.yml up --build

tasks-3-9:
	docker-compose -f ./3-9-Django-Project/docker-compose.yml --env-file ./3-9-Django-Project/.env up --build

test: tasks-3-9
	docker exec 3-9-django-project-django_application-1 python3 ./manage.py test

store: tasks-3-9
	docker exec 3-9-django-project-django_application-1 python3 ./store_file.py
