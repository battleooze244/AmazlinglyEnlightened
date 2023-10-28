import json
import subprocess
import fileinput
import time
import random
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, timedelta

from workaround import update_executable_path
import os
from keep_alive import keep_alive

keep_alive()
ua = UserAgent().random
chromedriver_path = update_executable_path()

executable_path = chromedriver_path
os.system(f"chmod 700 {executable_path}")


def store_current_time(video):
  data = {"time": str(datetime.now()), "video": video}
  with open("time.txt", "w") as file:
    json.dump(data, file)


def check_time():
  with open("time.txt", "r") as file:
    file_contents = file.read().strip()

  if file_contents:
    data = json.loads(file_contents)
    stored_time = datetime.strptime(data["time"], '%Y-%m-%d %H:%M:%S.%f')
    video = data["video"]

    # If the stored time is more than 24 hours ago or video is 2
    if datetime.now() - stored_time > timedelta(hours=25) or video < 2:
      seadra()
    else:
      print("Checking time: 24 hours have not passed yet.")
  else:
    print("The time.txt file is empty.")
    seadra()


def seadra():
  print("The stored time is more than 24 hours ago or video is 2.")
  with open("time.txt", "w") as file:
    file.write("")
  main()


def get_previous_video_count():
  with open("time.txt", "r") as file:
    file_contents = file.read().strip()

  if file_contents:
    data = json.loads(file_contents)
    return data["video"]
  else:
    return 0


def main():

  options = uc.ChromeOptions()
  # options.add_argument(f'--user-agent={ua}')
  options.add_argument("--no-sandbox")
  options.add_argument('--profile-directory=Default')
  options.add_argument('--disable-plugins-discovery')
  options.add_argument('--start-maximized')
  options.add_argument("--disable-dev-shm-usage")
  options.add_argument("--disable-gpu")
  options.add_argument("--disable-extensions")
  options.add_argument("--disable-popup-blocking")
  options.add_argument("--disable-infobars")
  options.add_argument("--disable-notifications")
  # options.add_argument("--headless=False")
  # options.add_argument("--disable-web-security")
  # options.add_argument("--disable-features=VizDisplayCompositor")
  options.add_argument("--disable-features=NetworkService")
  # options.add_argument("--disable-features=VizHitTestSurfaceLayer")
  # options.add_argument("--disable-features=VizHitTestDrawQuad")
  # options.add_argument("--disable-features=VizHitTestDrawQuad")
  options.add_argument("--enable-javascript")
  options.add_argument("--disk-cache-size=0")
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
    video_count = get_previous_video_count()
    print("currently watched", video_count)
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located(
    #     (By.XPATH, "//span[@class='x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft']")))

    # link_element = driver.find_element(
    #     By.XPATH,
    #     "//span[@class='x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft']")
    # link_element.click()
    # driver.get(
    #     "https://www.dailymotion.com/dm_d9726f3b44285e4df6e33980937290f2")
    driver.get(
        "https://l.instagram.com/?u=https%3A%2F%2Fwww.dailymotion.com%2Fdm_d9726f3b44285e4df6e33980937290f2&e=AT3F4-tKngod63Up6ZnhpZyF2UQ-sLd5QL_K1J2S92XloHlB0bS_o8Df3SxVw-REjBJCvMMTUoInf1ndFjUUysv1tR_y_8_Cqf2OjmfWf2J9_mSk"
    )
    time.sleep(random.uniform(10, 15))

    driver.find_element(
        By.CSS_SELECTOR,
        "body > div > div.page.-cx-PRIVATE-Page__body.-cx-PRIVATE-Page__body__ > div > div > p:nth-child(3) > button"
    ).click()
    time.sleep(random.uniform(25, 35))
    div_selector = "main>div>div:nth-child(2)>div"
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, div_selector)))
    anchor_selector = f"{div_selector} a"

    anchor_tags = driver.find_elements(By.CSS_SELECTOR, anchor_selector)

    # print("Number of anchor tags:", len(anchor_tags))

    print("Number of anchor tags:", len(anchor_tags))

    for i in range(0, 2):
      video_count += 1

      time.sleep(4)

      with open('list.txt', 'r') as f:
        clicked_links = f.read().splitlines()
        print(clicked_links)
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
          store_current_time(2)

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
      time.sleep(40)
      # WebDriverWait(driver, 20).until(
      #     EC.presence_of_element_located((
      #         By.XPATH,
      #         "#player > div > div.vod_mouse_keyboard > div.controls_vod > div.controls_layer_1 > button"
      #     )))

      # play_button = driver.find_element(
      #     By.CSS_SELECTOR,
      #     "#player > div > div.vod_mouse_keyboard > div.controls_vod > div.controls_layer_1 > button"
      # )
      # if play_button:
      #   play_button.click()
      #   time.sleep(random.uniform(15, 25))
      try:
        play_button = driver.find_element(By.CLASSNAME, "playback_button")

        button_state = play_button.get_attribute("aria-label")

        if button_state == "Play":
          play_button.click()
          print("Clicked the Play button")
        elif button_state == "Pause":
          print("The button is already in the Pause state")
      except:
        print("The button is not present")

      # time.sleep(random.uniform(200,300))
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
      time.sleep(random.uniform(4, 8))

      anchor_tags = driver.find_elements(
          By.CSS_SELECTOR,
          "#root > div > main > div > div.NewWatchingDiscovery__watchingSection___3Bzey > div > div.WatchingSection__safeZone___w2sTV > div > div:nth-child(2) > div > div > div.NewVideoInfo__videoInfoMetadataWrapper___2y4jE > div.NewVideoInfoDescription__videoInfoDescription___FBUHp > div a"
      )
      original_window = driver.current_window_handle
      # Iterate over each anchor tag
      with open('links.txt', 'r') as f:
        cm_links = f.read().splitlines()
        print(cm_links)
      for anchor in anchor_tags:

        link = anchor.get_attribute('href')

        if link not in cm_links:
          print(link)
          # ActionChains(driver).move_to_element_with_offset(
          #     anchor, random.randint(5, 20), random.randint(5, 20)).perform()

          # Wait for a random duration before clicking
          time.sleep(random.uniform(1, 2))
          anchor.click()
          time.sleep(random.uniform(3, 7))
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
                cloudflare_checkbox, random.randint(5, 13),
                random.randint(5, 13)).perform()
            time.sleep(random.uniform(1, 2))
            cloudflare_checkbox.click()
          except:
            pass

          wait.until(EC.presence_of_element_located((By.ID, 'downloadbtn')))
          print("waiting for Downloaded button")
          try:
            download_button = driver.find_element(By.ID, 'downloadbtn')
            ActionChains(driver).move_to_element_with_offset(
                download_button, random.randint(5, 13),
                random.randint(5, 13)).perform()
            time.sleep(random.uniform(1, 2))
            download_button.click()
          except:
            print("downlaod not clickable or present")

          print("Downloaded Video clicked")
          print("waiting 50-60 secs")
          time.sleep(random.randint(70, 90))

          with open("links.txt", "a") as file:
            file.write(f'{link}\n')
          driver.delete_all_cookies()
          time.sleep(3)
          close_other_tabs(driver, original_window)

          store_current_time(video_count)
          time.sleep(5)

    driver.quit()

  except:
    print(Exception)
  finally:

    driver.quit()


# if __name__ == "__main__":
#   while True:
#     check_time()
#     time.sleep(60)

if __name__ == "__main__":
  while True:
    check_time()
    time.sleep(60)
