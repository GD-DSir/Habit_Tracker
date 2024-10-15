import unittest
from scripts.data_handling import *

class TestMethods(unittest.TestCase):
    # Test if add button is disabled, when all field aren't filled or name already exists.
    def test_add_state(self):

        def state_checker(name, frequency, completion):
            habit_name = name.lower().title()
            habit_frequency = frequency
            habit_completion = completion
            if habit_name != '' and 1 <= habit_frequency <= 2 and 1 <= habit_completion <= 2:
                state='active'
            else:
                state='disabled'

            for habit in habit_list:
                if habit.name == habit_name:
                    state='disabled'
                    return state

            return state


        habit_list = data_retrieval()

        check_list = [state_checker(habit_list[0].name,1,1),
                      state_checker('Random habit', 0, 1),
                      state_checker(habit_list[0].name, 0, 1),
                      state_checker(habit_list[0].name, 1, 0),
                      state_checker('Random habit', 1, 0),
                      state_checker('Random habit', 0, 0),
                      state_checker('', 1, 1)
                      ]
        for valid in check_list:
            self.assertEqual(valid, 'disabled')

        self.assertEqual(state_checker('Random habit', 1, 1), 'active')

    # Test if change button is disabled, when all field aren't filled or data matches existing data.
    def test_change_state(self):
        def state_checker(new_name, frequency):
            habit_name = new_name.lower().title()
            habit_frequency = frequency
            if habit_frequency == 'daily':
                frequency_int = 1
            elif habit_frequency == 'weekly':
                frequency_int = 2
            else:
                frequency_int = 0
            if habit_name != '' and 1 <= frequency_int <= 2:
                state='active'
            else:
                state='disabled'
            for habit in habit_list:
                if habit.name == habit_name and habit_name != habit_list[0].name:
                    state='disabled'
                    return state
                if habit_list[0].frequency == habit_frequency and habit_name == habit_list[0].name:
                    state='disabled'
                    return state
            return state

        habit_list = data_retrieval()

        check_list = [state_checker(habit_list[0].name, habit_list[0].frequency),
                      state_checker('Random habit', ''),
                      state_checker(habit_list[1].name, 'weekly'),
                      state_checker(habit_list[1].name, 'daily'),
                      state_checker('', 'daily')
                      ]

        for valid in check_list:
            self.assertEqual(valid, 'disabled')

        if habit_list[0].frequency == 'daily':
            frequency = 'weekly'
        else:
            frequency = 'daily'

        self.assertEqual(state_checker('Random habit', 'daily'), 'active')
        self.assertEqual(state_checker(habit_list[0].name, frequency), 'active')

if __name__ == '__main__':
    unittest.main()