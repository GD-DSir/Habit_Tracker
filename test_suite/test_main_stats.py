import unittest
import datetime as dt
from scripts.data_handling import *

class TestMethods(unittest.TestCase):

    # Test main menu statistic validity.
    def test_longest_steak(self):
        habit_list = data_retrieval()
        longest_streak = 0
        index = 0

        for habit in habit_list:
            if habit.complete == 'yes':
                if habit.longest_streak > longest_streak:
                    longest_streak = habit.longest_streak
                    index = habit_list.index(habit)

        for habit in habit_list:
            if habit.complete == 'yes':
                self.assertGreaterEqual(habit_list[index].longest_streak, habit.longest_streak)


    def test_current_steak(self):
        habit_list = data_retrieval()
        current_streak = 0
        index = 0

        for habit in habit_list:
            if habit.complete == 'yes':
                if habit.streak > current_streak:
                    current_streak = habit.streak
                    index = habit_list.index(habit)

        for habit in habit_list:
            if habit.complete == 'yes':
                self.assertGreaterEqual(habit_list[index].streak, habit.streak)

    def test_oldest(self):
        habit_list = data_retrieval()
        oldest = dt.timedelta(days=0)
        index = 0

        for habit in habit_list:
            if habit.complete == 'yes':
                delta = dt.datetime.now() - dt.datetime.strptime(habit.first_log, '%Y-%m-%d %H:%M')
                if delta > oldest:
                    oldest = delta
                    index = habit_list.index(habit)

        for habit in habit_list:
            if habit.complete == 'yes':
                delta_index = (dt.datetime.now() -
                               dt.datetime.strptime(habit_list[index].first_log, '%Y-%m-%d %H:%M'))
                delta = dt.datetime.now() - dt.datetime.strptime(habit.first_log, '%Y-%m-%d %H:%M')
                self.assertGreaterEqual(delta_index, delta)

if __name__ == '__main__':
    unittest.main()