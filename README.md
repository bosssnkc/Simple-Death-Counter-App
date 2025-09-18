Simple Death Counter App
English

Simple Death Counter App is a simple desktop GUI application built with Python’s Tkinter library.
It helps you keep track of the number of “deaths” (or any counter you want to use) while playing games or doing activities.
You can increment, decrement, reset, and set a custom value, and optionally save/load the count to a .txt file.

# Features

1. Increment / Decrement: Increase or decrease the counter by pressing buttons or using hotkeys.

2. Reset: Reset the counter back to 0.

3. Set Custom Count: Input a custom number into the entry box and set it.

4. Save/Load: Save the counter value into a .txt file and reload it later.

# Hotkeys:

- Ctrl + Shift + Page Up → Increment count

- Ctrl + Shift + Page Down → Decrement count


# Installation & Usage

1. Download the latest release GitHub you will found file name death_counter.exe.

2. Double-click to run the program — no installation required.

3. The application window will open and you can start tracking immediately.

# File Saving

- If you click .txt Output, you can choose where to save your counter in a .txt file.

- If you don’t select a file, the app will still run but will not save data.

# **For Developer and who want to customize**

# **If you want to edit and create yourself Simple Death Counter App follow requirements section**
## Requirements

Make sure you have Python 3 installed, along with the following libraries:

`pip install keyboard`

## How to Run Code

Clone or download the project.

Run the Python script:

`python death_counter.py`

Use the GUI or hotkeys to update your counter.

## If you want to build your own .exe:

`pip install pyinstaller`
`pyinstaller --onefile --noconsole death_counter.py`


The compiled file will appear in the dist/ folder.

