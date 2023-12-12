from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
import csv
import json

def create_driver(headless=True):
    options = Options()

    #Get rid of console messages
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    options.add_argument('--disable-dev-shm-usage')  
    options.add_argument('--no-sandbox')  
    options.add_argument('--disable-gpu')  
    options.add_argument('--disable-infobars')  
    options.add_argument('--disable-extensions')  
    options.add_argument('--log-level=3')
    if headless:
        options.add_argument('--headless')  
    options.add_argument('--ignore-certificate-errors')  
    chrome_driver_manager = ChromeDriverManager()
    return webdriver.Chrome(service=Service(chrome_driver_manager.install()), options=options)

def cookieTracker(link, delay=2, timeout=15):
    numCookies = None
    total_size = None
    driver = create_driver(headless=True)  
    try:
        driver.set_page_load_timeout(timeout)
        driver.get(link)

        # Wait for a few seconds to allow cookies to load before retriving
        time.sleep(delay) 

        cookies = driver.get_cookies()
        numCookies = len(cookies)
        total_size = sum(len(json.dumps(cookie)) for cookie in cookies)
        print(f"Number of cookies for {link}: {len(cookies)}, Total size of cookies: {total_size} bytes")
    except TimeoutException:
        print(f"{link} failed due to timeout")
        driver.quit()
        return None, None
    except Exception as e:
        print(f"{link} failed due to {e}")
        driver.quit()
        return None, None
    finally:
        driver.quit()
        return numCookies, total_size

#Method to write the results to a csv file
def write_to_csv(result_filename, results):
        with open(result_filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Website', 'Number of Cookies', 'Total bytes used by cookies'])
            csvwriter.writerows(results)


def main():
    results = []
    urls_filename = "top_1000_urls.txt"
    result_filename = "test_selenium_cookies.csv"

    try:
        with open(urls_filename, 'r') as urls_file:
            num = 1
            for url in urls_file:
                url = 'http://' + url.strip()
                if url:
                    print(f"{url}, {num}")
                    num += 1
                    numCookies, totalSize = cookieTracker(url)
                    if numCookies is not None and totalSize is not None:
                        results.append([url, numCookies, totalSize])
                    if num % 10 == 0:
                        write_to_csv(result_filename, results)

    except IOError as e:
        print(f"File error: {e}")

if __name__ == "__main__":
    main()
