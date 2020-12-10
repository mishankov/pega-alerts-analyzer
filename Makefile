install-api:
	( \
		python3 -m venv src/api/venv; \
		. src/api/venv/bin/activate; \
		pip3 install --upgrade pip; \
		pip3 install -r src/api/requirements.txt; \
	)

install-client:
	(echo "Install client")

install: install-api install-client

run-api-dev:
	( \
		. src/api/venv/bin/activate; \
		uvicorn --app-dir src/api/ --reload main:app; \
	)

run-api:
	( \
		. src/api/venv/bin/activate; \
		gunicorn --chdir src/api/ main:app -k uvicorn.workers.UvicornWorker; \
	)

run-client-dev:
	vue serve src/client/App.vue

build-local:
	docker build . -t gpetb

black:
	(\
		. src/api/venv/bin/activate; \
		black src/api; \
	)

commit-all: black
ifdef m
	git add .
	git commit -m "${m}"
endif

push-all: black
ifdef m
	git add .
	git commit -m "${m}"
	git push
endif
