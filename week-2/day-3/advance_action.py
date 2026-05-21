import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# 1. Import the ActionChains tool for advanced interactions
from selenium.webdriver import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")          # Prevents OS security permission errors
chrome_options.add_argument("--disable-dev-shm-usage") # Prevents memory resource limits
chrome_options.add_argument("--disable-gpu")          # Avoids hardware acceleration bugs
chrome_options.add_argument("--start-maximized") 

# 2. Launch the browser using the updated options
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window() # Maximize so all elements are easily visible

try:
    mouse_actions = ActionChains(driver)
    # ==========================================
    # ACTION 1: MOUSE HOVER (Python.org)
    # ==========================================
    driver.get("https://python.org")
    time.sleep(2)

    # Find the "Community" menu link on the page
    community_menu = driver.find_element(By.LINK_TEXT, "Community")

    mouse_actions.move_to_element(community_menu).perform()
    print("1. Hover action successful!")
    time.sleep(2)

    # ==========================================
    # ACTION 2: DOUBLE CLICK 
    # ==========================================
    driver.get("https://demo.guru99.com/test/simple_context_menu.html")

# 2. Locate the button using the precise button text match
    double_click_button = driver.find_element(By.XPATH, "//button[contains(text(),'Double-Click Me To See Alert')]")
    
    actions = ActionChains(driver)
    actions.double_click(double_click_button).perform()
    print("2. Double-click action successful!")
    time.sleep(2)
    
    driver.switch_to.alert.accept() 
    time.sleep(1)
# ==========================================
    # ACTION 3: DRAG AND DROP 
    # ==========================================
    driver.get("https://demo.guru99.com/test/drag_drop.html")
    time.sleep(2)
   
    #source_money_block = driver.find_element(By.ID, "fourth")
      
    #target_amount_placeholder = driver.find_element(By.ID, "amt7")

    #mouse_actions.drag_and_drop(source_money_block, target_amount_placeholder).perform()

    source_money_block = driver.find_element(By.XPATH, "//*[@id='fourth']/a")
      
# . Locate the specific target placeholder drop list element
# Note: "amt7" targets the container block. The element drops directly inside the list item child.
    target_amount_placeholder = driver.find_element(By.XPATH, "//*[@id='amt7']/li")

# . Initialize and run ActionChains to execute the mouse movement
    mouse_actions = ActionChains(driver)
    mouse_actions.drag_and_drop(source_money_block, target_amount_placeholder).perform()
    print("3. Drag and Drop action successful!")
    time.sleep(3)
finally:
    
   driver.quit()