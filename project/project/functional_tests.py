from selenium import webdriver

def test_body():
	browser = webdriver.Firefox()
	browser.get("http://dev.sodaasu.com/slowergram")
	body = browser.find_element_by_tag_name('body')
	assert 'SlowerGram' in body.text
	browser.quit()

def main():
	test_body()

if __name__ == "__main__":
    main()
