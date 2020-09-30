# MakeMyTrip-Flight-Booking with Selenium

## Features of the script

* Grabs the from,to city and puts the given input in the boxes and selects the date from the Departure Calender
* Selects the cheapest flight among all the flights
* According to input checks the insurance checkbox to yes or no
* Fills the tarveller details and proceeds to payment page where debit card details are filled

## Selenium Documentation- Python
[Selenium docs](
https://selenium-python.readthedocs.io/api.html
)

## Download chrome driver and check chrome version
[Chrome-driver](https://chromedriver.chromium.org/downloads)

chrome version: Settings-> About

## Setup
#### make a folder
```
mkdir amazon_web_scrappe
cd MMT
```
#### Setup a Virtual Enviornment
```
pthon -m venv venev
source venv/bin/activate
```
#### Install the requirements
```
pip install -r requirement.txt
```

#### Run the script
```
python mmt.py
```
