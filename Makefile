help:
	@echo "help		-- print this help"
	@echo "build-dev	-- builds docker stack for development"
	@echo "build-prod	-- builds docker stack for production"
	@echo "clean-dev 	-- remove development containers"
	@echo "clean-prod	-- remove production containers"
	@echo "createdb	-- create inital DB"
	@echo "dockershell 	-- opens docker /bin/bash"
	@echo "migrations 	-- make Django migrations"
	@echo "ps-dev 		-- prints development containers status"
	@echo "ps-prod 	-- prints production containers status"
	@echo "pyshell 	-- opens python shell"
	@echo "rebuildb	-- rebuilds inital DB"
	@echo "stop-dev  	-- stops development stack"
	@echo "stop-prod 	-- stops production stack"
	@echo "up-dev		-- starts development stack"
	@echo "up-prod 	-- starts production stack"

RUN=docker-compose exec trest
COMPOSE_PROD=docker-compose -f docker-compose.prod.yml
RUN_PROD=${COMPOSE_PROD} exec trest
MANAGE=${RUN} python manage.py

build-dev:
	docker-compose build

build-prod:
	${COMPOSE_PROD} build

up-dev:
	docker-compose up -d
	${MANAGE} migrate
	${MANAGE} runserver 0:8000

up-prod:
	${COMPOSE_PROD} up -d

stop-dev:
	docker-compose stop

stop-prod:
	${COMPOSE_PROD} stop

ps-dev:
	docker-compose ps

ps-prod:
	${COMPOSE_PROD} ps

clean-dev:
	docker-compose down

clean-prod:
	${COMPOSE_PROD} down

dockershell:
	${RUN} /bin/bash

createdb:
	${MANAGE} db create

rebuilddb:
	${MANAGE} db rebuild

migrations:
	${MANAGE} makemigrations

pyshell:
	${MANAGE} shell

.PHONY: help build-dev
