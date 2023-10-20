install:
	# install dependencies
	pip install --upgrade pip &&\
		pip --default-timeout=1000 install -r requirements/base.txt 
format:
	# format python code with black
	find . -name "*.py" ! -path "./venv/*" | xargs black
lint:
	# check code syntaxes
	pylint --disable=R,C  api/*.py

populate:
	# populate sheet1 with grocery_transactions data
	python3 cli.py main --spread_sheet=grocery_transactions1 --csv_data_path=./data/grocery_transactions.csv --worksheet_name=sheet2 --email=bestnyah7@gmail.com