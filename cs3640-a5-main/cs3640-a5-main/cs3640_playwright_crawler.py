# Dependencies
import requests as req
from bs4 import BeautifulSoup as bs
from playwright.sync_api import sync_playwright
import time
import csv

# Timeout settings
REQUEST_TIMEOUT = 10  # seconds
BROWSER_TIMEOUT = 30  # seconds

# Define the URL of the web page you want to measure
# url = "https://yahoo.com"

# Create a function to calculate the page load time and count trackers
def calculate_page_load_time_with_trackers(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            # Set browser timeout
            page.set_default_timeout(BROWSER_TIMEOUT * 1000)

            # Record the start time
            start_time = time.time()
            
            # Navigate to the URL
            page.goto(url, timeout=BROWSER_TIMEOUT * 1000)
            
            # Wait for the page to load completely
            page.wait_for_load_state("networkidle")
            
            # Record the end time
            end_time = time.time()
            
            # Calculate the page load time
            load_time = end_time - start_time
            
            # Get the page content for tracker analysis
            page_content = page.content()
            
            # Count the number of tracker elements using BeautifulSoup (or your preferred method)
            tracker_count = 0
            tracker_count += count_page_trackers(page_content)
            tracker_count += count_trackers(url)

            browser.close()
            
            return load_time, tracker_count
    except Exception as e:
        print(f"An error occurred during {url} loading: {e}")
        return None, None

# Function to count trackers using BeautifulSoup (or your preferred method)
def count_page_trackers(page_content):
    soup = bs(page_content, "html.parser")
    
    # Define patterns or elements that represent trackers (e.g., <img> tags with specific src attributes)
    tracker_patterns = [
        {"tag": "img", "attribute": "src", "pattern": "tracker.com"},
        # Add more patterns as needed
    ]
    
    tracker_count = 0
    
    for pattern in tracker_patterns:
        elements = soup.find_all(pattern["tag"])
        for element in elements:
            if pattern["attribute"] in element.attrs and pattern["pattern"] in element.attrs[pattern["attribute"]]:
                tracker_count += 1
    
    return tracker_count

def count_trackers(url):
    # Fetch the webpage content
    response = req.get(url)
    
    if response.status_code == 200:
        # Parse the HTML content
        soup = bs(response.content, 'html.parser')
        
        # Find elements related to trackers (e.g., script tags, img tags, etc.)
        tracker_elements = soup.find_all(['script', 'img', 'iframe', 'link'])
        
        # Count the number of tracker elements
        num_trackers = len(tracker_elements)
        
        return num_trackers
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")
        return None

def write_to_csv(result_filename, results):
        with open(result_filename, 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            # csvwriter.writerow(['Website', 'Number of Trackers', 'Website Load Time (Latency)'])
            csvwriter.writerows(results)

def main():
    
    results = []
    urls_filename = "top_1000_urls.txt"
    result_filename = "playwright_crawler_results.csv"

    try:
        with open(urls_filename, 'r') as urls_file:
            num = 1
            for url in urls_file:
                url = 'http://' + url.strip()
                if url:
                    print(f"{url}, {num}")
                    num += 1
                    latency, num_trackers = calculate_page_load_time_with_trackers(url)
                    if latency is not None and num_trackers is not None:
                        results.append([url, num_trackers, latency])
                    if num % 10 == 0:
                        write_to_csv(result_filename, results)

    except IOError as e:
        print(f"File error: {e}")

if __name__ == "__main__":
    main()
    print('done')
