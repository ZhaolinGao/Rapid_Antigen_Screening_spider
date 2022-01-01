# Rapid_Antigen_Screening_spider

This repository is used to fetch available Rapid Antigen Screening tests in Shoppers.

## Enviroment Requirement

`python 3.8`
`selenium`

## Browser WebDriver Requirement

Chrome : https://chromedriver.chromium.org/downloads

Firefox : https://github.com/mozilla/geckodriver/releases

Safari : https://webkit.org/blog/6900/webdriver-support-in-safari-10/

Download the corresponding WebDriver and put it in the directory of main.py

## Parameters

- `range_km` The maximum range of shoppers in km. Default 20km.
- `location` The address you want to search around.
- `month` The month to get test. Default 1.
- `day` The day to get test. Default 1.

## Execute

The program is going to search all the shoppers within the range of the address for a time slot before and on the month/day. It will automatically refresh the webpage after each search. After it finds a suitable time slot, it will select it and play an alarm sound.
