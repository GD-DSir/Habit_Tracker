# Introduction
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

Alternatively, if you have git installed the code can be cloned using https://github.com/GD-DSir/Habit_Tracker.git as the source directory. (Option 1 is recommended as it requires no additional installations)  

To run the program head to https://www.python.org/downloads/ and download the python package for your operating system.

Head to the extracted folder containing readme.md and tracker.py
If using Windows click on the Explorer address bar in the folder and type cmd. This will run the cmd terminal. In the terminal type: py tracker.py

An example habits.json file is included, the file can be deleted or habits removed via the interface.

# Use application
## If habits.json does not exist or is empty:

The only usable pane in this case is the input pane. Both the stat and menu pane will inform the user to add a habit to use the program features.

Using the add function on input pane (add pane):

The add pane consists of the following elements:
- Entry box to input habit name.
- Radiobuttons to select habit frequency.
- Radiobuttons to select the completion state of the habit.
- Add button to add habit with specified properties. 

  The complete function is used to add habits that are not complete at time of adding. The habits will be added to list of habits allowing users to be reminded of the habit regardless of completion.
  The main use for this is to add a habit that might be forgotten if not added at the time of think about it, useful for those who are forgetful.

The Add button is only clickable if all fields are filled.

## With a habit now added, or using example file:

All panes are now usable. 
New habits can be added using the add pane, habits with the same name as existing habits cannot be added.
Statistics will be displayed in the stat pane.
The buttons of the menu pane are clickable and program can be navigated:
- Button 1: Log Progress

  Clicking Button 1 will replace the buttons on the menu pane with a scrollable list of buttons with habit names, the return button can be used to return to previous menu. Clicking on the name of habit to be logged will trigger a pop-up prompting the user to confirm.
  When confirmed one of 3 pop-ups will be displayed:
  - Pop-up 1: 'habit_name' was successfully logged current streak 'habit_streak'.
 
    This pop-up is displayed if a daily habit is logged within streak+1 days since the start of the the streak. This affords a user the ability to miss the habit once without the streak resetting.

    This pop-up is displayed if a weekly habit is logged within streak*7 days 12-hour since the start of the the streak. Weekly habits have a 12-hour grace period.
  - Pop-up 2: The current streak for habit_name has reset was 'habit_streak' currently 1.
    
    This pop-up is displayed if a daily habit is not logged within streak+1 days since the start of the the streak. The previous streak value is set to 1.

    This pop-up is displayed if a weekly habit is not logged within streak*7 days 12-hour since the start of the the streak. The previous streak value is set to 1.
  - Pop-up 3: 'habit_name' was logged 'hours'h:'minutes'm ago, Please try again later.
 
    This pop-up is displayed if a daily habit is logged within 10h of the previous log. This affords a user the ability to catch-up a missed day and reset the grace period.

    This pop-up is displayed if a weekly habit is logged within 6d of the previous log.
- Button 2: Open Habit Menu

  Clicking Button 2 will replace the buttons on the menu pane with 3 new buttons:
  - Button 1: Modify a Habit
 
    Clicking Button 1 will replace the buttons on the menu pane with a scrollable list of buttons with habit names, the return button can be used to return to previous menu. Clicking on the name of habit to modify will replace the add function with the modify function.
    Using the edit function on input pane (edit pane):

    The edit pane consists of the following elements:
    - Entry box to input new habit name.
    - Radiobuttons to select habit frequency.
    - Return button place add pane on input pane.
    - Reset button sets habit state to incomplete and removes stored data.
    - Change button to add habit with specified properties, and place add pane on input pane. 

    The name of the habit can be set to its existing name if the frequency is changed, the name and frequency can both be changed and the name can be changed without changing frequency. If the properties are unchanged the user will be informed.

    If the frequency is changed the habit will be reset. Changing the name does not reset the progress. 

    The Change button is only clickable if all fields are filled, and above conditions satisfied.

    This will also refresh the stat and menu pane to reflect the changes made.
  - Button 2: Remove a Habit
    
    Clicking Button 2 will replace the buttons on the menu pane with a scrollable list of buttons with habit names, the return button can be used to return to previous menu. Clicking on the name of habit to remove will trigger a pop-up:

    The pop-up reads -- Habit 'habit_name' will be deleted, THIS CANNOT BE UNDONE' -- The user must confirm.
    
    If confirmed the habit is removed and cannot be recovered.

    This will also refresh the stat and menu pane to reflect the changes made.
  - Button 3: Return
 
    Clicking Button 3 will replace the buttons on the menu pane with main menu buttons (previous menu)
  
- Button 3: View Additional Stats

  Clicking Button 3 will replace the buttons on the menu pane with 4 new buttons:
  - Button 1: Detailed Habit Stats
 
    Clicking Button 1 will replace the buttons on the menu pane with a scrollable list of buttons with habit names, the return button can be used to return to previous menu. Clicking on the name of habit will view the following statistics on the stats pane.
    
    - Habit name
    - Frequency
    - Current streak
    - Longest streak
    - Date added
    - Habit age
    - Time since last log
   
    The return button on this page will replace the detail statistics with the main page statistics   
  - Button 2: Best and Worst
 
    Clicking Button 2 will display the best and worst performing habit information on the stats pane.

    The performance is a measure of the number of logs completed since the habit was added. Number of recorder logs / days or weeks depending on frequency. A greater ratio indicates a better performing habit. 
  - Button 3: Habit Frequency
 
    Clicking Button 3 will display the frequency of all habits.
    
    2 List boxes are created on the stats pane, one for daily on for weekly.

    The return button on this page will replace the detail statistics with the main page statistics
  - Button 4: Return
 
    Clicking Button 4 will replace the buttons on the menu pane with main menu buttons (previous menu)


