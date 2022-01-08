.PHONY: build
build:
	@echo build
	docker build -t nginx-20220109 .

.PHONY: up
up:
	@echo up
	docker run --rm -p 81:80 --name nginx-20220109 nginx-20220109

.PHONY: down
down:
	@echo down
	docker stop nginx-20220109
