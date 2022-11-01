bash:
	docker compose -f docker-compose.yml run --rm api bash

build:
	docker compose -f docker-compose.yml build

up:
	docker compose -f docker-compose.yml up

down:
	docker compose -f docker-compose.yml down

run:
	docker run --env-file .env -p 80:80 --rm -it  seyes-api:latest