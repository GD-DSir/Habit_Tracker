import json
import os
from scripts.habit import Habit


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

    with open('habits.json', 'w') as store:                         # Overwrite habit.json with empty file.
        json.dump(save_data, store)                                 # Dump the new data to habit.json.
    path = os.getcwd()                                              # Get the current working directory
    test_file = os.path.join(path, 'test_suite', 'habits.json')     # Enter the test_suite folder and create habits.json
    with open(test_file, 'w') as store:                             # Access habits.json in test_suite.
        json.dump(save_data, store)                                 # Dump the new data to habit.json in test_suite.

