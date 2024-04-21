# Web Scrapping Scripts

- The screenshots of hail dataset social media links can be found at [Hail Forecasting Google Drive/Web Scrapping Scripts Folder](https://drive.google.com/drive/folders/1Zt2RvmurvnNoFaNOgp3cNkqhztDKJNie?usp=drive_link).
- If you do not have access to the folder, please send an email at `techandy42@gmail.com` or `dominique.brunet@ec.gc.ca` to gain access.

### Important Note

- The following code must be ran on a physical device like PowerShell on a laptop, not from a remote server or Colab Notebook

### Setup

- Install the following packages:
```
!pip install pyautogui pandas
```
- If you are running newer versions of Python, you may also need to install:
```
!pip install Pillow
```

- Run the following file to take screenshot of each social media link from the `extracted_info_with_validation.csv` file using `pyautogui` library:
```
!python screenshot_from_url.py
```
- Note, you must not open any other tabs while running the `screenshot_from_url.py` script, as it is opening new tabs and taking screenshots on the device itself

- Run the following file to zip the `images/` folder:
```
!python zip_images.py
```
