import unittest
from scripts.data_handling import *
import datetime as dt
import math

class TestMethods(unittest.TestCase):
    # Test if Best and Worst habit calculations are valid.
    def test_habit_performance(self):
        habit_list = data_retrieval()

        daily_performance = 0
        weekly_performance = 0
        previous_daily = 0
        previous_weekly = 0


        for habit in habit_list:
            if habit.complete == 'yes':
                first_log = dt.datetime.strptime(habit.first_log, '%Y-%m-%d %H:%M')
                all_logs = len(habit.all_logs)
                if habit.frequency == 'daily':
                    delta = math.ceil((dt.datetime.now() - first_log).days)
                    if delta == 0:
                        delta = 1
                    daily_performance = all_logs/delta
                    if (daily_performance > weekly_performance and daily_performance > previous_daily and
                            previous_weekly < daily_performance):
                        previous_daily = daily_performance
                else:
                    delta = math.ceil((dt.datetime.now() - first_log).days/7)
                    if delta == 0:
                        delta = 1
                    weekly_performance = all_logs / delta
                    if (daily_performance < weekly_performance and weekly_performance > previous_weekly and
                            previous_daily < weekly_performance):
                        previous_weekly = weekly_performance

        if previous_weekly >= previous_daily:
            best_habit = previous_weekly
        else:
            best_habit = previous_daily

        for habit in habit_list:
            if habit.complete == 'yes':
                first_log = dt.datetime.strptime(habit.first_log, '%Y-%m-%d %H:%M')
                all_logs = len(habit.all_logs)
                if habit.frequency == 'daily':
                    delta = math.ceil((dt.datetime.now() - first_log).days)
                    if delta == 0:
                        delta = 1
                    daily_performance = all_logs/delta
                    self.assertGreaterEqual(best_habit, daily_performance)
                else:
                    delta = math.ceil((dt.datetime.now() - first_log).days/7)
                    if delta == 0:
                        delta = 1
                    weekly_performance = all_logs / delta
                    self.assertGreaterEqual(best_habit, weekly_performance)

        daily_performance = 1
        weekly_performance = 1
        previous_daily = 1
        previous_weekly = 1


        for habit in habit_list:
            if habit.complete == 'yes':
                first_log = dt.datetime.strptime(habit.first_log, '%Y-%m-%d %H:%M')
                all_logs = len(habit.all_logs)
                if habit.frequency == 'daily':
                    delta = math.ceil((dt.datetime.now() - first_log).days)
                    if delta == 0:
                        delta = 1
                    daily_performance = all_logs / delta  # Calculate the performance of the selected habit object.
                    if (daily_performance < weekly_performance and daily_performance < previous_daily and
                            previous_weekly > daily_performance):
                        previous_daily = daily_performance
                else:
                    delta = math.ceil(
                        (dt.datetime.now() - first_log).days / 7)
                    if delta == 0:
                        delta = 1
                    weekly_performance = all_logs / delta
                    if (daily_performance > weekly_performance and weekly_performance < previous_weekly and
                            previous_daily > weekly_performance):
                        previous_weekly = weekly_performance

        if previous_weekly >= previous_daily:
            worst_habit = previous_daily
        else:
            worst_habit = previous_weekly

        for habit in habit_list:
            if habit.complete == 'yes':
                first_log = dt.datetime.strptime(habit.first_log, '%Y-%m-%d %H:%M')
                all_logs = len(habit.all_logs)
                if habit.frequency == 'daily':
                    delta = math.ceil((dt.datetime.now() - first_log).days)
                    if delta == 0:
                        delta = 1
                    daily_performance = all_logs / delta
                    self.assertLessEqual(worst_habit, daily_performance)
                else:
                    delta = math.ceil((dt.datetime.now() - first_log).days / 7)
                    if delta == 0:
                        delta = 1
                    weekly_performance = all_logs / delta
                    self.assertLessEqual(worst_habit, weekly_performance)