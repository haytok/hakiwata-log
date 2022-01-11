.PHONY: mistake-build
mistake-build:
	docker-compose -f docker-compose.yml -f docker-compose.mistake.yml build

.PHONY: mistake-up
mistake-up:
	docker-compose -f docker-compose.yml -f docker-compose.mistake.yml up

.PHONY: mistake-down
mistake-down:
	docker-compose -f docker-compose.yml -f docker-compose.mistake.yml down

.PHONY: correct-build
correct-build:
	docker-compose -f docker-compose.yml -f docker-compose.correct.yml build

.PHONY: correct-up
correct-up:
	docker-compose -f docker-compose.yml -f docker-compose.correct.yml up

.PHONY: correct-down
correct-down:
	docker-compose -f docker-compose.yml -f docker-compose.correct.yml down
