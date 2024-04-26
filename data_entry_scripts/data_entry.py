import webbrowser
import pyautogui
import time
import platform

# Open URL
url = "https://nswed-dev.cmc.ec.gc.ca/view/event-entry"
webbrowser.open(url)

# Wait for 1 seconds to ensure the page has loaded
time.sleep(2)

# Assuming x, y coordinates have been set for startTime and endTime inputs
# Example (these coordinates must be determined through trial and error):
x_coordinate_startTime = 640
y_coordinate_startTime = 835
pyautogui.click(x_coordinate_startTime, y_coordinate_startTime)
pyautogui.typewrite('2024-04-26 14:31Z')

x_coordinate_endTime = 640
y_coordinate_endTime = 991
pyautogui.click(x_coordinate_endTime, y_coordinate_endTime)
pyautogui.typewrite('2024-04-26 14:31Z')

pyautogui.scroll(-500)

time.sleep(2)

x_coordinate_notes = 616
y_coordinate_notes = 933
pyautogui.click(x_coordinate_notes, y_coordinate_notes)
pyautogui.typewrite('Test entry. DO NOT USE.')

time.sleep(2)

pyautogui.scroll(10000)

time.sleep(2)

x_coordinate_type_first_item = 200
y_coordinate_type_first_item = 800
pyautogui.click(x_coordinate_type_first_item, y_coordinate_type_first_item)

pyautogui.scroll(10000)

time.sleep(2)

# Take a screenshot
screenshot = pyautogui.screenshot()
screenshot.save('page1.png')

time.sleep(2)

x_coordinate_location_tab = 333
y_coordinate_location_tab = 620
pyautogui.click(x_coordinate_location_tab, y_coordinate_location_tab)
pyautogui.click(x_coordinate_location_tab, y_coordinate_location_tab)

pyautogui.scroll(-65)

time.sleep(2)

x_coordinate_latitude = 1276
y_coordinate_latitude = 839
pyautogui.click(x_coordinate_latitude, y_coordinate_latitude)
pyautogui.typewrite('50')
x_coordinate_longitude = 1276
y_coordinate_longitude = 952
pyautogui.click(x_coordinate_longitude, y_coordinate_longitude)
pyautogui.typewrite('-50')

time.sleep(2)

# Take a screenshot
screenshot = pyautogui.screenshot()
screenshot.save('page2.png')

pyautogui.scroll(-10000)

time.sleep(2)

x_coordinate_submit = 1652
y_coordinate_submit = 730
pyautogui.click(x_coordinate_submit, y_coordinate_submit)
pyautogui.click(x_coordinate_submit, y_coordinate_submit)

time.sleep(2)

pyautogui.scroll(-350)

time.sleep(5)

# Take a screenshot
screenshot = pyautogui.screenshot()
screenshot.save('submission.png')

# Close the browser tab
pyautogui.hotkey('ctrl', 'w')  # This might be 'cmd', 'w' on a Mac

