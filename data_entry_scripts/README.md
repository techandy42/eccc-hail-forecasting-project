# Severe Weather Data Entry

- The `data_entry.py` script uses `pyautogui` library to automatically fill-out the Severe Weather Report Form at `https://nswed-dev.cmc.ec.gc.ca/view/event-entry`.

### Setup

- Install the following packages:
```
!pip install pyautogui pandas
```
- If you are running newer versions of Python, you may also need to install:
```
!pip install Pillow
```

- Run the following file to automatically input sample data into the Severe Weather Report Form.
```
!python data_entry.py
```

### Adjusting to Screensize

- The X and Y coordinates of each inputs and buttons will depend on the screensize, you can open up a python terminal (type `python` on your terminal) and run the following commands.
```python
import pyautogui
# Hover over the spot that you want to find the coordinates to
pyautogui.position()
```
