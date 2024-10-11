from tkinter import *
import tkinter.messagebox
from scripts.data_handling import *
import datetime as dt
import math


class GUI:
    """Class used to create all elements of the habit tracing user interface, consists of a root window,
        3 primary Frames are created on this window.\n
        - stat_frame\n
        - menu_frame\n
        - input_frame\n
        all subsequent Frames are created on the primary frames."""
    def __init__(self):

        # tk root_window Config
        self.root = Tk()                                # Create root_window.
        self.root.title('Habit Tracker')                # root_window title.
        self.root.geometry('800x267+10+10')             # Fix the size of root_window.
        self.root.config(padx=50, pady=20)              # Padding of root_window.

        # stats_frame (Column 1) Config
        self.stat_frame = Frame(self.root)               # Create stat_frame.
        self.stat_frame.grid(column=1, row=1)            # Grid stat_frame in column 1 of root_window.
        self.stat_frame.config(height=227, width=185)    # Configure the size of stat_frame.
        self.stat_frame.grid_propagate(False)            # Remove stat_frame auto rescaling.

        # menu_frame (Column 2) Config
        self.menu_frame = Frame(self.root)               # Create menu_frame.
        self.menu_frame.grid(column=2, row=1)            # Grid menu_frame in column 2 of root_window.
        self.menu_frame.config(height=227, width=190)    # Configure the size of menu_frame.
        self.menu_frame.grid_propagate(False)            # Remove menu_frame auto rescaling.

        # input_frame (Column 3) Config
        self.input_frame = Frame(self.root)               # Create input_frame.
        self.input_frame.grid(column=3, row=1)            # Grid input_frame in column 3 of root_window.
        self.input_frame.config(height=227, width=370)    # Configure the size of input_frame.
        self.input_frame.grid_propagate(False)            # Remove input_frame auto rescaling.

    def create_window(self):
        """Create the program window displayed on start-up"""
        valid = file_verification()                 # Verify data to determine frames to grid.
        self.add_frame()                            # Frame for adding is added to grid.
        if valid:                                   # If file contains data, grid active windows.
            self.main_button_active()               # Buttons are enabled.
            self.main_stat_active()                 # Stats are displayed.
        else:                                       # If file contains data, grid inactive windows.
            self.main_button_inactive()             # Buttons are disabled.
            self.main_stat_inactive()               # No stats available to display.
        self.root.mainloop()                        # Keep application active.

    def recreate(self):
        """Destroy and recreate window when data changes"""
        self.root.destroy()                         # Destroy the root window/application.
        self.__init__()                             # Re-initialize the root window.
        self.create_window()                        # Create program start menu

    def reset_stat_frame(self):
        """Destroy and recreate stat frame, from menu frame."""
        self.stat_frame.destroy()
        self.stat_frame = Frame(self.root)              # Create stat_frame
        self.stat_frame.grid(column=1, row=1)           # Grid stat_frame in column 1 of root_window
        self.stat_frame.config(height=227, width=185)   # Configure the size of stat_frame
        self.stat_frame.grid_propagate(False)

    def reset_input_frame(self):
        self.input_frame.destroy()
        self.input_frame = Frame(self.root)             # Create input_frame.
        self.input_frame.grid(column=3, row=1)          # Grid input_frame in column 3 of root_window.
        self.input_frame.config(height=227, width=370)  # Configure the size of input_frame.
        self.input_frame.grid_propagate(False)          # Remove input_frame auto rescaling.

    # Elements of start screen

    def main_stat_active(self):
        """Stats displayed on main menu at start-up, active denotes that the data file contains habits,
            and statistic data will be displayed"""
        main_stat_frame = Frame(self.stat_frame)        # Create the frame for main menu stats.
        main_stat_frame.grid(column=1, row=1)           # Grid the stats to the stat_frame.

        habit_list = data_retrieval()                   # Retrieve the list of objects.
        name = str                                      # Create variable name.
        longest_streak = 0                              # Create a variable longest_streak with value 0.

        longest_streak_label = Label(main_stat_frame, text="All Time Longest Streak:", font='Helvetica 8 bold')
        longest_streak_label.grid(column=1, row=1)      # Create and grid a label for the longest streak of all time.

        for habit in habit_list:                            # Iterate the objects in habit_list.
            if habit.complete == 'yes':                     # Isolate completed habits, using complete property.
                if habit.longest_streak > longest_streak:   # Compare the longest_streak of selected object with the
                    longest_streak = habit.longest_streak   # longest_streak of previous object, set longest_streak to
                    name = habit.name                       # the greater of the two. Capture the name of the habit
                                                            # with the longest_streak.

        longest_streak_info = Label(main_stat_frame, text=f"Habit: {name}\n"      # Add streak and habit name to label.       
                                                          f"{longest_streak} Times")
        longest_streak_info.grid(column=1, row=2, sticky=N)                       # Grid the information label.

        current_streak = 0                              # Create a variable longest_streak with value 0.

        current_streak_label = Label(main_stat_frame, text="Current Longest Streak:", font='Helvetica 8 bold')
        current_streak_label.grid(column=1, row=3)      # Create and grid a label for the longest current streak.

        for habit in habit_list:                            # Iterate the objects in habit_list.
            if habit.complete == 'yes':                     # Isolate completed habits, using complete property.
                if habit.streak > current_streak:           # Compare the current_streak of selected object with the
                    current_streak = habit.streak           # current_streak of previous object, set current_streak to
                    name = habit.name                       # the greater of the two. Capture the name of the habit
                                                            # with the longest current_streak

        current_streak_info = Label(main_stat_frame, text=f"Habit: {name}\n"       # Add streak and habit name to label.
                                                          f"{current_streak} Times")
        current_streak_info.grid(column=1, row=4, sticky=N)                        # Grid the information label.

        oldest = dt.timedelta(days=0)                   # Create a variable oldest, type: timedelta, value: days=0.

        oldest_label = Label(main_stat_frame, text="Oldest Habit:", font='Helvetica 8 bold')
        oldest_label.grid(column=1, row=5)              # Create and grid a label for the oldest habit.

        for habit in habit_list:                            # Iterate the objects in habit_list.
            if habit.complete == 'yes':                     # Isolate completed habits, using complete property.
                delta = dt.datetime.now() - dt.datetime.strptime(habit.first_log, '%Y-%m-%d %H:%M')
                if delta > oldest:                          # Compare the age of selected object with the
                    oldest = delta                          # age of previous object, age calculated using
                    name = habit.name                       # now()-first_log, set oldest to the greater of the two.
                                                            # Capture the name of the oldest habit .

        oldest_label_info = Label(self.stat_frame, text=f"Habit: {name}\n"      # Add age and habit name to label.
                                                        f"First logged {str(oldest)[:-10]} ago")
        oldest_label_info.grid(column=1, row=6, sticky=N)                       # Grid the information label.

    def main_stat_inactive(self):
        """Stats displayed on main menu at start-up, inactive denotes that the data file contains no habits,
            the user will be informed that no statistics can be displayed"""
        main_stat_frame = Frame(self.stat_frame)                        # Create the frame for main menu stats.
        main_stat_frame.grid(column=1, row=1)                           # Grid the stats to the stat_frame.

        no_habit = Label(main_stat_frame, text="No Habits Added")       # Create info labels, to inform user that no
        no_habit.grid(column=1, row=1)                                  # habit data exists, add labels to grid.
        nothing_label = Label(main_stat_frame, text="Add habits to start Tracking")
        nothing_label.grid(column=1, row=2, pady=160/2)

    def main_button_active(self):
        """Buttons on main menu at start-up, active denotes that the data file contains habits,
            3 buttons are created buttons are pressable and app can be navigated"""
        def log_clicked():
            """Remove the current button frame (main_button_frame) and grids another (log_buttons_frame)"""
            main_button_frame.destroy()     # Destroy current button frame.
            self.log_button()               # Grids the next button frame.

        def habit_clicked():
            """Remove the current button frame (main_button_frame) and grids another (habit_buttons_frame)"""
            main_button_frame.destroy()     # Destroy current button frame.
            self.habit_button()             # Grids the next button frame.

        def stat_clicked():
            """Remove the current button frame (main_button_frame) and grids another (stat_buttons_frame)"""
            main_button_frame.destroy()     # Destroy current button frame.
            self.stat_button()              # Grids the next button frame.

        main_button_frame = Frame(self.menu_frame)              # Create the main_button_frame, displayed on main menu
        main_button_frame.grid(column=1, row=1, padx=(30, 0))   # on start-up.

        main_menu_label = Label(main_button_frame, text="What do you wish to do:")
        main_menu_label.grid(column=1, row=1, sticky=W + E, pady=(0, 10))   # Create a label with a prompt.

        log_menu = Button(main_button_frame,                            # Set parameters for the first button.
                          text='Log Progress',
                          command=log_clicked,                          # Calls function log_clicked when button is
                          bd=1,                                         # pressed.
                          relief='ridge',
                          pady=10)
        log_menu.grid(column=1, row=2, sticky=W + E, pady=10)           # Add button to frame using grid.

        habit_menu = Button(main_button_frame,                          # Set parameters for the second button.
                            text='Open habit menu',
                            command=habit_clicked,                      # Calls function habit_clicked when button is
                            bd=1,                                       # pressed.
                            relief='ridge',
                            pady=10)
        habit_menu.grid(column=1, row=3, sticky=W + E, pady=(0, 10))    # Add button to frame using grid.

        stat_menu = Button(main_button_frame,                           # Set parameters for the third button.
                           text='View Additional Stats',
                           command=stat_clicked,                        # Calls function stat_clicked when button is
                           bd=1,                                        # pressed.
                           relief='ridge',
                           pady=10)
        stat_menu.grid(column=1, row=4, sticky=W + E)                   # Add button to frame using grid.

    def main_button_inactive(self):
        """Buttons on main menu at start-up, active denotes that the data file contains habits,
            3 buttons are created buttons are not pressable"""
        main_button_frame = Frame(self.menu_frame)              # Create the main_button_frame, displayed on main menu
        main_button_frame.grid(column=1, row=1, padx=(30, 0))   # on start-up.

        main_menu_label = Label(main_button_frame, text="Add a habit to access menus:")
        main_menu_label.grid(column=1, row=1, sticky=W + E, pady=(0, 10))   # Create a label with a prompt.

        log_menu = Button(main_button_frame,                            # Set parameters for the first button.
                          text='Log Progress',
                          bd=1,
                          relief='ridge',
                          pady=10,
                          state='disabled')                             # Button is disabled (not pressable).
        log_menu.grid(column=1, row=2, sticky=W + E, pady=10)           # Add button to frame using grid.

        habit_menu = Button(main_button_frame,                          # Set parameters for the second button.
                            text='Open habit menu',
                            bd=1,
                            relief='ridge',
                            pady=10,
                            state='disabled')                           # Button is disabled (not pressable).
        habit_menu.grid(column=1, row=3, sticky=W + E, pady=(0, 10))    # Add button to frame using grid.

        stat_menu = Button(main_button_frame,                           # Set parameters for the third button.
                           text='View stats',
                           bd=1,
                           relief='ridge',
                           pady=10,
                           state='disabled')                            # Button is disabled (not pressable).
        stat_menu.grid(column=1, row=4, sticky=W + E)                   # Add button to frame using grid.

    # Elements of the menu frame

    def log_button(self):
        """Called when log button is clicked on the main screen, creates a list of buttons with habit names and grids
            buttons on the menu_frame"""
        def selected(habit_button):
            """Called when clicking one of the habit buttons, habit_button is an integer value used to identify the
                index of the selected habit within the habit_list"""
            selected_habit = habit_button               # Set selected_habit to value habit_button returned from button
            habit_object = habit_list[selected_habit]   # click. Find the habit in habit_list using index selected_habit
            confirm = tkinter.messagebox.askyesno('Confirm',
                                                  f'Log habit {habit_object.name}') # Ask user if they wish to proceed
            if confirm:                     # If the user confirms.
                habit_object.log()          # Use the method .log() on the selected habit object.
                store_data(habit_list)      # Use store_data form script.store_data(habit_list), to store the habit_list containing the now modified object.
                log_buttons.destroy()       # Destroy the log_buttons Frame.
                self.log_button()           # Recreate the log buttons Frame, this is done to update the buttons.
                self.reset_stat_frame()     # Delete stat_frame and recreate stat_frame.
                self.main_stat_active()     # Recreate main_stat_active on new stat_frame, done to update data after .log()

        def return_clicked():
            """Called when return button is clicked, destroys the log_button frame and recreates the
                main_button frame"""
            self.main_button_active()   # Recreate the main_button frame, previous Frame.
            log_buttons.destroy()       # Destroy the log_button frame.

        log_buttons = Frame(self.menu_frame)                # Create the log_buttons_frame, displayed after clicking
        log_buttons.grid(column=1, row=1, padx=(30, 0))     # on the log button in the start-up menu.

        labels = Frame(log_buttons)                         # Create a frame to grid a label containing a prompt, fixed
        labels.grid(column=1, row=1)                        # while scrolling.

        log_label = Label(labels, text="Select a habit to log", width=20)   # Label with prompt on label frame.
        log_label.grid(column=1, row=1)

        habit_list = data_retrieval()                # Retrieve the list of habit objects for habits.json using
        list_of = []                                 # data_retrieval form script.data_handling. Create an empty list to
        row = 0                                      # append buttons, row used to iterate buttons and grid them.

        scroll_option = Canvas(log_buttons, width=130, height=140)  # Create a canvas to enable scrolling of a frame.
        scroll_option.grid(column=1, row=2, sticky=W)

        buttons = Frame(scroll_option)      # Create a frame to grid the habit buttons in list_of.

        scroller = Scrollbar(log_buttons, command=scroll_option.yview)      # Create scrollbar and assign target.
        scroller.grid(column=1, row=2, sticky=N + S + E)

        for habit in habit_list:                            # Iterate the habits in the habit_list.
            list_of.append(Button(buttons,                  # Append the buttons to the empty list, set parameters for
                                  text=f'{habit.name}',     # the habit buttons.
                                  command=lambda habit_button=row: selected(habit_button),# Call function selected_habit
                                  bd=1,                                                   # and assign the row number
                                  relief='ridge',                                         # as the variable habit_button
                                  padx=35))
            list_of[row].grid(column=1, row=row + 1, pady=(0, 10), sticky=W + E)    # Grid button to first row.
            row += 1                                                                # Set row for next habit to grid.

        scroll_option.create_window(0, 0, window=buttons, anchor='n')   # Create the canvas with Frame buttons.
        scroll_option.update()                                          # Keep scroll active.
        # Configure the Canvas, enable the scrolling of the Canvas using scrollbar (scroller), set scrollable region.
        scroll_option.configure(yscrollcommand=scroller.set, scrollregion=scroll_option.bbox("all"))

        commands = Frame(log_buttons)       # Create a new Frame for the return button, fixed while scrolling
        commands.grid(column=1, row=3)

        return_button = Button(commands, text='Return', command=return_clicked) # Create a button to return to previous
        return_button.grid(column=2, row=1, pady=(10, 0))                       # menu using function return_clicked

    def habit_button(self):
        """Called when Open habit menu button is clicked on the main screen, replaces the main screen buttons with 2 new
                buttons, modify habit and delete habit."""
        def modify_clicked():
            """Called when modify habit is clicked in the habit menu, creates a list of buttons with habit names and grids
                buttons on the menu_frame"""
            self.modify_button()       # Calls method modify_button, creates list of buttons.
            habit_buttons.destroy()    # Destroy the habit_button frame.

        def delete_clicked():
            """Called when delete habit is clicked in the habit menu, creates a list of buttons with habit names and grids
                buttons on the menu_frame"""
            habit_buttons.destroy()     # Destroy the habit_button frame.
            self.delete_button()        # Calls method delete_button, creates list of buttons.

        def return_clicked():
            """Called when return button is clicked, destroys the habit_button frame and recreates the
                main_button frame"""
            self.main_button_active()   # Destroy the habit_button frame.
            habit_buttons.destroy()     # Recreate the main_button frame, previous Frame.

        habit_buttons = Frame(self.menu_frame)                 # Create Frame for the habit buttons.
        habit_buttons.grid(column=1, row=1, padx=(30, 0))      # Grid Frame onto menu_frame.

        habit_menu_label = Label(habit_buttons, text="What do you wish to do:")
        habit_menu_label.grid(column=1, row=1, sticky=W + E, pady=(0, 10))     # Create a label with a prompt.

        edit_menu = Button(habit_buttons,                       # Set parameters for the first button.
                           text='Modify a Habit',
                           command=modify_clicked,              # Calls function modify_clicked when button is pressed.
                           bd=1,
                           relief='ridge',
                           pady=10)
        edit_menu.grid(column=1, row=2, sticky=W + E, pady=10)  # Add button to frame using grid.

        remove_menu = Button(habit_buttons,                     # Set parameters for the second button.
                             text='Remove a Habit',
                             command=delete_clicked,            # Calls function delete_clicked when button is pressed.
                             bd=1,
                             relief='ridge',
                             pady=10)
        remove_menu.grid(column=1, row=3, sticky=W + E, pady=(0, 10)) # Add button to frame using grid.

        return_button = Button(habit_buttons, text='Return', command=return_clicked, pady=10)
        return_button.grid(column=1, row=4) # Create and grid a return button, calls function return_clicked when clicked.

    def modify_button(self):
        """Called when modify button is clicked in the habit menu, creates a list of buttons with habit names and grids
            buttons on the menu_frame"""
        def selected(habit_button):
            """Called when clicking one of the habit buttons, habit_button is an integer value used to identify the
                index of the selected habit within the habit_list"""
            habit_id = habit_button     # Set habit_id to value habit_button returned from button.
            self.edit_frame(habit_id)   # Create edit Frame for selected habit and grid on input Frame.

        def return_clicked():
            """Called when return button is clicked, destroys the modify_button frame and recreates the
                habit_button frame"""
            self.habit_button()             # Recreate the habit_button frame, previous Frame.
            modify_buttons.destroy()        # Destroy the modify_button frame.

        modify_buttons = Frame(self.menu_frame)             # Create the modify_buttons_frame, displayed after clicking
        modify_buttons.grid(row=1, column=1, padx=(30, 0))  # on the modify button in the start-up menu.

        labels = Frame(modify_buttons)                      # Create a frame to grid a label containing a prompt, fixed
        labels.grid(column=1, row=1)                        # while scrolling.

        modify_label = Label(labels, text="Select a habit to modify", width=20) # Label with prompt on label frame.
        modify_label.grid(column=1, row=1)

        habit_list = data_retrieval()               # Retrieve the list of habit objects for habits.json using
        list_of = []                                # data_retrieval form script.data_handling. Create an empty list to
        row = 0                                     # append buttons, row used to iterate buttons and grid them.

        scroll_option = Canvas(modify_buttons, width=130, height=140)  # Create a canvas to enable scrolling of a frame.
        scroll_option.grid(column=1, row=2, sticky=W)

        buttons = Frame(scroll_option)      # Create a frame to grid the habit buttons in list_of.

        scroller = Scrollbar(modify_buttons, command=scroll_option.yview)   # Create scrollbar and assign target.
        scroller.grid(column=1, row=2, sticky=N + S + E)

        for habit in habit_list:                            # Iterate the habits in the habit_list.
            list_of.append(Button(buttons,                  # Append the buttons to the empty list, set parameters for
                                  text=f'{habit.name}',     # the habit buttons.
                                  command=lambda habit_button=row: selected(habit_button),# Call function selected_habit
                                  bd=1,                                                   # and assign the row number
                                  relief='ridge',                                         # as the variable habit_button
                                  padx=35))
            list_of[row].grid(column=1, row=row + 1, pady=(0, 10), sticky=W + E)    # Grid button to first row.
            row += 1                                                                # Set row for next habit to grid.

        scroll_option.create_window(0, 0, window=buttons, anchor='n')   # Create the canvas with Frame buttons.
        scroll_option.update()                                          # Keep scroll active.
        # Configure the Canvas, enable the scrolling of the Canvas using scrollbar (scroller), set scrollable region.
        scroll_option.configure(yscrollcommand=scroller.set, scrollregion=scroll_option.bbox("all"))

        commands = Frame(modify_buttons)    # Create a new Frame for the return button, fixed while scrolling
        commands.grid(column=1, row=3)

        return_button = Button(commands, text='Return', command=return_clicked) # Create a button to return to previous
        return_button.grid(column=1, row=1, pady=(10, 0))                       # menu using function return_clicked

    def delete_button(self):
        """Called when delete button is clicked in the habit menu, creates a list of buttons with habit names and grids
            buttons on the menu_frame"""
        def selected(habit_button):
            """Called when clicking one of the habit buttons, habit_button is an integer value used to identify the
                index of the selected habit within the habit_list"""
            confirm = tkinter.messagebox.askokcancel('Confirm',   # Ask user for confirmation before deleting data
                                                     f'Habit {habit_list[habit_button].name} '
                                                     f'will be deleted, THIS CANNOT BE UNDONE')
            if confirm:                             # If user confirms the variable received from the button press is
                del habit_list[habit_button]        # used as a list index to locate the selected habit. Use built in
                store_data(habit_list)              # method del to delete object from list. Call store_data form
                delete_buttons.destroy()            # scripts.data_handling to save new habit_list. Destroy
                valid = file_verification()         # delete_buttons frame. Verify if last habit in habits.json was
                if valid:                           # deleted. If valid, valid is true if habits.json contains at least
                    self.delete_button()            # 1 habit. Recreate delete_button Frame, updates buttons.
                    self.reset_stat_frame()         # Destroy and recreate the stat_frame.
                    self.main_stat_active()         # Recreates the main menu stats, stats will be updated.
                    self.reset_input_frame()        # Destroy and recreate the input_frame
                    self.add_frame()                # This will update names in duplicate list
                else:                               # If the last habit was removed
                    self.recreate()                 # Destroy the root window, recreate program, will mimic first run

        def return_clicked():
            """Called when return button is clicked, destroys the delete_button frame and recreates the
                habit_button frame"""
            self.habit_button()                 # Recreate the habit_button frame, previous Frame.
            delete_buttons.destroy()            # Destroy the modify_button frame.

        delete_buttons = Frame(self.menu_frame)             # Create the delete_buttons_frame, displayed after clicking
        delete_buttons.grid(row=1, column=2, padx=(30, 0))  # on the delete button in the start-up menu.

        labels = Frame(delete_buttons)                      # Create a frame to grid a label containing a prompt, fixed
        labels.grid(column=1, row=1)                        # while scrolling.

        remove_label = Label(labels, text="Select a habit to remove", width=20) # Label with prompt on label frame.
        remove_label.grid(column=1, row=1)

        habit_list = data_retrieval()               # Retrieve the list of habit objects for habits.json using
        list_of = []                                # data_retrieval form script.data_handling. Create an empty list to
        row = 0                                     # append buttons, row used to iterate buttons and grid them.

        scroll_option = Canvas(delete_buttons, width=130, height=140)  # Create a canvas to enable scrolling of a frame.
        scroll_option.grid(column=1, row=2, sticky=W)

        buttons = Frame(scroll_option)      # Create a frame to grid the habit buttons in list_of.

        scroller = Scrollbar(delete_buttons, command=scroll_option.yview)   # Create scrollbar and assign target.
        scroller.grid(column=1, row=2, sticky=N + S + E)

        for habit in habit_list:                            # Iterate the habits in the habit_list.
            list_of.append(Button(buttons,                  # Append the buttons to the empty list, set parameters for
                                  text=f'{habit.name}',     # the habit buttons.
                                  command=lambda habit_button=row: selected(habit_button),# Call function selected_habit
                                  bd=1,                                                   # and assign the row number
                                  relief='ridge',                                         # as the variable habit_button
                                  padx=35))
            list_of[row].grid(column=1, row=row + 1, pady=(0, 10), sticky=W + E)    # Grid button to first row.
            row += 1                                                                # Set row for next habit to grid.

        scroll_option.create_window(0, 0, window=buttons, anchor='n')   # Create the canvas with Frame buttons.
        scroll_option.update()                                          # Keep scroll active.
        # Configure the Canvas, enable the scrolling of the Canvas using scrollbar (scroller), set scrollable region.
        scroll_option.configure(yscrollcommand=scroller.set, scrollregion=scroll_option.bbox("all"))

        commands = Frame(delete_buttons)    # Create a new Frame for the return button, fixed while scrolling.
        commands.grid(column=1, row=3)

        return_button = Button(commands, text='Return', command=return_clicked) # Create a button to return to previous
        return_button.grid(column=1, row=1, pady=(10, 0))                       # menu using function return_clicked

    def stat_button(self):
        """Called when view additional stat button is clicked on the main screen, replaces the main screen buttons with
             3 new buttons, Detailed habit stats, Best and Worst and Habit frequency."""
        def detail_clicked():
            """Called when Detailed habit stats is clicked in the stat menu, creates a list of buttons with habit names
                and grids buttons on the menu_frame"""
            self.stat_selection()       # Calls method modify_button, creates list of buttons.
            stat_buttons.destroy()      # Destroy the habit_button frame.

        def performance_clicked():
            """On clicking of performance button the stat frame will be destroyed and recreated, and performance stats
                added to frame"""
            self.reset_stat_frame()     # Destroy and recreate stat frame.
            self.performance()          # Create and grid performance_frame on stat_frame.

        def frequency_clicked():
            """On clicking of frequency button the stat frame will be destroyed and recreated, and frequency stats
                added to frame"""
            self.reset_stat_frame()     # Destroy and recreate stat frame.
            self.frequency_button()     # Create and grid frequency_frame on stat_frame.

        def return_clicked():
            """Called when return button is clicked, destroys the stat_button frame and recreates the
                main_button frame"""
            stat_buttons.destroy()      # Destroy the stat_button frame.
            self.main_button_active()   # Recreate the main_button frame, previous Frame.

        stat_buttons = Frame(self.menu_frame)               # Create Frame for the habit buttons.
        stat_buttons.grid(row=1, column=1, padx=(30, 0))    # Grid Frame onto menu_frame.

        stat_label = Label(stat_buttons, text="What do you wish to do:")
        stat_label.grid(column=1, row=1, sticky=W + E, pady=(0, 10))    # Create a label with a prompt.

        detail_button = Button(stat_buttons,                      # Set parameters for the first button.
                               text='Detailed Habit Stats',
                               command=detail_clicked,            # Calls function detail_clicked when button is pressed.
                               bd=1,
                               relief='ridge',
                               pady=4)
        detail_button.grid(column=1, row=2, sticky=W + E, pady=10) # Add button to frame using grid.

        if file_verification():
            performance_button = Button(stat_buttons,                # Set parameters for the second button.
                                        text='View Best And Worst',
                                        command=performance_clicked, # Calls function performance_clicked when button is
                                        bd=1,                        # pressed.
                                        relief='ridge',
                                        pady=4)
            performance_button.grid(column=1, row=3, sticky=W + E, pady=(0, 10)) # Add button to frame using grid.
        else:
            performance_button = Button(stat_buttons,  # Set parameters for the second button, if nothing is logged
                                        text='View Best And Worst',
                                        state="disabled",
                                        bd=1,  # pressed.
                                        relief='ridge',
                                        pady=4)
            performance_button.grid(column=1, row=3, sticky=W + E, pady=(0, 10))  # Add button to frame using grid.

        frequency_button = Button(stat_buttons,                 # Set parameters for the third button.
                                  text='Habit Frequency',
                                  command=frequency_clicked,    # Calls function frequency_clicked when button is pressed.
                                  bd=1,
                                  relief='ridge',
                                  pady=4)
        frequency_button.grid(column=1, row=4, sticky=W + E)    # Add button to frame using grid.

        return_button = Button(stat_buttons, text='Return', command=return_clicked)
        return_button.grid(column=1, row=5, pady=(10, 0)) # Create and grid a return button, calls function return_clicked when clicked.

    def stat_selection(self):
        """Called when detail stat button is clicked in the stat menu, creates a list of buttons with habit names and
            grids buttons on the menu_frame"""
        def selected(habit_button):
            """Called when clicking one of the habit buttons, habit_button is an integer value used to identify the
                index of the selected habit within the habit_list"""
            habit_id = habit_button         # Set habit_id to value habit_button returned from button.
            self.reset_stat_frame()         # Destroy and recreate stat frame to remove previous gridded frames.
            self.stat_details(habit_id)     # Call method stat_detail to create a detail window for selected stat.

        def return_clicked():
            """Called when return button is clicked, destroys the delete_button frame and recreates the
                habit_button frame"""
            stat_select.destroy()   # Destroy the modify_button frame.
            self.stat_button()      # Recreate the habit_button frame, previous Frame.

        stat_select = Frame(self.menu_frame)             # Create the stat_select Frame, displayed after clicking
        stat_select.grid(row=1, column=1, padx=(30, 0))  # on the detail stat button in the stat menu.

        labels = Frame(stat_select)                     # Create a frame to grid a label containing a prompt, fixed
        labels.grid(column=1, row=1)                    # while scrolling.

        stat_label = Label(labels, text="Select a habit to view stats", width=20)   # Label with prompt on label frame.
        stat_label.grid(column=1, row=1)

        habit_list = data_retrieval()               # Retrieve the list of habit objects for habits.json using
        list_of = []                                # data_retrieval form script.data_handling. Create an empty list to
        row = 0                                     # append buttons, row used to iterate buttons and grid them.

        scroll_option = Canvas(stat_select, width=130, height=140)  # Create a canvas to enable scrolling of a frame.
        scroll_option.grid(column=1, row=2, sticky=W)

        buttons = Frame(scroll_option)      # Create a frame to grid the habit buttons in list_of.

        scroller = Scrollbar(stat_select, command=scroll_option.yview)  # Create scrollbar and assign target.
        scroller.grid(column=1, row=2, sticky=N + S + E)

        for habit in habit_list:                            # Iterate the habits in the habit_list.
            list_of.append(Button(buttons,                  # Append the buttons to the empty list, set parameters for
                                  text=f'{habit.name}',     # the habit buttons.
                                  command=lambda habit_button=row: selected(habit_button),# Call function selected_habit
                                  bd=1,                                                   # and assign the row number
                                  relief='ridge',                                         # as the variable habit_button
                                  padx=35))
            list_of[row].grid(column=1, row=row + 1, pady=(0, 10), sticky=W + E)    # Grid button to first row.
            row += 1                                                                # Set row for next habit to grid.

        scroll_option.create_window(0, 0, window=buttons, anchor='n')   # Create the canvas with Frame buttons.
        scroll_option.update()                                          # Keep scroll active.
        # Configure the Canvas, enable the scrolling of the Canvas using scrollbar (scroller), set scrollable region.
        scroll_option.configure(yscrollcommand=scroller.set, scrollregion=scroll_option.bbox("all"))

        commands = Frame(stat_select)    # Create a new Frame for the return button, fixed while scrolling.
        commands.grid(column=1, row=3)

        return_button = Button(commands, text='Return', command=return_clicked) # Create a button to return to previous
        return_button.grid(column=1, row=1, pady=(10, 0))                       # menu using function return_clicked

    def stat_details(self, habit_id):
        """Called when clicking one of the habit buttons, habit_button is an integer value used to identify the
            index of the selected habit within the habit_list"""
        def return_clicked():
            """Called when return button is clicked, destroys the stat_frame and recreates the stat_frame, then create
                main stat frame and add to grid on stat_frame"""
            stat_detail.destroy()           # Destroy stat_detail frame in the stat_frame.
            return_fix.destroy()            # Destroy the return fix frame, used to fix location of button.
            self.reset_stat_frame()         # Destroy and recreate stat_frame.
            self.main_stat_active()         # Call main_stat_active() to create and grid frame.

        stat_detail = Frame(self.stat_frame)            # Create frame for detailed stats, on the stat_frame.
        stat_detail.config(height=195, width=185)       # Set the size of the detail frame.
        stat_detail.grid_propagate(False)               # Remove detail_frame auto rescaling.
        stat_detail.grid(column=1, row=1)               # Grid the detail_frame onto the stat_frame.

        habit_list = data_retrieval()                   # Retrieve the list of objects.
        if habit_list[habit_id].complete == 'no':       # Check if selected habit is complete, determines displayed
            name = habit_list[habit_id].name            # stats. If the habit is not complete the only available stats
            frequency = habit_list[habit_id].frequency  # are the name and frequency of selected habit.
        else:
            name = habit_list[habit_id].name                        # Check if selected habit is complete, determines
            frequency = habit_list[habit_id].frequency              # displayed stats. If the habit is complete the
            current_streak = habit_list[habit_id].streak            # stats contain name, frequency, streak, longest
            longest_streak = habit_list[habit_id].longest_streak    # streak, add date, age and time since last log
            add_date = habit_list[habit_id].first_log               # of the selected habit.
            age = dt.datetime.now() - dt.datetime.strptime(habit_list[habit_id].first_log, '%Y-%m-%d %H:%M')
            since_log = dt.datetime.now() - dt.datetime.strptime(habit_list[habit_id].last_log, '%Y-%m-%d %H:%M')

            # Statistics only available for completed habits
            current_streak_label = Label(stat_detail, text='Current streak:')
            current_streak_label.grid(column=1, row=3)  # Create and grid label to identify the property displayed.

            current_streak_info = Label(stat_detail, text=current_streak, font='Helvetica 10 bold')
            current_streak_info.grid(column=2, row=3)   # Create and grid label with the property info.

            longest_streak_label = Label(stat_detail, text='Longest streak:')
            longest_streak_label.grid(column=1, row=4)  # Create and grid label to identify the property displayed.

            longest_streak_info = Label(stat_detail, text=longest_streak, font='Helvetica 10 bold')
            longest_streak_info.grid(column=2, row=4)   # Create and grid label with the property info.

            add_date_label = Label(stat_detail, text='Date added:')
            add_date_label.grid(column=1, row=5)    # Create and grid label to identify the property displayed.

            add_date_info = Label(stat_detail, text=add_date[:-5], font='Helvetica 10 bold')
            add_date_info.grid(column=2, row=5)     # Create and grid label with the property info.

            age_label = Label(stat_detail, text='Habit age:')
            age_label.grid(column=1, row=6)         # Create and grid label to identify the property displayed.

            age_info = Label(stat_detail, text=f'{str(age.days)} days', font='Helvetica 10 bold')
            age_info.grid(column=2, row=6)          # Create and grid label with the property info.

            last_log_label = Label(stat_detail, text='Time since last log:')
            last_log_label.grid(column=1, row=7)    # Create and grid label to identify the property displayed.

            last_log_info = Label(stat_detail, text=f'{str(since_log.days)} days', font='Helvetica 10 bold')
            last_log_info.grid(column=2, row=7)     # Create and grid label with the property info.

        # Statistics available for all habits
        name_label = Label(stat_detail, text='Habit name:')
        name_label.grid(column=1, row=1)        # Create and grid label to identify the property displayed.

        name_info = Label(stat_detail, text=name, font='Helvetica 10 bold')
        name_info.grid(column=2, row=1)         # Create and grid label with the property info.

        frequency_label = Label(stat_detail, text='Frequency:')
        frequency_label.grid(column=1, row=2)    # Create and grid label to identify the property displayed.

        frequency_info = Label(stat_detail, text=frequency, font='Helvetica 10 bold')
        frequency_info.grid(column=2, row=2)    # Create and grid label with the property info.

        return_fix = Frame(self.stat_frame)     # Create a frame that fixes button to same position regardless of number
        return_fix.grid(column=1, row=2)        # of properties displayed

        return_button = Button(return_fix, text='Return', command=return_clicked)# Create a button to return to main
        return_button.grid(column=1, row=1)                                      # stat menu using function return_clicked

    def performance(self):
        """Called when best and worst button is clicked in the stat menu, creates a frame on the stat_frame that
            displays the best and worst performing habit"""
        def return_clicked():
            """Called when return button is clicked, destroys the stat_frame and recreates the stat_frame, then create
                main stat frame and add to grid on stat_frame"""
            performance_button.destroy()        # Destroy stat_performance frame in the stat_frame.
            return_fix.destroy()                # Destroy the return fix frame, used to fix location of button.
            self.reset_stat_frame()             # Destroy and recreate stat_frame.
            self.main_stat_active()             # Call main_stat_active() to create and grid frame.

        performance_button = Frame(self.stat_frame)         # Create frame for habit performance, on the stat_frame.
        performance_button.config(height=195, width=185)    # Set the size of the performance frame.
        performance_button.grid_propagate(False)            # Remove performance_frame auto rescaling.
        performance_button.grid(column=1, row=1)            # Grid the performance_frame onto the stat_frame.

        habit_list = data_retrieval()           # Retrieve list of habit objects.
        name = 'No habits \n meet criteria'     # Set name to default string if no habit satisfies criteria
        daily_performance = 0                   # Create a criteria to verify if a habit performs worse than the next
        weekly_performance = 0                  # the performance is calculated using the days since a habit was created
        previous_daily = 0                      # and the amount of logs since. logs/days = performance.
        previous_weekly = 0                     # The value can't be zero, it can exceed 1, higher values signify better
        days = 0                                # performance, All values assigned to zero as we try to identify higher
        logs = 0                                # values.
        time_frame = ""

        for habit in habit_list:            # Iterate objects in habit_list.
            if habit.complete == 'yes':     # Assess complete habits and calculate the amount of logs vs days/weeks.
                first_log = dt.datetime.strptime(habit.first_log, '%Y-%m-%d %H:%M') # Retrieve first log date.
                all_logs = len(habit.all_logs)      # Find the number of logs recorded for an object.
                if habit.frequency == 'daily':      # Assess daily habits.
                    delta = math.ceil((dt.datetime.now() - first_log).days)    # Get the days since habit was created.
                    if delta == 0:
                        delta = 1   # If a log exist the minimum days can be 1
                    daily_performance = all_logs/delta      # Calculate the performance of the selected habit object.
                    if (daily_performance > weekly_performance and daily_performance > previous_daily and
                            previous_weekly < daily_performance):   # Compare current habit performance with previous.
                        name = habit.name       # Set the name for label to habit with the best performance.
                        time_frame = 'days'     # If the habit is daily set time frame to days.
                        days = delta            # Assign the days since habit creation of the best performing habit.
                        logs = all_logs         # Assign the number of logs for the best performing habit.
                        previous_daily = daily_performance # Save habit performance to be assessed in next iteration.
                else:
                    delta = math.ceil((dt.datetime.now() - first_log).days/7)  # Get the weeks since habit was created.
                    if delta == 0:
                        delta = 1   # If a log exist the minimum weeks can be 1
                    weekly_performance = all_logs / delta   # Calculate the performance of the selected habit object.
                    if (daily_performance < weekly_performance and weekly_performance > previous_weekly and
                            previous_daily < weekly_performance):   # Compare current habit performance with previous.
                        name = habit.name       # Set the name for label to habit with the best performance.
                        time_frame = 'weeks'    # If the habit is daily set time frame to days.
                        days = delta            # Assign the days since habit creation of the best performing habit.
                        logs = all_logs         # Assign the number of logs for the best performing habit.
                        previous_weekly = weekly_performance # Save habit performance to be assessed in next iteration.

        best_label = Label(performance_button, text='Best habit')
        best_label.grid(column=1, columnspan=2, row=1) # Create and grid label denoting the best habit.

        name_label = Label(performance_button, text='Habit name:')
        name_label.grid(column=1, row=2)    # Create and grid label for name property.

        name_info = Label(performance_button, text=name, font='Helvetica 10 bold')
        name_info.grid(column=2, row=2)     # Create and grid label with the best habit name.

        log_label = Label(performance_button, text='Logged:')
        log_label.grid(column=1, row=3)     # Create and grid label for total number of logs.

        log_info = Label(performance_button, text=f'{logs} times', font='Helvetica 10 bold')
        log_info.grid(column=2, row=3)      # Create and grid label with the total number of logs of the best habit.

        day_label = Label(performance_button, text='In:')
        day_label.grid(column=1, row=4)     # Create and grid label for total number of days.

        day_info = Label(performance_button, text=f'{days} {time_frame}', font='Helvetica 10 bold')
        day_info.grid(column=2, row=4)      # Create and grid label with the total number of days of the best habit.

        if name == 'No habits \n meet criteria':  # Use default string to un-grid labels if criteria was not satisfied.
            log_label.grid_forget()
            log_info.grid_forget()
            day_label.grid_forget()
            day_info.grid_forget()


        name = 'No habits \n meet criteria'     # Set name to default string if no habit satisfies criteria
        daily_performance = 1                   # Create a criteria to verify if a habit performs worse than the next
        weekly_performance = 1                  # the performance is calculated using the days since a habit was created
        previous_daily = 1                      # and the amount of logs since. logs/days = performance.
        previous_weekly = 1                     # The value can't be zero, it can exceed 1, higher values signify better
        days = 0                                # performance, All values assigned to 1 as we try to identify lower
        logs = 0                                # values.
        time_frame = ""

        for habit in habit_list:  # Iterate objects in habit_list.
            if habit.complete == 'yes':  # Assess complete habits and calculate the amount of logs vs days/weeks.
                first_log = dt.datetime.strptime(habit.first_log, '%Y-%m-%d %H:%M')  # Retrieve first log date.
                all_logs = len(habit.all_logs)  # Find the number of logs recorded for an object.
                if habit.frequency == 'daily':  # Assess daily habits.
                    delta = math.ceil((dt.datetime.now() - first_log).days)  # Get the days since habit was created.
                    if delta == 0:
                        delta = 1   # If a log exist the minimum days can be 1
                    daily_performance = all_logs / delta  # Calculate the performance of the selected habit object.
                    if (daily_performance < weekly_performance and daily_performance < previous_daily and
                            previous_weekly > daily_performance):  # Compare current habit performance with previous.
                        name = habit.name  # Set the name for label to habit with the best performance.
                        time_frame = 'days'  # If the habit is daily set time frame to days.
                        days = delta  # Assign the days since habit creation of the best performing habit.
                        logs = all_logs  # Assign the number of logs for the best performing habit.
                        previous_daily = daily_performance  # Save habit performance to be assessed in next iteration.
                else:
                    delta = math.ceil(
                        (dt.datetime.now() - first_log).days / 7)  # Get the weeks since habit was created.
                    if delta == 0:
                        delta = 1   # If a log exist the minimum weeks can be 1
                    weekly_performance = all_logs / delta  # Calculate the performance of the selected habit object.
                    if (daily_performance > weekly_performance and weekly_performance < previous_weekly and
                            previous_daily > weekly_performance):  # Compare current habit performance with previous.
                        name = habit.name  # Set the name for label to habit with the best performance.
                        time_frame = 'weeks'  # If the habit is daily set time frame to days.
                        days = delta  # Assign the days since habit creation of the best performing habit.
                        logs = all_logs  # Assign the number of logs for the best performing habit.
                        previous_weekly = weekly_performance  # Save habit performance to be assessed in next iteration.

        best_label = Label(performance_button, text='Worst habit')
        best_label.grid(column=1, columnspan=2, row=5)  # Create and grid label denoting the worst habit.

        name_label = Label(performance_button, text='Habit name:')
        name_label.grid(column=1, row=6)    # Create and grid label for name property.

        name_info = Label(performance_button, text=name, font='Helvetica 10 bold')
        name_info.grid(column=2, row=6)     # Create and grid label with the worst habit name.

        log_label = Label(performance_button, text='Logged:')
        log_label.grid(column=1, row=7)     # Create and grid label for total number of logs.

        log_info = Label(performance_button, text=f'{logs} times', font='Helvetica 10 bold')
        log_info.grid(column=2, row=7)      # Create and grid label with the total number of logs of the worst habit.

        day_label = Label(performance_button, text='In:')
        day_label.grid(column=1, row=8)     # Create and grid label for total number of days.

        day_info = Label(performance_button, text=f'{days} {time_frame}', font='Helvetica 10 bold')
        day_info.grid(column=2, row=8)      # Create and grid label with the total number of days of the worst habit.

        if name == 'No habits \n meet criteria': # Use default string to un-grid labels if criteria was not satisfied.
            log_label.grid_forget()
            log_info.grid_forget()
            day_label.grid_forget()
            day_info.grid_forget()

        return_fix = Frame(self.stat_frame)  # Create a frame that fixes button to same position regardless of number
        return_fix.grid(column=1, row=2)  # of properties displayed

        return_button = Button(return_fix, text='Return', command=return_clicked) # Create a button to return to main
        return_button.grid(column=1, row=1)                                       # stat menu using function return_clicked

    def frequency_button(self):
        """Called when frequency button is clicked in the stat menu, creates a frame on the stat_frame that
            displays the frequency of the habits in a Listbox"""
        def return_clicked():
            """Called when return button is clicked, destroys the stat_frame and recreates the stat_frame, then create
                main stat frame and add to grid on stat_frame"""
            frequency_list.destroy()        # Destroy the frequency frame.
            self.reset_stat_frame()         # Destroy the stat_frame and recreate it.
            self.main_stat_active()         # Create the main stat window and grid it onto stat_frame

        frequency_list = Frame(self.stat_frame)         # Create frame for habit frequency, on the stat_frame.
        frequency_list.config(height=227, width=185)    # Set the size of the frequency frame.
        frequency_list.grid_propagate(False)            # Remove frequency_frame auto rescaling.
        frequency_list.grid(row=1, column=1)            # Grid the frequency_frame onto the stat_frame.

        frequency_label = Label(frequency_list, text='Habit Frequency:')
        frequency_label.grid(row=1, column=1, columnspan=2)     # Create and grid frequency label.

        daily_label = Label(frequency_list, text='Daily Habits')
        daily_label.grid(row=2, column=1, sticky=W)             # Create and grid daily label.

        weekly_label = Label(frequency_list, text='Weekly Habits')
        weekly_label.grid(row=2, column=2, sticky=W)            # Create and grid weekly label.

        daily_habits = Listbox(frequency_list, font='Helvetica 10', height=7, width=11)
        daily_habits.grid(row=3, column=1, sticky=W)            # Create listbox to add daily habits.

        weekly_habits = Listbox(frequency_list, font='Helvetica 10', height=7, width=11)
        weekly_habits.grid(row=3, column=2, sticky=W)           # Create listbox to add weekly habits.

        habit_list = data_retrieval()       # Retrieve list of objects.

        for habit in habit_list:                # Iterate through the list of objects.
            if habit.frequency == 'weekly':     # Isolate weekly habits.
                weekly_habits.insert('end', habit.name)     # Add habit name to the end of the list box
            elif habit.frequency == 'daily':    # Isolate daily habits.
                daily_habits.insert('end', habit.name)      # Add habit name to the end of the list box

        return_button = Button(frequency_list, text='Return', command=return_clicked) # Create a button to return to main
        return_button.grid(row=4, column=1, columnspan=2)                             # stat menu using function return_clicked

    def add_frame(self):
        """Always displayed at startup, gives the user the ability to add habits through the user interface. Requires
            name, frequency and completion to add a habit. Name is supplied via an entry field and frequency and
            completion are radiobuttons, duplicate habit names are not permitted"""
        def my_callback(*args):
            """Monitor changes in user input to determine the state of the add button"""
            habit_name = name.get()             # Get habit name from entry field, done each time field changes
            habit_frequency = frequency.get()   # Get habit frequency from radiobutton, done each time field changes
            habit_completion = completion.get() # Get habit completion from radiobutton, done each time field changes
            if habit_name != '' and 1 <= habit_frequency <= 2 and 1 <= habit_completion <= 2:
                add.config(state='active')  # Set button active if no fields are unfilled.
            else:
                add.config(state='disabled')    # Set button disabled if any field is unfilled.
            for habit in habit_list:            # Iterate through list of habit objects.
                if habit.name == habit_name:        # If the current value of name entry field matches a habit.name in
                    add.config(state='disabled')    # list, the add button state will be disabled.
                    dup.grid(column=2, row=7, columnspan=4, sticky=W + N, pady=(0, 10), padx=(50, 0)) # Info label
                    break # Break for loop keeping label on grid
                if habit.name != habit_name and dup.grid_info() != {}:
                    dup.grid_forget() # If the name is change and no longer matches an existing name, remove label from
                                      # grid

        def add_clicked():
            """Called when the add button is clicked, only active if all fields are filled and the habit name is not
                that of an existing habit, only usable frame when not habit data exists"""
            habit = Habit()                         # Create object of Class Habit.
            habit_name = name.get()                 # Assign object name property using text from entry label.
            habit_frequency = frequency.get()       # Assign object frequency property using value from radiobuttons.
            habit_complete = completion.get()       # Assign object complete property using value from radiobuttons.
            habit.add(habit_name, habit_frequency, habit_complete) # Use method .add with variable from entry fields.
            habit_list.append(habit)                # complete property. Add/Append created habit to the list of habits
            store_data(habit_list)                  # retrieved from habits.json. Store data in habits.json.
            tkinter.messagebox.showinfo('Habit Added', f'{habit.name} added to tracker') # Information.
            add_frame.destroy()  # Destroy the add frame to clear data.
            self.recreate()  # Recreate application, updates all frames

        habit_list = data_retrieval()               # Retrieve habit list, used for duplicate handling and data storage.

        add_frame = Frame(self.input_frame)         # Create the add frame on the input_frame.
        add_frame.config(height=227, width=370)     # Set size of the add frame.
        add_frame.grid_propagate(False)             # Remove autoscaling from the add_frame.
        add_frame.grid(column=1, row=1)             # Grid onto input_frame.

        menu_label = Label(add_frame, text="Add")
        menu_label.grid(column=2, row=1, columnspan=4, pady=(0, 10))    # Information label (Add).

        add_name = Label(add_frame, text="Input habit name:")
        add_name.grid(column=2, row=2, sticky=W, pady=(10, 0), padx=(50, 0))    # User prompt label (Name).

        name = StringVar()
        name.trace_add('write', my_callback)    # Input trace used for duplicate handling and add button state.

        input_name = Entry(add_frame, width=20, textvariable=name)
        input_name.grid(column=3, row=2, columnspan=2, sticky=W, pady=(10, 0))  # Habit name entry field.

        add_frequency = Label(add_frame, text="Select habit frequency:")
        add_frequency.grid(column=2, row=3, sticky=W, padx=(50, 0))         # User prompt label (Frequency).

        frequency = IntVar()
        frequency.trace_add('write', my_callback)    # Input trace used for add button state.

        frequency_daily = Radiobutton(add_frame, text='Daily', variable=frequency, value=1)
        frequency_daily.grid(column=3, row=3, sticky=W)         # Frequency selection radiobutton 1 of 2

        frequency_weekly = Radiobutton(add_frame, text='Weekly', variable=frequency, value=2)
        frequency_weekly.grid(column=4, row=3, sticky=W)        # Frequency selection radiobutton 2 of 2

        add_complete = Label(add_frame, text="Status at time of adding:")
        add_complete.grid(column=2, row=4, sticky=W+S, padx=(50, 0))    # User prompt label (Completion).

        add_complete = Label(add_frame, text="Complete:")
        add_complete.grid(column=2, row=5, sticky=W+N, pady=(0, 10), padx=(50, 0)) # User prompt label (Completion).

        completion = IntVar()
        completion.trace_add('write', my_callback)  # Input trace used for add button state.

        complete_yes = Radiobutton(add_frame, text='Yes', variable=completion, value=1)
        complete_yes.grid(column=3, row=5, sticky=W+N, pady=(0, 10))    # Completion selection radiobutton 1 of 2

        complete_no = Radiobutton(add_frame, text='No', variable=completion, value=2)
        complete_no.grid(column=4, row=5, sticky=W+N, pady=(0, 10))     # Completion selection radiobutton 2 of 2

        add = Button(add_frame, text='Add', command=add_clicked)
        add.grid(column=3, row=6, columnspan=2, pady=(10, 0))       # Button to add habit, only active if all fields are
                                                                    # filled and name is not a duplicate.
        dup = Label(add_frame, text="This habit already exists")    # Information label (duplicate)

        my_callback()   # Function tracking changes in variable using .trace, used for duplicate handling and add
                        # button state.

    def edit_frame(self, habit_id):
        """Displayed when habit button is pressed in modify_button frame, gives the user the ability to modify habits
            through the user interface. Requires name and frequency to modify a habit. Name is supplied via an entry
            field and frequency with a radiobutton, the habit name can remain the same if frequency is changed, changing
            frequency will reset the habit. The habit can also be reset on this frame"""
        def my_callback(*args):
            """Monitor changes in user input to determine the state of the change button"""
            habit_name = new_name.get()         # Get habit name from entry field, done each time field changes
            habit_frequency = frequency.get()   # Get habit frequency from radiobutton, done each time field changes
            if habit_frequency == 1:            # Convert property to match object property, receive integer (1 or 2)
                frequency_string = 'daily'      # convert to string ('daily' or 'weekly')
            else:
                frequency_string = 'weekly'
            if habit_name != '' and 1 <= habit_frequency <= 2:
                change.config(state='active')   # Set button active if no fields are unfilled.
            else:
                change.config(state='disabled') # Set button disabled if any field is unfilled.
            for habit in habit_list:            # Iterate through list of habit objects.
                if habit.name == habit_name and habit_name != habit_object.name: # If input matches name of non-selected
                    change.config(state='disabled')                              # habit, set button state too disabled.
                    dup.grid(column=1, row=7, columnspan=4, sticky=W + N, pady=(0, 10), padx=(50, 0)) # Info label.
                    break   # Break for loop keeping label on grid
                if habit.name != habit_name and dup.grid_info() != {}:
                    dup.grid_forget() # If the name is change and no longer matches an existing name, remove label from
                                      # grid
                if habit_object.frequency == frequency_string and habit_name == habit_object.name:
                    change.config(state='disabled') # New input matches existing habit information, button disabled
                    unchanged.grid(column=1, row=7, columnspan=4, sticky=W + N, pady=(0, 10), padx=(50, 0)) # Info label
                    break # Break for loop keeping label on grid
                if habit.name != habit_name and unchanged.grid_info() != {}:
                    unchanged.grid_forget() # If the name or frequency is change and no longer matches the existing
                                            # information, remove label from grid.

        def reset_clicked():
            """Removes all log information from the selected habit, habit will be stored as an incomplete habit, this
                cannot be undone"""
            habit_object.reset()        # Call method .reset removes all log data.
            store_data(habit_list)      # Store the habit list containing the reset object.
            edit_frame.destroy()        # Destroy the edit frame.
            self.reset_input_frame()    # Destroy and recreate the input_frame.
            self.add_frame()            # Create add_frame and place on grid.
            self.reset_stat_frame()     # Destroy and recreate the stat_frame.
            self.main_stat_active()     # Create main_stat_frame and place on grid, refreshes stats.

        def change_clicked():
            """Change name or frequency of a habit, or both. if frequency is changed all log information for the
                selected habit will be deleted, habit will be stored as an incomplete habit, this cannot be undone, name
                can't be changed to that of an existing habit, name change will not reset progress"""
            habit_object.change(name=new_name.get(), frequency=frequency.get())     # Use method .change with new inputs
            store_data(habit_list)      # Store the habit list containing the modified object.
            edit_frame.destroy()        # Destroy the edit frame.
            self.reset_input_frame()    # Destroy and recreate the input_frame.
            self.add_frame()            # Create add_frame and place on grid.
            self.reset_stat_frame()     # Destroy and recreate the stat_frame.
            self.main_stat_active()     # Create main_stat_frame and place on grid, refreshes stats.

        def return_clicked():
            """Called when return button is clicked, destroys the edit_frame and input_frame recreates the input_frame,
                then create add_frame and add to grid on input_frame"""
            edit_frame.destroy()        # Destroy the edit Frame.
            self.reset_input_frame()    # Destroy and recreate input frame, destroy all elements on grid
            self.add_frame()            # Create the add Frame and add to grid

        habit_list = data_retrieval()          # Retrieve list of objects.
        habit_object = habit_list[habit_id]    # Retrieve selected object from list.

        edit_frame = Frame(self.input_frame)        # Create the edit frame.
        edit_frame.config(height=227, width=370)    # Set size of edit frame.
        edit_frame.grid_propagate(False)            # Remove edit_frame auto rescaling
        edit_frame.grid(column=1, row=1)            # Add edit_frame to grid

        menu_label = Label(edit_frame, text="Modify")
        menu_label.grid(column=1, row=1, columnspan=4, pady=(0, 10)) # Information label (Modify).

        add_name = Label(edit_frame, text=f"Input new name for {habit_object.name}:")
        add_name.grid(column=1, row=2, sticky=W, pady=(10, 0), padx=(50, 0)) # User prompt label (New Name).

        new_name = StringVar()
        new_name.trace_add('write', my_callback) # Input trace used for duplicate handling and change button state.

        input_new_name = Entry(edit_frame, width=20, textvariable=new_name)
        input_new_name.grid(column=2, row=2, columnspan=2, sticky=W, pady=(10, 0))  # Habit name entry field.

        add_frequency = Label(edit_frame, text="Select habit frequency:")
        add_frequency.grid(column=1, row=3, sticky=W, padx=(50, 0))     # User prompt label (Frequency).

        frequency = IntVar()
        frequency.trace_add('write', my_callback)       # Input trace used for change button state.

        frequency_daily = Radiobutton(edit_frame, text='Daily', variable=frequency, value=1)
        frequency_daily.grid(column=2, row=3, sticky=W)     # Frequency selection radiobutton 1 of 2

        frequency_weekly = Radiobutton(edit_frame, text='Weekly', variable=frequency, value=2)
        frequency_weekly.grid(column=3, row=3, sticky=W)    # Frequency selection radiobutton 2 of 2

        change = Button(edit_frame, text='Change', command=change_clicked)
        change.grid(column=3, row=4, pady=(10, 0))  # Button to modify habit, only active if all fields are filled and
                                                    # name is not a duplicate.

        reset = Button(edit_frame, text='Reset', command=reset_clicked)
        reset.grid(column=2, row=4, pady=(10, 0))   # Button to reset a habit, deletes all log data.

        return_button = Button(edit_frame, text='Return', command=return_clicked)
        return_button.grid(column=1, row=4, pady=(10, 0)) # Button returns to previous frame.

        dup = Label(edit_frame, text="This habit already exists")   # Information label.
        unchanged = Label(edit_frame, text="The inputs match the existing habit") # Information label.

        my_callback()   # Function tracking changes in variable using .trace, used for duplicate handling and change
                        # button state.