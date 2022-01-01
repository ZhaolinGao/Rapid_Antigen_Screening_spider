# import module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--range_km', type=float, default=20,
                        help="the maximum range of shoppers in km")
    parser.add_argument('--location', type=str, default="386 Yonge St, Toronto",
                        help="your address")
    parser.add_argument('--month', type=int, default=1,
                        help="month to get test")
    parser.add_argument('--day', type=int, default=1,
                        help="day to get test")
    return parser.parse_args()

if __name__ == '__main__':
	args = parse_args()

	text_to_month = {}
	text_to_month['Jan'] = 1
	text_to_month['Feb'] = 2
	text_to_month['Mar'] = 3
	text_to_month['Apr'] = 4
	text_to_month['May'] = 5
	text_to_month['Jun'] = 6
	text_to_month['Jul'] = 7
	text_to_month['Aug'] = 8
	text_to_month['Sep'] = 9
	text_to_month['Oct'] = 10
	text_to_month['Nov'] = 11
	text_to_month['Dec'] = 12

	# Create the webdriver object. Here the 
	# chromedriver is present in the driver 
	# folder of the root directory.
	driver = webdriver.Chrome()

	# get https://www.geeksforgeeks.org/
	driver.get("https://shoppersdrugmart.medmeapp.com/schedule/groups/Covid-19-Rapid-Screening")
	  
	# Click continue
	driver.implicitly_wait(2)
	button = driver.find_element_by_class_name("MuiButtonBase-root")
	button.click()

	# Enter location
	driver.implicitly_wait(5)
	button = driver.find_element_by_class_name("mapboxgl-ctrl-geocoder--input")
	button.send_keys(args.location)
	driver.implicitly_wait(1)
	button.send_keys(Keys.RETURN)
	driver.implicitly_wait(2)

	# Check distance
	buttons = driver.find_elements_by_class_name("storeSelectionstyles__DistanceContainer-sc-16rd8si-10")
	inrange = 0
	for button in buttons:
		distance = float(button.text.split()[0])
		if distance >= args.range_km:
			break
		inrange += 1

	while True:
		# get time slot
		buttons = driver.find_elements_by_class_name("storeSelectionstyles__CardContainer-sc-16rd8si-2")
		for button in buttons[:inrange]:
			button.click()

			# check dates
			num_dates = 0
			dates = driver.find_elements_by_class_name("schedulingSelectionstyles__DateText-sc-1h2570n-16")
			for date in dates:
				date_split = date.text.split()
				date_month = text_to_month[date_split[0]]
				date_day = int(date_split[1])
				if date_month < args.month:
					num_dates += 1
					continue
				elif date_month == args.month and date_day <= args.day:
					num_dates += 1
					continue
				break

			# check time slots
			slots = driver.find_elements_by_class_name("schedulingSelectionstyles__DateColumn-sc-1h2570n-19 ")
			if len(slots) == 0:
				continue
			available = False
			for i in range(num_dates):
				if slots[i].text:
					available = True
					break

			# reserve
			if available:
				button = driver.find_element_by_class_name("schedulingSelectionstyles__DateTimeCard-sc-1h2570n-20")
				button.click()
				button = driver.find_element_by_class_name("navigationFooterstyles__SubmitButton-sc-uinvu0-2")
				button.click()
				alarm = webdriver.Chrome()
				alarm.get("https://www.youtube.com/watch?v=V-mraEeOHYI")
				button = alarm.find_element_by_class_name("html5-video-player")
				button.click()
				quit()

		driver.refresh()
		alert = driver.switch_to.alert
		alert.accept()

		# Click continue
		driver.implicitly_wait(2)
		button = driver.find_element_by_class_name("MuiButtonBase-root")
		button.click()

		# Enter location
		driver.implicitly_wait(5)
		button = driver.find_element_by_class_name("mapboxgl-ctrl-geocoder--input")
		button.send_keys(args.location)
		driver.implicitly_wait(1)
		button.send_keys(Keys.RETURN)
		driver.implicitly_wait(2)
