# stockscraper
scrape latest stock prices from 'www.duniainvestasi.com' and send notification through email if the stock prices fall below certain value. upload it as a function in AWS Lambda. you can make it run daily using cloudwatch event trigger

# How To Install
- download the script
- start python 3.7 virtual environment in the directory
- pip install beautifulsoup and request in virtual environment
- move lambda_function.py to lib/python3.7/site-packages
- zip all files in the lib/python3.7/site-packages and upload it to AWS lambda function
