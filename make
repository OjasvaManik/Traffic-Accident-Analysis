install:
	pip install -r requirements.txt

run:
	python main.py

clean:
	rm -rf data/processed/*.csv
