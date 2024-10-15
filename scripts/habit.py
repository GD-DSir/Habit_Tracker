import datetime as dt
import math
import tkinter.messagebox


class Habit:
    """Creates a habit object that can be modified and inspected within the habit tracker interface"""
    def __init__(self):
        self.name = str
        """The name of a habit object"""
        self.frequency = str
        """The frequency of a habit object, either 'daily' or 'weekly'"""
        self.complete = str
        """The state of a habit when adding, was the habit complete at time of adding or not? 'yes' or 'no' If 'yes' 
        then the habit will have log properties, if 'no' only name, frequency and completion"""
        self.streak = int
        """The current valid streak of the habit"""
        self.streak_start = dt
        """The start time of the current valid streak of the habit"""
        self.longest_streak = int
        """The longest historical streak of the habit"""
        self.first_log = dt
        """The date and time the habit was logged for the first time"""
        self.last_log = dt
        """The date and time the habit was last logged"""
        self.all_logs = list
        """A list containing every log since the first log"""

    def to_object(self, habit_dict: dict):
        """Used to convert a dictionary to a habit object. Data is stored as dictionaries in a file habits.json, the
        method is called to convert entries in habits.json to objects"""
        if habit_dict["complete"] == 'yes':                 # Create complete habits based on the complete property.
            self.name = habit_dict["name"]
            self.frequency = habit_dict["frequency"]
            self.complete = habit_dict["complete"]
            self.streak = habit_dict["streak"]
            self.streak_start = habit_dict["streak_start"]
            self.longest_streak = habit_dict["longest_streak"]
            self.first_log = habit_dict["first_log"]
            self.last_log = habit_dict["last_log"]
            self.all_logs = habit_dict["all_logs"]
        else:                                           # Create incomplete habits based on the complete property.
            self.name = habit_dict["name"]
            self.frequency = habit_dict["frequency"]
            self.complete = habit_dict["complete"]

    def log(self):
        """Logs a habit selected in the habit tracker interface"""
        if self.complete == 'no':           # For an incomplete habit, record a first log
            self.complete = 'yes'           # Change habit completion
            self.first_log = dt.datetime.now().strftime('%Y-%m-%d %H:%M')
            self.streak = 1
            self.streak_start = self.first_log
            self.longest_streak = 1
            self.last_log = self.first_log
            self.all_logs = [self.first_log]
            tkinter.messagebox.showinfo('Success',
                                        f'{self.name} was successfully logged,\n '
                                        f'current streak {self.streak}') # Inform user.

        else:       # For a complete habit, record a log
            time_since = dt.datetime.now() - dt.datetime.strptime(self.last_log, '%Y-%m-%d %H:%M')
            if time_since > dt.timedelta(hours=10) and self.frequency == 'daily':  # Prevent habit being logged twice.
                self.last_log = dt.datetime.now().strftime('%Y-%m-%d %H:%M')       # Set new log time.
                self.all_logs.append(self.last_log)                                # Add new log to historical data.

                last_log = dt.datetime.strptime(self.last_log, '%Y-%m-%d %H:%M')    # Convert property to dt object.
                streak_start = dt.datetime.strptime(self.streak_start, '%Y-%m-%d %H:%M') # Convert property to dt object.
                # Verify streak validity, the days since streak start can only be 1 above the streak value for daily habits.
                if last_log - streak_start <= dt.timedelta(days=self.streak + 1):
                    self.streak = self.streak + 1                       # Increase streak value if streak is valid
                    tkinter.messagebox.showinfo('Success',
                                                f'{self.name} was successfully logged,\n '
                                                f'current streak {self.streak}') # Information pop-up

                else:   # Streak not valid, reset streak to 1 and set new streak start.
                    self.streak_start = dt.datetime.now().strftime('%Y-%m-%d %H:%M')
                    tkinter.messagebox.showinfo('Success',
                                                f'\nThe current streak for {self.name} has reset, '
                                                f'was {self.streak} currently {1}\n') # Information pop-up
                    self.streak = 1

                if self.longest_streak <= self.streak:
                    self.longest_streak = self.streak   # Set longest streak value to current streak if it exceeds
                                                        # historical best.

            elif time_since > dt.timedelta(days=6) and self.frequency == 'weekly':    # Prevent habit being logged twice.
                self.last_log = dt.datetime.now().strftime('%Y-%m-%d %H:%M')        # Set new log time.
                self.all_logs.append(self.last_log)                                 # Add new log to historical data.

                last_log = dt.datetime.strptime(self.last_log, '%Y-%m-%d %H:%M')    # Convert property to dt object.
                streak_start = dt.datetime.strptime(self.streak_start, '%Y-%m-%d %H:%M') # Convert property to dt object.
                # Verify streak validity, the days since streak start should be within 7*steak days.
                if last_log - streak_start <= dt.timedelta(days=self.streak*7, hours=12):
                    self.streak = self.streak + 1                   # Increase streak value if streak is valid
                    tkinter.messagebox.showinfo('Success',
                                                f'{self.name} was successfully logged,\n '
                                                f'current streak {self.streak}')    # Information pop-up

                else:   # Streak not valid, reset streak to 1 and set new streak start.
                    self.streak_start = dt.datetime.now().strftime('%Y-%m-%d %H:%M')
                    tkinter.messagebox.showinfo('Success',
                                                f'\nThe current streak for {self.name} has reset, '
                                                f'was {self.streak} currently {1}\n') # Information pop-up
                    self.streak = 1

                if self.longest_streak <= self.streak:
                    self.longest_streak = self.streak   # Set longest streak value to current streak if it exceeds
                                                        # historical best.

            else:   # Habit was logged recently, inform user.
                days = time_since.days
                total_minutes = time_since.seconds/60
                hours = math.floor(total_minutes/60)
                minutes = math.floor(total_minutes - hours*60)
                if self.frequency == "daily":
                    tkinter.messagebox.showwarning('Failed',
                                                f'\n{self.name} was logged {hours}h:{minutes}m ago\n'
                                                         f'Please try again later')
                else:
                    tkinter.messagebox.showwarning('Failed',
                                                   f'\n{self.name} was logged {days}d:{hours}h ago\n'
                                                   f'Please try again later')

    def add(self, name, frequency, complete):
        """Add a habit \n
            name:[str] = 'name_of_habit'\n
            frequency:[int] = 1 or 2:
            \t- frequency = 1: daily
            \t- frequency = 2: weekly \n
            completion:[int] = 1 or 2:
            \t- completion = 1: True
            \t- completion = 2: False"""

        self.name = name

        if frequency == 1:                  # Value recorded with tkinter radiobutton (1 or 2).
            self.frequency = 'daily'        # If value is 1 then frequency is daily.
        else:
            self.frequency = 'weekly'       # If value is 2 then frequency is weekly.

        if complete == 1:                   # Value recorded with tkinter radiobutton (1 or 2).
            self.complete = 'yes'           # If value is 1 then habit is completed.
            self.first_log = dt.datetime.now().strftime(
                '%Y-%m-%d %H:%M')               # Completed habits have more properties than incomplete
            self.last_log = self.first_log      # habits.
            self.all_logs = [self.first_log]    # As this is a new habit, logged for first time.
            self.streak_start = self.first_log  # first_log = last_log = all_log = streak_start = now()
            self.streak = 1                     # Streak is 1
            self.longest_streak = 1             # Longest streak is 1
        else:
            self.complete = 'no'

    def change(self, name, frequency):
        """Modify a habit \n
                    name:[str] = 'name_of_habit'\n
                    frequency:[int] = 1 or 2:
                    \t- frequency = 1: daily
                    \t- frequency = 2: weekly \n"""
        if frequency == 1:
            new_frequency = "daily"     # Convert to match object property.
            if new_frequency == self.frequency:
                frequency_string = ""   # String for information pop-up.
            else:
                frequency_string = f'Change {self.frequency} to {new_frequency}' # String for information pop-up

        else:
            new_frequency = "weekly"    # Convert to match object property.
            if new_frequency == self.frequency:
                frequency_string = "" # String for information pop-up.
            else:
                frequency_string = f'Change {self.frequency} to {new_frequency}' # String for information pop-up
        if name == self.name:
            name_string = "" # String for information pop-up
        else:
            name_string = f'Change {self.name} to {name}' # String for information pop-up

        confirm = tkinter.messagebox.askyesno('Confirm',
                                              f'For {self.name}\n'
                                              f'{name_string}\n'
                                              f'{frequency_string}') # Ask user for confirmation
        if confirm:
            if new_frequency != self.frequency: # If frequency changes reset habit.
                reset = self.reset()
                if reset:
                    self.name = name
                    self.frequency = new_frequency
            else:
                self.name = name
                self.frequency = new_frequency

    def reset(self):
        # Ask for confirmation.
        confirm = tkinter.messagebox.askokcancel('Confirm',
                                                 f'Data for {self.name} will be deleted, THIS CANNOT BE UNDONE')
        if confirm:                             # User confirmed following properties will be removed.
            if self.complete == 'yes':
                self.complete = 'no'
                del self.streak
                del self.first_log
                del self.last_log
                del self.longest_streak
                del self.streak_start
                del self.all_logs

        return confirm


