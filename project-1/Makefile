install:
	# install dependencies
	pip install --upgrade pip &&\
		pip --default-timeout=1000 install -r requirements/base.txt 
format:
	# format python code with black
	find . -name "*.py" ! -path "./venv/*" | xargs black
lint:
	# check code syntaxes
	find . -name "*.py" ! -path "./venv/*" |  xargs pylint --disable=R,C  

populate:
	# populate sheet1 with grocery_transactions data
	python3 cli.py --spread_sheet=ny_taxi_data \
		 --worksheet_name=taxi_2023_2 \
		 --email=bestnyah7@gmail.com \
		 --year=2023 \
		 --month=3 

bash:
	# run extract bash script 
	chmod +x extract.sh &&\
		./extract.sh 2023 3

test:
	# run unit and integration tests
	pytest -s ./tests/unit/test_gspread_utility.py	


all: 
	# run in required order
	install format lint test populate 