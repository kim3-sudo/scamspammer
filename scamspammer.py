#import requests
import string
import random
import json
import time
import threading
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.comon.action_chains import ActionChains


url = 'https://www.ultimateconsumerdeals.com/discountoffer/v2/checkout.php'

edomains = [
    "@gmail.com",
    "@yahoo.com",
    "@protonmail.com",
    "@ultimateconsumerdeals.com",
    "@secure.mail",
    "@we4.gg"
]

months = ["(01)", "(02)", "(03)", "(04)", "(05)", "(06)", "(07)", "(08)", "(09)", "(10)", "(11)", "(12)"]

years = ["2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032"]

addresses = json.loads(open('addresses.json').read())
cities = json.loads(open('cities.json').read())
zips = json.loads(open('zips.json').read())

def generate():
    letters = string.ascii_lowercase
    numbers = string.digits
    first = ''.join(random.choice(letters) for i in range(10))
    last = ''.join(random.choice(letters) for i in range(8))
    email = first.join(random.choice(numbers) for i in range(3))
    email = email + random.choice(edomains)
    phone = ''.join(random.choice(numbers) for i in range(10))
    address = ''.join(random.choice(addresses))
    city = ''.join(random.choice(cities))
    zip = ''.join(random.choice(zips))
    number =  "4007000000270000",
    cvv =  "233",
    month = ''.join(random.choice(months)),
    year = ''.join(random.choice(years))
    return {"first": first, "last": last, "email": email, "phone": phone, "address": address, "city": city, "zip": zip}, {"number": number, "cvv": cvv, "month": month, "year": year}

def sendid(iddict):
    """
    Send requests by idea

    Parameters
    ----------
    iddict : dictionary of strings
        A dictionary of strings with the ID field mappings

    Return
    ------
    None

    """
    driver = webdriver.Chrome(executable_path = 'C:/bin/chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get(url)
    id, card = generate()
    print(id, card)
    driver.find_element(By.ID, (iddict["first"])).send_keys(id["first"])
    driver.find_element(By.ID, (iddict["last"])).send_keys(id["last"])
    driver.find_element(By.ID, (iddict["email"])).send_keys(id["email"])
    driver.find_element(By.ID, (iddict["phone"])).send_keys(id["phone"])
    driver.find_element(By.ID, (iddict["address"])).send_keys(id["address"])
    driver.find_element(By.ID, (iddict["city"])).send_keys(id["city"])
    driver.find_element(By.ID, (iddict["state"])).send_keys("California")
    driver.find_element(By.ID, (iddict["zip"])).send_keys(id["zip"])
    driver.find_element(By.ID, (iddict["cardnumber"])).send_keys(card["number"])
    driver.find_element(By.ID, (iddict["cvv"])).send_keys(card["cvv"])
    driver.find_element(By.ID, (iddict["month"])).send_keys(card["month"])
    driver.find_element(By.ID, (iddict["year"])).send_keys(card["year"])
    driver.find_element(By.ID, (iddict["submit"])).click()
    time.sleep(4)

def sendname(namedict):
    """
    Send requests by idea

    Parameters
    ----------
    namedict : dictionary of strings
        A dictionary of strings with the name field mappings

    Return
    ------
    None

    """
    driver = webdriver.Chrome(executable_path = 'C:/bin/chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get(url)
    id, card = generate()
    print(id, card)
    driver.find_element(By.name, (namedict["first"])).send_keys(id["first"])
    driver.find_element(By.name, (namedict["last"])).send_keys(id["last"])
    driver.find_element(By.name, (namedict["email"])).send_keys(id["email"])
    driver.find_element(By.name, (namedict["phone"])).send_keys(id["phone"])
    driver.find_element(By.name, (namedict["address"])).send_keys(id["address"])
    driver.find_element(By.name, (namedict["city"])).send_keys(id["city"])
    driver.find_element(By.name, (namedict["state"])).send_keys("California")
    driver.find_element(By.name, (namedict["zip"])).send_keys(id["zip"])
    driver.find_element(By.name, (namedict["cardnumber"])).send_keys(card["number"])
    driver.find_element(By.name, (namedict["cvv"])).send_keys(card["cvv"])
    driver.find_element(By.name, (namedict["month"])).send_keys(card["month"])
    driver.find_element(By.name, (namedict["year"])).send_keys(card["year"])
    driver.find_element(By.name, (namedict["submit"])).click()
    time.sleep(4)

def main():
    while True:
        try:
            numthreads = int(input("Enter number of threads to use: "))
            threads = [] # Initialize multithreads
            try:
                # The mapping file tells Python where what the ID or names of the fields are so it can click on the right things
                # Use mappings.json as a guide, leave the keys alone and edit the values
                # Set the values to the ID or name of the field on the scam page
                # For example, if the ID of the first name field is customer_firstname, then set the "first" value to "customer_firstname"
                # That means that line 2 would look like
                #   "first": "customer_firstname"
                mappingfile = str(input("Enter mapping JSON file location: "))
                mappings = json.loads(open(mappingfile).read())
                try:
                    method = int(input("Enter the search method:\n\n1: Search by ID\n2: Search by name"))
                    if method == 1:
                        for i in range(numthreads):
                            t = threading.Thread(target=sendid, args = (mappings))
                            t.daemon = True
                            threads.append(t)
                        for i in range(numthreads):
                            threads[i].start()
                        for i in range(numthreads):
                            threads[i].join()
                    elif method == 2:
                        for i in range(numthreads):
                            t = threading.Thread(target=sendname, args = (mappings))
                            t.daemon = True
                            threads.append(t)
                        for i in range(numthreads):
                            threads[i].start()
                        for i in range(numthreads):
                            threads[i].join()
                    else:
                        raise TypeError
                except TypeError:
                    warnings.warn("Search method entered is not a valid option", RuntimeWarning)
            except:
                warnings.warn("Mapping file not readable", RuntimeWarning)
        except TypeError:
            warnings.warn("Number of threads is not an integer or cannot be typecast to an integer", RuntimeWarning)


if __name__ == "__main__":
    main()
