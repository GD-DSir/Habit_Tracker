# Intoduction
Welcome and thank you for trying out my Habit tracker, the Tracker was made to track the progress of various Habits of daily and weekly frequencies, with the goal of motivating users to build habits and reminding users of habits to be completed.

# Overview
The program uses a GUI created with tkinter. The main screen has 3 panes:
- Stats pane
- Menu pane
- Input pane

The stats pane is used to display all statistical information: detailed habits stats, habit frequencies, best and worst performing.
The menu pane is used to navigate the program, giving users the ability to:
- Log existing habits
- Modify an existing habit
- Reset an existing habit
- Delete an existing habit
    
The input pane is used to add and modify habits, it utilizes an Entry box for naming and radio buttons for frequency selection. 
 
# Install/Run
On the github page https://github.com/GD-DSir/Habit_Tracker.git click the code dropdown button. Click on download zip and wait for download to finish.
Once finished head to the downloads folder and extract the contents of the zip file.

Alternatively if you have git installed the code can be cloned using https://github.com/GD-DSir/Habit_Tracker.git as the source directory. (Option 1 is recommended as it requires no additional installations)  

To run the program head to https://www.python.org/downloads/ and download the python package for your operating system.

Head to the extracted folder containing readme.md and tracker.py
If using Windows click on the Explorer adress bar in the folder and type cmd. This will run the cmd terminal. In the terminal type: py tracker.py

An example habits.json file is included, the file can be deleted or habits removed via the interface.

# Use application
If habits.json exists and contains data:
Statistics will be displayed in the stat pane.
The buttons of the menu pane are clickable and program can be navigated:
- Button 1: Log Progress

  Clicking Button 1 will replace the buttons on the menu pane with a scrollable list of buttons with habit names. Clicking on the name of habit to be logged will trigger a pop-up prompting the user to confirm.
  When confirmed one of 3 pop-ups will be displayed:
  - Pop-up 1: 'habit_name' was successfully logged current streak 'habit_streak'
  - Pop-up 2: The current streak for habit_name has reset was 'habit_streak' currently 1
  - Pop-up 3: habit_name was logged 'hours'h:'minutes'm ago, Please try again later
- Button 2: Open Habit Menu
- Button 3: View Additional Stats

If habits.json does not exist or is empty.
