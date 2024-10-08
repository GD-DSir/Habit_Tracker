import datetime as dt
import tkinter.messagebox


class Habit:
    def __init__(self):
        self.name = str
        self.frequency = str
        self.complete = str
        self.streak = int
        self.streak_start = dt
        self.longest_streak = int
        self.first_log = dt
        self.last_log = dt
        self.all_logs = list

    def to_object(self, habit_dict: dict):
        if habit_dict["complete"] == 'yes':
            self.name = habit_dict["name"]
            self.frequency = habit_dict["frequency"]
            self.complete = habit_dict["complete"]
            self.streak = habit_dict["streak"]
            self.streak_start = habit_dict["streak_start"]
            self.longest_streak = habit_dict["longest_streak"]
            self.first_log = habit_dict["first_log"]
            self.last_log = habit_dict["last_log"]
            self.all_logs = habit_dict["all_logs"]
        else:
            self.name = habit_dict["name"]
            self.frequency = habit_dict["frequency"]
            self.complete = habit_dict["complete"]

    def log(self):
        if self.complete == 'no':
            self.complete = 'yes'
            self.first_log = dt.datetime.now().strftime('%Y-%m-%d %H:%M')
            self.streak = 1
            self.streak_start = self.first_log
            self.longest_streak = 1
            self.last_log = self.first_log
            self.all_logs = [self.first_log]
            tkinter.messagebox.showinfo('Success',
                                        f'{self.name} was successfully logged,\n '
                                        f'current streak {self.streak}')

        else:
            self.last_log = dt.datetime.now().strftime('%Y-%m-%d %H:%M')
            self.all_logs.append(self.last_log)

            last_log = dt.datetime.strptime(self.last_log, '%Y-%m-%d %H:%M')
            streak_start = dt.datetime.strptime(self.streak_start, '%Y-%m-%d %H:%M')
            if last_log - streak_start <= dt.timedelta(days=self.streak + 1) and self.frequency == 'daily':
                self.streak = self.streak + 1
                tkinter.messagebox.showinfo('Success',
                                            f'{self.name} was successfully logged,\n '
                                            f'current streak {self.streak}')

            elif last_log - streak_start <= dt.timedelta(days=8) and self.frequency == 'weekly':
                self.streak = self.streak + 1
                tkinter.messagebox.showinfo('Success',
                                            f'{self.name} was successfully logged,\n '
                                            f'current streak {self.streak}')

            else:
                self.streak_start = dt.datetime.now().strftime('%Y-%m-%d %H:%M')
                tkinter.messagebox.showinfo('Success',
                                            f'\nThe current streak for {self.name} has reset, '
                                            f'was {self.streak} currently {1}\n')
                self.streak = 1

    def change(self, name, frequency):
        if frequency == 1:
            new_frequency = "daily"
            if new_frequency == self.frequency:
                frequency_string = ""
            else:
                frequency_string = f'Change {self.frequency} to {new_frequency}'

        else:
            new_frequency = "weekly"
            if new_frequency == self.frequency:
                frequency_string = ""
            else:
                frequency_string = f'Change {self.frequency} to {new_frequency}'
        if name == self.name:
            name_string = ""
        else:
            name_string = f'Change {self.name} to {name}'

        confirm = tkinter.messagebox.askyesno('Confirm',
                                              f'For {self.name}\n'
                                              f'{name_string}\n'
                                              f'{frequency_string}')
        if confirm:
            if new_frequency != self.frequency:
                reset = self.reset()
                if reset:
                    self.name = name
                    self.frequency = new_frequency
            else:
                self.name = name
                self.frequency = new_frequency

    def reset(self):
        confirm = tkinter.messagebox.askokcancel('Confirm',
                                                 f'Data for {self.name} will be deleted, THIS CANNOT BE UNDONE')
        if confirm:
            if self.complete == 'yes':
                self.complete = 'no'
                del self.streak
                del self.first_log
                del self.last_log
                del self.longest_streak
                del self.streak_start
                del self.all_logs

        return confirm


