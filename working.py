import subprocess
import fileinput

import time
import random
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, timedelta

from workaround import update_executable_path
import os

chromedriver_path = update_executable_path()

executable_path = chromedriver_path
os.system(f"chmod 700 {executable_path}")


def store_current_time():
  with open("time.txt", "w") as file:
    file.write(str(datetime.now()))


def check_time():
  with open("time.txt", "r") as file:
    file_contents = file.read().strip()

  if file_contents:
    stored_time = datetime.strptime(file_contents, '%Y-%m-%d %H:%M:%S.%f')

    # If the stored time is more than 24 hours ago
    if datetime.now() - stored_time > timedelta(hours=24):
      seadra()
    else:
      print("Checking time 24 ghante nhi hue")
  else:
    print("The time.txt file is empty.")
    seadra()


# Function to be called when the stored time is more than 24 hours ago


def seadra():
  print("The stored time is more than 24 hours ago.")
  with open("links.txt", "w") as file:
    file.write("")
  main()


def main():

  url = "https://www.instagram.com/adhipathi_here/?hl=en"
  options = uc.ChromeOptions()

  options = uc.ChromeOptions()
  options.add_argument('--disable-extensions')
  options.add_argument('--disable-popup-blocking')
  options.add_argument('--profile-directory=Default')
  options.add_argument('--disable-plugins-discovery')
  options.add_argument('--start-maximized')

  count = 0
  exit_flag = False
  # driver = uc.Chrome(options=options)
  driver = uc.Chrome(options=options, driver_executable_path=executable_path)
  # driver.get(url)
  wait = WebDriverWait(driver, 20)
  # # wait = WebDriverWait(driver, 10)

  # wait_time = random.uniform(5, 15)
  # time.sleep(wait_time)

  try:
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located(
    #     (By.XPATH, "//span[@class='x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft']")))

    link_element = driver.find_element(
        By.XPATH,
        "//span[@class='x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft']")
    link_element.click()
    # driver.get(
    #     "https://www.dailymotion.com/dm_d9726f3b44285e4df6e33980937290f2")
    driver.get(
        "https://l.instagram.com/?u=https%3A%2F%2Fwww.dailymotion.com%2Fdm_d9726f3b44285e4df6e33980937290f2&e=AT3F4-tKngod63Up6ZnhpZyF2UQ-sLd5QL_K1J2S92XloHlB0bS_o8Df3SxVw-REjBJCvMMTUoInf1ndFjUUysv1tR_y_8_Cqf2OjmfWf2J9_mSk"
    )
    time.sleep(random.uniform(15, 25))
    div_selector = "main>div>div:nth-child(2)>div"
    # WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located(
    #         (By.CSS_SELECTOR, div_selector)))
    anchor_selector = f"{div_selector} a"

    anchor_tags = driver.find_elements(By.CSS_SELECTOR, anchor_selector)

    # print("Number of anchor tags:", len(anchor_tags))

    print("Number of anchor tags:", len(anchor_tags))

    for i in range(0, 2):

      with open('list.txt', 'r') as f:
        clicked_links = f.read().splitlines()
        print(clicked_links)
      time.sleep(4)

      # while random_link in clicked_links:
      while True:

        random_index = random.randint(0, len(anchor_tags) - 1)
        random_anchor_tag = anchor_tags[random_index]
        print(random_index)
        random_link = random_anchor_tag.get_attribute("href")
        count += 1

        if random_link not in clicked_links:
          break
        elif count > 50:
          print("already done")
          exit_flag = True
          break
      if exit_flag:
        break
      print(random_link)
      with open('list.txt', 'a') as f:
        f.write(f'{random_link}\n')
        time.sleep(2)
      random_anchor_tag.click()

      # driver.find_element(
      #     By.CSS_SELECTOR, "main>div>div:nth-child(2)>div>a:nth-child(2)").click()

      time.sleep(20)

      description = driver.find_element(
          By.CSS_SELECTOR,
          "#root > div > main > div > div.NewWatchingDiscovery__watchingSection___3Bzey > div > div.WatchingSection__safeZone___w2sTV > div > div:nth-child(2) > div > div > div.NewVideoInfo__videoInfoMetadataWrapper___2y4jE > button > span"
      )
      description_text = description.text
      time.sleep(4)
      print(description_text)
      if description_text == "Show details":
        description.click()

      anchor_tags = driver.find_elements(
          By.CSS_SELECTOR,
          "#root > div > main > div > div.NewWatchingDiscovery__watchingSection___3Bzey > div > div.WatchingSection__safeZone___w2sTV > div > div:nth-child(2) > div > div > div.NewVideoInfo__videoInfoMetadataWrapper___2y4jE > div.NewVideoInfoDescription__videoInfoDescription___FBUHp > div a"
      )
      original_window = driver.current_window_handle
      # Iterate over each anchor tag
      for anchor in anchor_tags:

        link = anchor.get_attribute('href')

        if link not in clicked_links:

          ActionChains(driver).move_to_element_with_offset(
              anchor, random.randint(5, 20), random.randint(5, 20)).perform()

          # Wait for a random duration before clicking
          time.sleep(random.uniform(1, 2))
          anchor.click()
          time.sleep(random.uniform(1, 2))
          time.sleep(2)

          class number_of_windows_to_be_either(object):

            def __init__(self, count1, count2):
              self.count1 = count1
              self.count2 = count2

            def __call__(self, driver):
              return len(driver.window_handles) == self.count1 or len(
                  driver.window_handles) == self.count2

          def close_other_tabs(driver, main_window):
            for window in driver.window_handles:
              if window != main_window:
                driver.switch_to.window(window)
                driver.close()
            driver.switch_to.window(main_window)

          wait.until(number_of_windows_to_be_either(2, 3))

          # with open("links.txt", "a") as file:
          #     file.write(link + "\n")

          # driver.delete_all_cookies()
          for window_handle in driver.window_handles:
            if window_handle != original_window:
              driver.switch_to.window(window_handle)
              break

          # Check for Cloudflare verification and click the checkbox if present
          try:
            cloudflare_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "input[type='checkbox']")))
            # EC.presence_of_element_located((By.ID, 'checkbox')))
            ActionChains(driver).move_to_element_with_offset(
                cloudflare_checkbox, random.randint(5, 20),
                random.randint(5, 20)).perform()
            time.sleep(random.uniform(1, 2))
            cloudflare_checkbox.click()
          except:
            pass

          wait.until(EC.presence_of_element_located((By.ID, 'downloadbtn')))

          download_button = driver.find_element(By.ID, 'downloadbtn')
          ActionChains(driver).move_to_element_with_offset(
              download_button, random.randint(5, 20),
              random.randint(5, 20)).perform()
          time.sleep(random.uniform(1, 2))
          download_button.click()

          print("waiting 50-60 secs")
          time.sleep(random.randint(15, 20))

          with open("links.txt", "a") as file:
            file.write(link + "\n")
          driver.delete_all_cookies()
          time.sleep(3)
          close_other_tabs(driver, original_window)

          time.sleep(5)

      store_current_time()

      driver.quit()

  except:
    print(Exception)
  finally:

    driver.quit()


if __name__ == "__main__":
  while True:
    check_time()
    # time.sleep(60)  # Wait for 60 seconds before checking again
