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
If habits.json does not exist or is empty:
The only usable pane in this case is the input pane. Both the stat and menu pane will inform the user to add a habit to use the program features.

Using the add function on input pane (add pane):

The add pane consists of the following elements:
- Entry box to input habit name.
- Radiobuttons to select habit frequency.
- Radiobuttons to select the completion state of the habit.
- Add button to add habit with specified properties. 

  The complete function is used to add habits that are not complete at time of adding. The habits will be added to list of habits allowing users to be reminded of the habit regardless of completion.
  The main use for this is to add a habit that might be forgotten if not added at the time of think about it, usefull for those who are forgetfull.

The Add button is only clickable if all fields are filled.


With a habit now added, or using example file:

All panes are now usable. 
New habits can be added using the add pane.
Statistics will be displayed in the stat pane.
The buttons of the menu pane are clickable and program can be navigated:
- Button 1: Log Progress

  Clicking Button 1 will replace the buttons on the menu pane with a scrollable list of buttons with habit names. Clicking on the name of habit to be logged will trigger a pop-up prompting the user to confirm.
  When confirmed one of 3 pop-ups will be displayed:
  - Pop-up 1: 'habit_name' was successfully logged current streak 'habit_streak'.
 
    This pop-up is displayed if a daily habits is logged within streak+1 days since the start of the the streak. This affords a user the ability to miss the habit once without the streak resetting.
    This pop-up is displayed if a weekly habits is logged within streak*7 days 12 hour since the start of the the streak. Weekly habits have a 12 hour grace period.
  - Pop-up 2: The current streak for habit_name has reset was 'habit_streak' currently 1.
    
    This pop-up is displayed if a daily habits is not logged within streak+1 days since the start of the the streak. The previous streak value is set to 1.
    This pop-up is displayed if a weekly habits is not logged within streak*7 days 12 hour since the start of the the streak. The previous streak value is set to 1.
  - Pop-up 3: 'habit_name' was logged 'hours'h:'minutes'm ago, Please try again later.
 
    This pop-up is displayed if a daily habits is logged within 10h of the previous log. This affords a user the ability to catch-up a missed day and reset the grace period.
    This pop-up is displayed if a weekly habits is logged within 6d of the previous log.
- Button 2: Open Habit Menu
- Button 3: View Additional Stats


