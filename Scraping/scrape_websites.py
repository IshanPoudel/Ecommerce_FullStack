#Use bs4 and Selenium to scrape data prices and have them store it in a mongoDB instance. 

from bs4 import BeautifulSoup


chrome_options = Options()  # Instantiate an options class for the selenium webdriver
# chrome_options.add_argument("--headless")  # So that a chrome window does not pop up
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
time.sleep(10)

url = "https://www.amazon.com/s?k=kindle"

driver.get(url)
time.sleep(20)

html_text = BeautifulSoup(html_text , 'htmll.parser')
print(html_text)