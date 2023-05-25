SHELL=/bin/sh

source:
	source     ~/envs/certus_back/bin/activate
run:
	virtualenv --python python3 \
    	~/envs/certus_back	
	pip install -r requirements.txt
	python main.py

gce:
	gcloud app create
	gcloud app deploy app.yaml \
		--project app-puntos-285220
gcd:
	gcloud app deploy app.yaml \
		--project upbeat-stratum-349012

