import pandas as pd
import webbrowser
import time
import pyautogui
import sys
import re
import os

def is_valid_generic_twitter_url(url):
    # Regex pattern to match the required URL format
    pattern = r'^https://(www\.)?twitter\.com/[^/]+$'
    
    # re.match() checks for a match only at the beginning of the string
    if re.match(pattern, url):
        return True
    else:
        return False

def check_generic_url(url):
    if url in ['https://twitter.com', 'https://www.twitter.com', 'https://facebook.com', 'https://www.facebook.com']:
        return True
    elif is_valid_generic_twitter_url(url):
        return True
    return False

def open_browser_and_capture(idx, url, url_no = None):
    try:
        if check_generic_url(url):
            return 'GENERIC'

        # Open the default web browser to the specified URL
        webbrowser.open(url)
        
        # Wait for the browser to load the page
        time.sleep(5)  # Adjust this time based on your internet speed and page load time
        
        if 'twitter.com' in url:
            # Scroll down 90 pixels if the URL contains "twitter.com"
            pyautogui.scroll(-90)  # Negative value for scrolling down

        # Take a screenshot and save it
        screenshot = pyautogui.screenshot()
        image_path = f'images/{idx}_1.png' if url_no is None else f'images/{idx}_{url_no}.png'
        screenshot.save(image_path)

        if 'twitter.com' in url:
            # Scroll down 300 pixels if the URL contains "twitter.com"
            pyautogui.scroll(-300)  # Negative value for scrolling down
            screenshot = pyautogui.screenshot()
            image_path = f'images/{idx}_1l.png' if url_no is None else f'images/{idx}_{url_no}l.png'
            screenshot.save(image_path)
        
        # Close the browser tab
        if sys.platform == 'darwin':  # macOS
            pyautogui.hotkey('cmd', 'w')
        else:  # Windows/Linux
            pyautogui.hotkey('ctrl', 'w')

        return 'SUCCESS'
    except Exception as e:
        print(f"Error occurred at row {idx}: {str(e)}")
        
        return 'FAILURE'

def contains_https_single_time(text):
    # Count occurrences of "https://"
    count = text.count("https://")
    # Check if "https://" appears more than once
    return count == 1

def contains_https_multiple_times(text):
    # Count occurrences of "https://"
    count = text.count("https://")
    # Check if "https://" appears more than once
    return count > 1

def split_string(input_string):
    # Split the string by space or comma and filter out empty strings
    return [part for part in re.split(r'[ ,]+', input_string) if part]

# Define the folder name
folder_name = "images"

# Check if the folder exists
if not os.path.exists(folder_name):
    # Create the folder
    os.makedirs(folder_name)
    print(f"Folder '{folder_name}' created.")
else:
    print(f"Folder '{folder_name}' already exists.")

df_extracted_info = pd.read_csv('./extracted_info_with_validation.csv')

status_and_row_indexes = []

for row_index, social_media_link in zip(df_extracted_info['row_index'], df_extracted_info['social_media_link']):
    if contains_https_single_time(social_media_link):
        status = open_browser_and_capture(row_index, social_media_link)
        status_and_row_indexes.append({
            'row_index': row_index,
            'status': status,
        })
    elif contains_https_multiple_times(social_media_link):
        urls = split_string(social_media_link)
        row_status = 'FAILURE'
        for i, url in enumerate(urls):
            status = open_browser_and_capture(row_index, url, i)
            if row_status == 'FAILURE':
                row_status = status
            elif row_status == 'GENERIC' and status == 'FAILURE':
                row_status = status
        status_and_row_indexes.append({
            'row_index': row_index,
            'status': row_status,
        })

df_extracted_info['social_media_link_status'] = 'NOT_FOUND'

for status_and_row_index in status_and_row_indexes:
    row_index = status_and_row_index['row_index']
    status = status_and_row_index['status']
    df_extracted_info.loc[row_index, 'social_media_link_status'] = status

df_extracted_info.to_csv('extracted_info_with_validation_and_link_status.csv', index=False)
