import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
#driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
# options = FirefoxOptions()
# options.add_argument("--headless")

driver = webdriver.Firefox()
driver.get("https://ocr.sanskritdictionary.com/")
input_folder_path = "/home/mangal/Tesseract/ImageUpload/Input"
output_folder_path = "//home/mangal/Tesseract/ImageUpload/Output"

image_paths = list(os.walk(input_folder_path))
print("path")
print(image_paths)
print()

for path in sorted(image_paths[0][2]):
    driver.execute_script("document.querySelector('input[type=file]').style.display = 'block';")

    # Find the file input element
    file_input = driver.find_element(By.CSS_SELECTOR, 'input[type=file]')
    file_input.send_keys(f"{image_paths[0][0]}/{path}")
    import time
    # time.sleep(5)
    wait = WebDriverWait(driver, 60)
    iframe = wait.until(EC.visibility_of_element_located((By.ID, 'tinymcetext_ifr')))
    # iframe = driver.find_element(By.CSS_SELECTOR, 'iframe #tinymcetext_ifr')
    driver.switch_to.frame(iframe)

    paragraph = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    print(path)
    with(open(f"{output_folder_path}/{path}.txt", 'a', encoding='utf-8')) as f:
        f.write(paragraph.text)

    driver.switch_to.default_content()
    time.sleep(5)
    li_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'hasImage')))
    link_element = li_element.find_element(By.TAG_NAME, 'a')

    href_attribute = li_element.get_attribute('href')
    link_element.click()


    time.sleep(2)

driver.close()
