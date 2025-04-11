default:
	@cat makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r requirements.txt

ygainers.html:	
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html

clean:
	rm ygainers.* || true
	rm wsjgainers.* || true

ygainers.csv: ygainers.html
	. env/bin/activate; python -c "import pandas as pd; raw = pd.read_html('ygainers.html'); raw[0].to_csv('ygainers.csv')"

wjsgainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=500 https://www.wsj.com/market-data/stocks/us/movers > wjsgainers.html

wjsgainers.csv: wjsgainers.html
	. env/bin/activate; python -c "import pandas as pd; raw = pd.read_html('wjsgainers.html'); raw[0].to_csv('wjsgainers.csv')"

ygainers_norm.csv:
	python3 bin/normalize_csv.py ygainers.csv
lint:
	pylint bin/normalize_csv.py
	PYTHONPATH=. pylint bin/get_gainer.py
test:
	make lint
	pytest -vv tests
	pytest tests/test_environment.py
	PYTHONPATH=. pytest tests/test_wsj_gainers.py
	PYTHONPATH=. pytest tests/test_yahoo_gainers.py
	PYTHONPATH=. pytest tests/test_factory.py

gainers:
	PYTHONPATH=. python3 get_gainer.py $(SRC)

