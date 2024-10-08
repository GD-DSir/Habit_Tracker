import json
import os
from scripts.habit import Habit
from datetime import *


def file_verification():
    """Function used to verify the data in habits.json
    return: bool"""
    if os.path.exists('habits.json') is False:          # Check if file exists
        state = False                                   # Set state as False, program runs for first time
        with open('habits.json', 'w') as create:        # Create file if it does not exist
            create.close()                              # Close the file
        return state                                    # Return file state bool
    else:
        with open('habits.json', 'r') as create:        # Read file if it exists
            content = create.read()                     # Store content to variable
        if len(content) == 0:                           # Check if file contains any data, If file is empty
            state = False                               # Set state as False, program runs for first time
            return state                                # Return file state bool
        else:
            with open('habits.json', 'r') as create:    # Read file if it exists
                data = json.load(create)                # Store content to variable
            if not data['habits']:                      # Check if file contained data, If criterion met
                state = False                           # Set state as False, program resets to initial run
                return state                            # Return file state bool
            else:                                       # Check if file contains data, If file contains data
                state = True                            # Set state as True, program has run before
                return state                            # Return file state bool


def data_retrieval():
    """Function used to retrieve the data in habits.json
        return: [object]"""
    if file_verification():                             # Check file state with function file_verification().
        with open('habits.json', 'r') as create:        # Read file if it exists.
            data = json.load(create)                    # Store content to variable.
        habit_list = []                                 # Create list to append objects.
        for habits in data['habits']:                   # Iterate entries in habits.json.
            habit_object = Habit()                      # Create an object of Class Habit.
            habit_object.to_object(habit_dict=habits)   # Use method Habit.to_object to create objects.
            habit_list.append(habit_object)             # Append the created object into the habit_list.
        return habit_list                               # Return list of objects.
    else:                                               # If state false, no data in file.
        return []                                       # Return an empty list.


def to_json(habit_list):
    """Create a dictionary form object data contained in a habit_list,
        called when using function store_data() for data conversion\n
        habit_list = [object]\n
        return json_data = [dict]"""

    json_data = []                                                  # Create empty list to append dictionaries.
    for habit_object in habit_list:                                 # Iterate entries in habit_list.
        if habit_object.complete == 'yes':                          # Determine object properties.
            habit_dict = {"name": habit_object.name,
                          "frequency": habit_object.frequency,
                          "complete": habit_object.complete,
                          "streak": habit_object.streak,
                          "streak_start": habit_object.streak_start,
                          "longest_streak": habit_object.longest_streak,
                          "first_log": habit_object.first_log,
                          "last_log": habit_object.last_log,
                          "all_logs": habit_object.all_logs
                          }                                         # Dictionary for a full/complete habit.
        else:
            habit_dict = {"name": habit_object.name,
                          "frequency": habit_object.frequency,
                          "complete": habit_object.complete,
                          }                                         # Dictionary for a partial/incomplete habit.
        json_data.append(habit_dict)                                # Append the created dictionaries to json_data list.

    return json_data                                                # Return the json_data list


def store_data(habit_list):
    """Store data from objects to a json file, calls function to_json() for data conversion\n
        habit_list = [object]"""
    data = to_json(habit_list)                              # Calls function to_json() for data conversion.
    save_data = {"habits": data}                            # Set format for habit.json, and add data.

    with open('habits.json', 'w') as store:                 # Overwrite habit.json with empty file.
        json.dump(save_data, store)                         # Dump the new data to habit.json.


def add_habit(name: str, frequency: int, completion: int):
    """Add a habit \n
            name:[str] = 'name_of_habit'\n
            frequency:[int] = 1 or 2:
            \t- frequency = 1: daily
            \t- frequency = 2: weekly \n
            completion:[int] = 1 or 2:
            \t- completion = 1: True
            \t- completion = 2: False"""

    if frequency == 1:                                          # Value recorded with tkinter radiobutton (1 or 2).
        frequency_string = 'daily'                              # If value is 1 then frequency is daily.
    else:
        frequency_string = 'weekly'                             # If value is 2 then frequency is weekly.

    if completion == 1:                                         # Value recorded with tkinter radiobutton (1 or 2).
        completion_string = 'yes'                               # If value is 1 then habit is completed.
        first_log = datetime.now().strftime('%Y-%m-%d %H:%M')   # Completed habits have more properties than incomplete
        last_log = first_log                                    # habits.
        all_logs = [first_log]                                  # As this is a new habit, logged for first time.
        streak_start = first_log                                # first_log = last_log = all_log = streak_start = now()
        streak = 1                                              # Streak is 1
        longest_streak = 1                                      # Longest streak is 1
        habit = {'name': name,
                 'frequency': frequency_string,
                 'complete': completion_string,
                 'streak': streak,
                 'streak_start': streak_start,
                 'longest_streak': longest_streak,
                 'first_log': first_log,
                 'last_log': last_log,
                 'all_logs': all_logs
                 }                                             # Habit properties compiled in a dictionary

    else:                                                      # An incomplete habit has no time and streak data.
        completion_string = 'no'                               # Completion is used to determine if a habit is complete.
        habit = {'name': name,                                 # This determines the properties that are assigned to the
                 'frequency': frequency_string,                # habit.
                 'complete': completion_string
                 }

    data = Habit()                                             # Create an object of Class Habit.
    data.to_object(habit)                                      # Create a habit using the properties in dictionaries.
    habit_list = data_retrieval()                              # Retrieve the existing list of objects.
    habit_list.append(data)                                    # Append new object to end of existing habit list.
    store_data(habit_list)                                     # Store the new habit_list to habits.json
