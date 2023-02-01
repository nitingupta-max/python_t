from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import urllib.parse
driver = None
Link = "https://web.whatsapp.com/"
wait = None

# login to whatsApp


def whatsapp_login():
    global wait, driver, Link
    driver = webdriver.Chrome("/driver/chromedriver") # add chromedriver path here
    wait = WebDriverWait(driver, 20)
    print(" Scan your QR code for WhatsApp web if displayed on screen")
    driver.get(Link)
    driver.maximize_window()
    sleep(15)
    print("QR code scanned")


def send_message(name, msg, count):
    user_group_xpath = '//span[@title = "{}"]'.format(name)
    for retry in range(3):
        try:
            sleep(3)
            wait.until(EC.presence_of_element_located(
                (By.XPATH, user_group_xpath))).click()
            break
        except Exception:
            print("retry:{} {} not found in your contact list".format(retry, name))
            if retry == 2:
                return
    msg_box = driver.find_element(
        "xpath",  '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
    for index in range(count):
        msg_box.send_keys(msg)
        driver.find_element(
            "xpath",  '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
    print("Message send successfully.")


def send_attachment(name, file_name):
    user_group_xpath = '//span[@title = "{}"]'.format(name)
    for retry in range(3):
        try:
            sleep(3)
            wait.until(EC.presence_of_element_located(
                (By.XPATH, user_group_xpath))).click()
            break
        except Exception:
            print("retry:{} {} not found in your contact list".format(retry, name))
            if retry == 2:
                return
    attachment_box = driver.find_element("xpath",  '//div[@title = "Attach"]')
    attachment_box.click()
    attachment = driver.find_element("xpath",
                                     '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    attachment.send_keys(file_name)
    sleep(5)
    send = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span')))
    send.click()
    print("File send successfully.")


if __name__ == "__main__":
    print("Web Page Open")

    # Let us login and Scan
    whatsapp_login()
    send_message("contact_name", "Hello", 2)
    sleep(2)
    send_attachment("contact_name", 'path_of_file')

    print("Completed")
    driver.close()  # Close the Open tab
    driver.quit()
