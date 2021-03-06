install-api:
	( \
		python3 -m venv api/venv; \
		. api/venv/bin/activate; \
		pip3 install --upgrade pip; \
		pip3 install -r api/requirements.txt; \
	)

install-client:
	npm install --prefix client/

install: install-api install-client

run-api-dev:
	( \
		. api/venv/bin/activate; \
		api/venv/bin/uvicorn --app-dir api/src/ --reload main:app; \
	)

run-api:
	( \
		. api/venv/bin/activate; \
		gunicorn --chdir api/src/ main:app -k uvicorn.workers.UvicornWorker; \
	)

run-client-dev:
	npm run serve --prefix client/

build-local:
	docker build . -t gpetb

lint-api:
	(\
		. api/venv/bin/activate; \
		api/venv/bin/black api; \
	)

lint-client:
	npm run lint --prefix client

lint: lint-api lint-client

commit-all: lint
ifdef m
	git add .
	git commit -m "${m}"
endif

push-all: commit-all
ifdef m
	git push
endif
