from tkinter import *
import tkinter.messagebox
from scripts.data_handling import *
import datetime as dt


class GUI:
    def __init__(self):

        # tk root_window Config
        self.root = Tk()                                # Create root_window
        self.root.title('Habit Tracker')                # root_window title
        self.root.geometry('800x267+10+10')             # Fix the size of root_window
        self.root.config(padx=50, pady=20)              # Padding of root_window

        # stats_frame (Column 1) Config
        self.stat_frame = Frame(self.root)               # Create stat_frame
        self.stat_frame.grid(column=1, row=1)            # Grid stat_frame in column 1 of root_window
        self.stat_frame.config(height=227, width=185)    # Configure the size of stat_frame
        self.stat_frame.grid_propagate(False)            # Remove stat_frame auto rescaling

        # menu_frame (Column 2) Config
        self.menu_frame = Frame(self.root)               # Create menu_frame
        self.menu_frame.grid(column=2, row=1)            # Grid menu_frame in column 2 of root_window
        self.menu_frame.config(height=227, width=190)    # Configure the size of menu_frame
        self.menu_frame.grid_propagate(False)            # Remove menu_frame auto rescaling

        # input_frame (Column 3) Config
        self.input_frame = Frame(self.root)               # Create input_frame
        self.input_frame.grid(column=3, row=1)            # Grid input_frame in column 3 of root_window
        self.input_frame.config(height=227, width=370)    # Configure the size of input_frame
        self.input_frame.grid_propagate(False)            # Remove input_frame auto rescaling

    def create_window(self):
        valid = file_verification()
        self.add_frame()
        if valid:
            self.main_button_active()
            self.main_stat_active()
        else:
            self.main_button_inactive()
            self.main_stat_inactive()
        self.root.mainloop()

    def recreate(self):
        self.root.destroy()
        self.__init__()
        self.create_window()

    def reset_stat_frame(self):
        self.stat_frame.destroy()
        self.stat_frame = Frame(self.root)  # Create stat_frame
        self.stat_frame.grid(column=1, row=1)  # Grid stat_frame in column 1 of root_window
        self.stat_frame.config(height=227, width=185)  # Configure the size of stat_frame
        self.stat_frame.grid_propagate(False)

    def main_stat_active(self):
        main_stat_frame = Frame(self.stat_frame)
        main_stat_frame.grid(column=1, row=1)
        main_stat_frame.config(height=227, width=185)
        main_stat_frame.grid(column=1, row=1)

        habit_list = data_retrieval()
        name = ""
        longest_streak = 0

        longest_streak_label = Label(main_stat_frame, text="All Time Longest Streak:", font='Helvetica 8 bold')
        longest_streak_label.grid(column=1, row=1)

        for habit in habit_list:
            if habit.complete == 'yes':
                if habit.longest_streak > longest_streak:
                    longest_streak = habit.longest_streak
                    name = habit.name

        long_all_label = Label(main_stat_frame, text=f"Habit: {name}\n"
                                                     f"{longest_streak} Times")
        long_all_label.grid(column=1, row=2, sticky=N)

        current_streak = 0

        current_streak_label = Label(main_stat_frame, text="Current Longest Streak:", font='Helvetica 8 bold')
        current_streak_label.grid(column=1, row=3)

        for habit in habit_list:
            if habit.complete == 'yes':
                if habit.streak > current_streak:
                    current_streak = habit.streak
                    name = habit.name

        current_streak_info = Label(main_stat_frame, text=f"Habit: {name}\n"
                                                          f"{current_streak} Times")
        current_streak_info.grid(column=1, row=4, sticky=N)

        oldest = dt.timedelta(days=0)

        oldest_label = Label(main_stat_frame, text="Oldest Habit:", font='Helvetica 8 bold')
        oldest_label.grid(column=1, row=5)

        for habit in habit_list:
            if habit.complete == 'yes':
                delta = dt.datetime.now() - dt.datetime.strptime(habit.first_log, '%Y-%m-%d %H:%M')
                if delta > oldest:
                    oldest = delta
                    name = habit.name

        oldest_label_info = Label(self.stat_frame, text=f"Habit: {name}\n"
                                                        f"First logged {str(oldest)[:-10]} ago")
        oldest_label_info.grid(column=1, row=6, sticky=N)

    def main_stat_inactive(self):
        main_stat_frame = Frame(self.stat_frame)
        main_stat_frame.grid(row=1, column=1)

        no_habit = Label(main_stat_frame, text="No Habits Added")
        no_habit.grid(column=1, row=1)
        nothing_label = Label(main_stat_frame, text="Add habits to start Tracking")
        nothing_label.grid(column=1, row=2, pady=160/2)

    def main_button_active(self):
        def to_log_frame():
            main_button_frame.destroy()
            self.log_button()

        def to_habit_frame():
            main_button_frame.destroy()
            self.habit_button()

        main_button_frame = Frame(self.menu_frame)
        main_button_frame.grid(column=1, row=1, padx=(30, 0))

        main_menu_label = Label(main_button_frame, text="What do you wish to do:")
        main_menu_label.grid(column=1, row=1, sticky=W + E, pady=(0, 10))

        log_menu = Button(main_button_frame,
                          text='Log Progress',
                          command=to_log_frame,
                          bd=1,
                          relief='ridge',
                          pady=10)
        log_menu.grid(column=1, row=2, sticky=W + E, pady=10)

        habit_menu = Button(main_button_frame,
                            text='Open habit menu',
                            command=to_habit_frame,
                            bd=1,
                            relief='ridge',
                            pady=10)
        habit_menu.grid(column=1, row=3, sticky=W + E, pady=(0, 10))

        stat_menu = Button(main_button_frame,
                           text='View Additional Stats',
                           command=self.stat_button,
                           bd=1,
                           relief='ridge',
                           pady=10)
        stat_menu.grid(column=1, row=4, sticky=W + E)

    def main_button_inactive(self):
        main_button_frame = Frame(self.menu_frame)
        main_button_frame.grid(column=1, row=1, padx=(30, 0))

        main_menu_label = Label(main_button_frame, text="Add a habit to access menus:")
        main_menu_label.grid(column=1, row=1, sticky=W + E, pady=(0, 10))

        log_menu = Button(main_button_frame,
                          text='Log Progress',
                          bd=1,
                          relief='ridge',
                          pady=10,
                          state='disabled')
        log_menu.grid(column=1, row=2, sticky=W + E, pady=10)

        habit_menu = Button(main_button_frame,
                            text='Open habit menu',
                            bd=1,
                            relief='ridge',
                            pady=10,
                            state='disabled')
        habit_menu.grid(column=1, row=3, sticky=W + E, pady=(0, 10))

        stat_menu = Button(main_button_frame,
                           text='View stats',
                           bd=1,
                           relief='ridge',
                           pady=10,
                           state='disabled')
        stat_menu.grid(column=1, row=4, sticky=W + E)

    def log_button(self):
        def selected(habit_button):
            selected_habit = habit_button
            habit_object = habit_list[selected_habit]
            confirm = tkinter.messagebox.askyesno('Confirm',
                                                  f'Log habit {habit_object.name}')
            if confirm:
                habit_object.log()
                store_data(habit_list)
                log_buttons.destroy()
                self.log_button()
                self.reset_stat_frame()
                self.main_stat_active()

        def return_clicked():
            self.main_button_active()
            log_buttons.destroy()

        log_buttons = Frame(self.menu_frame)
        log_buttons.grid(column=1, row=1, padx=(30, 0))

        labels = Frame(log_buttons)
        labels.grid(column=1, row=1)

        log_label = Label(labels, text="Select a habit to log", width=20)
        log_label.grid(column=1, row=1)

        habit_list = data_retrieval()
        list_of = []
        key = 0

        scroll_option = Canvas(log_buttons, width=130, height=140)
        scroll_option.grid(column=1, row=2, sticky=W)

        buttons = Frame(scroll_option)

        scroller = Scrollbar(log_buttons, command=scroll_option.yview)
        scroller.grid(column=1, row=2, sticky=N + S + E)

        for habit in habit_list:
            list_of.append(Button(buttons,
                                  text=f'{habit.name}',
                                  command=lambda habit_button=key: selected(habit_button),
                                  bd=1,
                                  relief='ridge',
                                  padx=35))
            list_of[key].grid(column=1, row=key + 1, pady=(0, 10), sticky=W + E)
            key += 1

        scroll_option.create_window(0, 0, window=buttons, anchor='n')
        scroll_option.update()
        scroll_option.configure(yscrollcommand=scroller.set, scrollregion=scroll_option.bbox("all"))

        commands = Frame(log_buttons)
        commands.grid(column=1, row=3)

        return_button = Button(commands, text='Return', command=return_clicked)
        return_button.grid(column=2, row=1, pady=(10, 0))

    def habit_button(self):
        def modify_clicked():
            habit_buttons.destroy()
            self.modify_button()

        def delete_clicked():
            habit_buttons.destroy()
            self.delete_button()

        def return_clicked():
            self.main_button_active()
            habit_buttons.destroy()

        habit_buttons = Frame(self.menu_frame)
        habit_buttons.grid(column=1, row=1, padx=(30, 0))

        habit_menu_label = Label(habit_buttons, text="What do you wish to do:")
        habit_menu_label.grid(column=1, row=1, sticky=W + E, pady=(0, 10))

        edit_menu = Button(habit_buttons,
                           text='Modify a Habit',
                           command=modify_clicked,
                           bd=1,
                           relief='ridge',
                           pady=10)
        edit_menu.grid(column=1, row=2, sticky=W + E, pady=10)

        remove_menu = Button(habit_buttons, text='Remove a Habit', command=delete_clicked, bd=1, relief='ridge',
                             pady=10)
        remove_menu.grid(column=1, row=3, sticky=W + E, pady=(0, 10))

        return_button = Button(habit_buttons, text='Return', command=return_clicked, pady=10)
        return_button.grid(column=1, row=4)

    def modify_button(self):
        def selected(habit_button):
            habit_id = habit_button
            self.edit_frame(habit_id)

        def return_clicked():
            self.habit_button()
            modify_buttons.destroy()

        modify_buttons = Frame(self.menu_frame)
        modify_buttons.grid(row=1, column=1, padx=(30, 0))

        modify_buttons = Frame(self.menu_frame)
        modify_buttons.grid(row=1, column=1, padx=(30, 0))

        labels = Frame(modify_buttons)
        labels.grid(column=1, row=1)

        modify_label = Label(labels, text="Select a habit to modify", width=20)
        modify_label.grid(column=1, row=1)

        habit_list = data_retrieval()
        list_of = []
        key = 0

        scroll_option = Canvas(modify_buttons, width=130, height=140)
        scroll_option.grid(column=1, row=2, sticky=W)

        buttons = Frame(scroll_option)

        scroller = Scrollbar(modify_buttons, command=scroll_option.yview)
        scroller.grid(column=1, row=2, sticky=N + S + E)

        for habit in habit_list:
            list_of.append(Button(buttons,
                                  text=f'{habit.name}',
                                  command=lambda habit_button=key: selected(habit_button),
                                  bd=1,
                                  relief='ridge',
                                  padx=35))
            list_of[key].grid(column=1, row=key + 1, pady=(0, 10), sticky=W + E)
            key += 1

        scroll_option.create_window(0, 0, window=buttons, anchor='n')
        scroll_option.update()
        scroll_option.configure(yscrollcommand=scroller.set, scrollregion=scroll_option.bbox("all"))

        commands = Frame(modify_buttons)
        commands.grid(column=1, row=3)

        return_button = Button(commands, text='Return', command=return_clicked)
        return_button.grid(column=1, row=1, pady=(10, 0))

    def edit_frame(self, habit_id):

        def my_callback(*args):
            habit_name = new_name.get()
            habit_frequency = frequency.get()
            if habit_frequency == 1:
                frequency_string = 'daily'
            else:
                frequency_string = 'weekly'
            if habit_name != '' and 1 <= habit_frequency <= 2:
                change.config(state='active')
            else:
                change.config(state='disabled')
            for habit in habit_list:
                if habit.name == habit_name and habit_name != habit_object.name:
                    change.config(state='disabled')
                    dup.grid(column=1, row=7, columnspan=4, sticky=W + N, pady=(0, 10), padx=(50, 0))
                    break
                if habit.name != habit_name and dup.grid_info() != {}:
                    dup.grid_forget()
            for habit in data_retrieval():
                if habit_object.frequency == frequency_string and habit_name == habit_object.name:
                    change.config(state='disabled')
                    unchanged.grid(column=1, row=7, columnspan=4, sticky=W + N, pady=(0, 10), padx=(50, 0))
                    break
                if habit.name != habit_name and unchanged.grid_info() != {}:
                    unchanged.grid_forget()

        def reset_clicked():
            habit_object.reset()
            store_data(habit_list)
            self.add_frame()
            edit_frame.destroy()
            self.reset_stat_frame()
            self.main_stat_active()

        def change_clicked():
            habit_object.change(name=new_name.get(), frequency=frequency.get())
            store_data(habit_list)
            edit_frame.destroy()
            self.reset_stat_frame()
            self.main_stat_active()

        def return_clicked():
            edit_frame.destroy()
            self.add_frame()

        habit_list = data_retrieval()
        habit_object = habit_list[habit_id]

        edit_frame = Frame(self.input_frame)
        edit_frame.config(height=227, width=370)
        edit_frame.grid_propagate(False)
        edit_frame.grid(column=1, row=1)

        menu_label = Label(edit_frame, text="Modify")
        menu_label.grid(column=1, row=1, columnspan=4, pady=(0, 10))

        add_name = Label(edit_frame, text=f"Input new name for {habit_object.name}:")
        add_name.grid(column=1, row=2, sticky=W, pady=(10, 0), padx=(50, 0))

        new_name = StringVar()
        new_name.trace_add('write', my_callback)

        input_new_name = Entry(edit_frame, width=20, textvariable=new_name)
        input_new_name.grid(column=2, row=2, columnspan=2, sticky=W, pady=(10, 0))

        add_frequency = Label(edit_frame, text="Select habit frequency:")
        add_frequency.grid(column=1, row=3, sticky=W, padx=(50, 0))

        frequency = IntVar()
        frequency.trace_add('write', my_callback)

        frequency_daily = Radiobutton(edit_frame, text='Daily', variable=frequency, value=1)
        frequency_daily.grid(column=2, row=3, sticky=W)

        frequency_weekly = Radiobutton(edit_frame, text='Weekly', variable=frequency, value=2)
        frequency_weekly.grid(column=3, row=3, sticky=W)

        change = Button(edit_frame, text='Change', command=change_clicked)
        change.grid(column=3, row=4, pady=(10, 0))

        reset = Button(edit_frame, text='Reset', command=reset_clicked)
        reset.grid(column=2, row=4, pady=(10, 0))

        return_button = Button(edit_frame, text='Return', command=return_clicked)
        return_button.grid(column=1, row=4, pady=(10, 0))

        dup = Label(edit_frame, text="This habit already exists")
        unchanged = Label(edit_frame, text="The inputs match the existing habit")

        my_callback()

    def delete_button(self):
        def selected(habit_button):
            confirm = tkinter.messagebox.askokcancel('Confirm',
                                                     f'Habit {habit_list[habit_button].name} '
                                                     f'will be deleted, THIS CANNOT BE UNDONE')
            if confirm:
                del habit_list[habit_button]
                store_data(habit_list)
                delete_buttons.destroy()
                valid = file_verification()
                if valid:
                    self.delete_button()
                    self.reset_stat_frame()
                    self.main_stat_active()
                else:
                    self.recreate()

        def return_clicked():
            self.habit_button()
            delete_buttons.destroy()

        delete_buttons = Frame(self.menu_frame)
        delete_buttons.grid(row=1, column=2, padx=(30, 0))

        labels = Frame(delete_buttons)
        labels.grid(column=1, row=1)

        remove_label = Label(labels, text="Select a habit to remove", width=20)
        remove_label.grid(column=1, row=1)

        habit_list = data_retrieval()
        list_of = []
        key = 0

        scroll_option = Canvas(delete_buttons, width=130, height=140)
        scroll_option.grid(column=1, row=2, sticky=W)

        buttons = Frame(scroll_option)

        scroller = Scrollbar(delete_buttons, command=scroll_option.yview)
        scroller.grid(column=1, row=2, sticky=N + S + E)

        for habit in habit_list:
            list_of.append(Button(buttons,
                                  text=f'{habit.name}',
                                  command=lambda habit_button=key: selected(habit_button),
                                  bd=1,
                                  relief='ridge',
                                  padx=35))
            list_of[key].grid(column=1, row=key + 1, pady=(0, 10), sticky=W + E)
            key += 1

        scroll_option.create_window(0, 0, window=buttons, anchor='n')
        scroll_option.update()
        scroll_option.configure(yscrollcommand=scroller.set, scrollregion=scroll_option.bbox("all"))

        commands = Frame(delete_buttons)
        commands.grid(column=1, row=3)

        return_button = Button(commands, text='Return', command=return_clicked)
        return_button.grid(column=1, row=1, pady=(10, 0))

    def stat_button(self):
        def to_frequency():
            self.reset_stat_frame()
            self.frequency_button()

        def to_performance():
            self.reset_stat_frame()
            self.performance()

        def return_clicked():
            stat_buttons.destroy()
            self.main_button_active()

        stat_buttons = Frame(self.menu_frame)
        stat_buttons.grid(row=1, column=1, padx=(30, 0))

        stat_label = Label(stat_buttons, text="What do you wish to do:")
        stat_label.grid(column=1, row=1, sticky=W + E, pady=(0, 10))

        list_button = Button(stat_buttons,
                             text='Detailed Habit Stats',
                             command=self.stat_selection,
                             bd=1,
                             relief='ridge',
                             pady=4)
        list_button.grid(column=1, row=2, sticky=W + E, pady=10)

        performance_button = Button(stat_buttons,
                                    text='View Best And Worst',
                                    command=to_performance,
                                    bd=1,
                                    relief='ridge',
                                    pady=4)
        performance_button.grid(column=1, row=3, sticky=W + E, pady=(0, 10))

        frequency_button = Button(stat_buttons,
                                  text='Habit Frequency',
                                  command=to_frequency,
                                  bd=1,
                                  relief='ridge',
                                  pady=4)
        frequency_button.grid(column=1, row=4, sticky=W + E)

        return_button = Button(stat_buttons, text='Return', command=return_clicked)
        return_button.grid(column=1, row=5, pady=(10, 0))

    def stat_selection(self):
        def selected(habit_button):
            habit_id = habit_button
            self.reset_stat_frame()
            self.stat_details(habit_id)

        def return_clicked():
            stat_select.destroy()

        stat_select = Frame(self.menu_frame)
        stat_select.grid(row=1, column=1, padx=(30, 0))

        labels = Frame(stat_select)
        labels.grid(column=1, row=1)

        stat_label = Label(labels, text="Select a habit to view stats", width=20)
        stat_label.grid(column=1, row=1)

        habit_list = data_retrieval()
        list_of = []
        key = 0

        scroll_option = Canvas(stat_select, width=130, height=140)
        scroll_option.grid(column=1, row=2, sticky=W)

        buttons = Frame(scroll_option)

        scroller = Scrollbar(stat_select, command=scroll_option.yview)
        scroller.grid(column=1, row=2, sticky=N + S + E)

        for habit in habit_list:
            list_of.append(Button(buttons,
                                  text=f'{habit.name}',
                                  command=lambda habit_button=key: selected(habit_button),
                                  bd=1,
                                  relief='ridge',
                                  padx=35))
            list_of[key].grid(column=1, row=key + 1, pady=(0, 10), sticky=W + E)
            key += 1

        scroll_option.create_window(0, 0, window=buttons, anchor='n')
        scroll_option.update()
        scroll_option.configure(yscrollcommand=scroller.set, scrollregion=scroll_option.bbox("all"))

        commands = Frame(stat_select)
        commands.grid(column=1, row=3)

        return_button = Button(commands, text='Return', command=return_clicked)
        return_button.grid(column=1, row=1, pady=(10, 0))

    def stat_details(self, habit_id):
        def return_clicked():
            stat_detail.destroy()
            return_fix.destroy()
            self.reset_stat_frame()
            self.main_stat_active()

        stat_detail = Frame(self.stat_frame)
        stat_detail.config(height=195, width=185)
        stat_detail.grid_propagate(False)
        stat_detail.grid(column=1, row=1)

        habit_list = data_retrieval()
        if habit_list[habit_id].complete == 'no':
            name = habit_list[habit_id].name
            frequency = habit_list[habit_id].frequency
        else:
            name = habit_list[habit_id].name
            frequency = habit_list[habit_id].frequency
            current_streak = habit_list[habit_id].streak
            longest_streak = habit_list[habit_id].longest_streak
            add_date = habit_list[habit_id].first_log
            age = dt.datetime.now() - dt.datetime.strptime(habit_list[habit_id].first_log, '%Y-%m-%d %H:%M')
            since_log = dt.datetime.now() - dt.datetime.strptime(habit_list[habit_id].last_log, '%Y-%m-%d %H:%M')

            current_streak_label = Label(stat_detail, text='Current streak:')
            current_streak_label.grid(column=1, row=3)

            current_streak_info = Label(stat_detail, text=current_streak, font='Helvetica 10 bold')
            current_streak_info.grid(column=2, row=3)

            longest_streak_label = Label(stat_detail, text='Longest streak:')
            longest_streak_label.grid(column=1, row=4)

            longest_streak_info = Label(stat_detail, text=longest_streak, font='Helvetica 10 bold')
            longest_streak_info.grid(column=2, row=4)

            add_date_label = Label(stat_detail, text='Date added:')
            add_date_label.grid(column=1, row=5)

            add_date_info = Label(stat_detail, text=add_date[:-5], font='Helvetica 10 bold')
            add_date_info.grid(column=2, row=5)

            age_label = Label(stat_detail, text='Habit age:')
            age_label.grid(column=1, row=6)

            age_info = Label(stat_detail, text=f'{str(age.days)} days', font='Helvetica 10 bold')
            age_info.grid(column=2, row=6)

            last_log_label = Label(stat_detail, text='Time since last log:')
            last_log_label.grid(column=1, row=7)

            last_log_info = Label(stat_detail, text=f'{str(since_log.days)} days', font='Helvetica 10 bold')
            last_log_info.grid(column=2, row=7)

        name_label = Label(stat_detail, text='Habit name:')
        name_label.grid(column=1, row=1)

        name_info = Label(stat_detail, text=name, font='Helvetica 10 bold')
        name_info.grid(column=2, row=1)

        frequency_label = Label(stat_detail, text='Frequency:')
        frequency_label.grid(column=1, row=2)

        frequency_info = Label(stat_detail, text=frequency, font='Helvetica 10 bold')
        frequency_info.grid(column=2, row=2)

        return_fix = Frame(self.stat_frame)
        return_fix.grid(column=1, row=2)

        return_button = Button(return_fix, text='Return', command=return_clicked)
        return_button.grid(column=1, row=8)

    def performance(self):
        def return_clicked():
            performance_button.destroy()
            return_fix.destroy()
            self.reset_stat_frame()
            self.main_stat_active()

        performance_button = Frame(self.stat_frame)
        performance_button.config(height=195, width=185)
        performance_button.grid_propagate(False)
        performance_button.grid(column=1, row=1)

        habit_list = data_retrieval()
        logs = 0
        name = 'No habits meet criteria'

        for habit in habit_list:
            if habit.complete == 'yes':
                last_log = dt.datetime.strptime(habit.last_log, '%Y-%m-%d %H:%M')
                first_index = habit.all_logs.index(habit.streak_start)
                last_index = habit.all_logs.index(habit.last_log)
                if habit.frequency == 'daily':
                    if logs < last_index-first_index and \
                            dt.datetime.now()-last_log < dt.timedelta(days=habit.streak + 1):
                        logs = last_index-first_index
                        name = habit.name
                else:
                    if logs < last_index-first_index and \
                            dt.datetime.now()-last_log < dt.timedelta(days=8):
                        logs = (last_index-first_index)/7
                        name = habit.name

        best_label = Label(performance_button, text='Best habit')
        best_label.grid(column=1, columnspan=2, row=1)

        name_label = Label(performance_button, text='Habit name:')
        name_label.grid(column=1, row=2)

        name_info = Label(performance_button, text=name, font='Helvetica 10 bold')
        name_info.grid(column=2, row=2)

        log_label = Label(performance_button, text='Logged:')
        log_label.grid(column=1, row=3)

        log_info = Label(performance_button, text=f'{logs} times', font='Helvetica 10 bold')
        log_info.grid(column=2, row=3)

        day_label = Label(performance_button, text='In:')
        day_label.grid(column=1, row=4)

        day_info = Label(performance_button, text=f'{logs} weeks', font='Helvetica 10 bold')
        day_info.grid(column=2, row=4)

        logs = 1e10
        name = 'No habits meet criteria'

        for habit in habit_list:
            if habit.complete == 'yes':
                last_log = dt.datetime.strptime(habit.last_log, '%Y-%m-%d %H:%M')
                first_index = habit.all_logs.index(habit.streak_start)
                last_index = habit.all_logs.index(habit.last_log)
                if habit.frequency == 'daily':
                    if logs > last_index - first_index and \
                            dt.datetime.now() - last_log < dt.timedelta(days=habit.streak + 1):
                        logs = last_index - first_index
                        name = habit.name
                else:
                    if logs > last_index - first_index and \
                            dt.datetime.now() - last_log < dt.timedelta(days=8):
                        logs = last_index - first_index
                        name = habit.name

        worst_label = Label(performance_button, text='Worst habit')
        worst_label.grid(column=1, columnspan=2, row=5)

        name_label = Label(performance_button, text='Habit name:')
        name_label.grid(column=1, row=6)

        name_info = Label(performance_button, text=name, font='Helvetica 10 bold')
        name_info.grid(column=2, row=6)

        log_label = Label(performance_button, text='Logged:')
        log_label.grid(column=1, row=7)

        log_info = Label(performance_button, text=f'{logs} times', font='Helvetica 10 bold')
        log_info.grid(column=2, row=7)

        day_label = Label(performance_button, text='In:')
        day_label.grid(column=1, row=8)

        day_info = Label(performance_button, text=f'{logs} days', font='Helvetica 10 bold')
        day_info.grid(column=2, row=8)

        return_fix = Frame(self.stat_frame)
        return_fix.grid(column=1, row=2)

        return_button = Button(return_fix, text='Return', command=return_clicked)
        return_button.grid(column=1, row=8)

    def frequency_button(self):
        def return_clicked():
            frequency_list.destroy()
            self.reset_stat_frame()
            self.main_stat_active()

        frequency_list = Frame(self.stat_frame)
        frequency_list.config(height=227, width=185)
        frequency_list.grid_propagate(False)
        frequency_list.grid(row=1, column=1)

        frequency_label = Label(frequency_list, text='Habit Frequency:')
        frequency_label.grid(row=1, column=1, columnspan=2)

        daily_label = Label(frequency_list, text='Daily Habits')
        daily_label.grid(row=2, column=1, sticky=W)

        weekly_label = Label(frequency_list, text='Weekly Habits')
        weekly_label.grid(row=2, column=2, sticky=W)

        daily_habits = Listbox(frequency_list, font='Helvetica 10', height=7, width=11)
        daily_habits.grid(row=3, column=1, sticky=W)

        weekly_habits = Listbox(frequency_list, font='Helvetica 10', height=7, width=11)
        weekly_habits.grid(row=3, column=2, sticky=W)

        habit_list = data_retrieval()

        for habit in habit_list:
            if habit.frequency == 'weekly':
                weekly_habits.insert('end', habit.name)
            elif habit.frequency == 'daily':
                daily_habits.insert('end', habit.name)

        return_button = Button(frequency_list, text='Return', command=return_clicked)
        return_button.grid(row=4, column=1, columnspan=2)

    def add_frame(self):

        def my_callback(*args):
            habit_name = name.get()
            habit_frequency = frequency.get()
            habit_completion = completion.get()
            if habit_name != '' and 1 <= habit_frequency <= 2 and 1 <= habit_completion <= 2:
                add.config(state='active')
            else:
                add.config(state='disabled')
            for habit in data_retrieval():
                if habit.name == habit_name:
                    add.config(state='disabled')
                    dup.grid(column=2, row=7, columnspan=4, sticky=W + N, pady=(0, 10), padx=(50, 0))
                    break
                if habit.name != habit_name and dup.grid_info() != {}:
                    dup.grid_forget()

        def add_clicked():
            habit_name = name.get()
            habit_frequency = frequency.get()
            habit_completion = completion.get()
            add_habit(name=habit_name, frequency=habit_frequency, completion=habit_completion)
            add_frame.destroy()
            self.add_frame()
            tkinter.messagebox.showinfo('Habit Added', f'{habit_name} added to tracker')
            self.recreate()

        add_frame = Frame(self.input_frame)
        add_frame.config(height=227, width=370)
        add_frame.grid_propagate(False)
        add_frame.grid(column=1, row=1)

        menu_label = Label(add_frame, text="Add")
        menu_label.grid(column=2, row=1, columnspan=4, pady=(0, 10))

        add_name = Label(add_frame, text="Input habit name:")
        add_name.grid(column=2, row=2, sticky=W, pady=(10, 0), padx=(50, 0))

        name = StringVar()
        name.trace_add('write', my_callback)

        input_name = Entry(add_frame, width=20, textvariable=name)
        input_name.grid(column=3, row=2, columnspan=2, sticky=W, pady=(10, 0))

        add_frequency = Label(add_frame, text="Select habit frequency:")
        add_frequency.grid(column=2, row=3, sticky=W, padx=(50, 0))

        frequency = IntVar()
        frequency.trace_add('write', my_callback)

        frequency_daily = Radiobutton(add_frame, text='Daily', variable=frequency, value=1)
        frequency_daily.grid(column=3, row=3, sticky=W)

        frequency_weekly = Radiobutton(add_frame, text='Weekly', variable=frequency, value=2)
        frequency_weekly.grid(column=4, row=3, sticky=W)

        add_complete = Label(add_frame, text="Status at time of adding:")
        add_complete.grid(column=2, row=4, sticky=W+S, padx=(50, 0))

        add_complete = Label(add_frame, text="Complete:")
        add_complete.grid(column=2, row=5, sticky=W+N, pady=(0, 10), padx=(50, 0))

        completion = IntVar()
        completion.trace_add('write', my_callback)

        complete_yes = Radiobutton(add_frame, text='Yes', variable=completion, value=1)
        complete_yes.grid(column=3, row=5, sticky=W+N, pady=(0, 10))

        complete_no = Radiobutton(add_frame, text='No', variable=completion, value=2)
        complete_no.grid(column=4, row=5, sticky=W+N, pady=(0, 10))

        add = Button(add_frame, text='Add', command=add_clicked)
        add.grid(column=3, row=6, columnspan=2, pady=(10, 0))

        dup = Label(add_frame, text="This habit already exists")

        my_callback()
