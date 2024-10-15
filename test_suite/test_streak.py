import unittest
import datetime as dt
from scripts.data_handling import *


class TestMethods(unittest.TestCase):
    # Test streak verification in habit.log()
    def test_streak_validity(self):
        habit_list = data_retrieval()

        for habit in habit_list:
            if habit.complete == 'yes':
                time_since = dt.datetime.now() - dt.datetime.strptime(habit.last_log, '%Y-%m-%d %H:%M')
                if time_since > dt.timedelta(hours=10) and habit.frequency == 'daily':
                    habit.last_log = dt.datetime.now().strftime('%Y-%m-%d %H:%M')
                    habit.all_logs.append(habit.last_log)

                    last_log = dt.datetime.strptime(habit.last_log, '%Y-%m-%d %H:%M')
                    streak_start = dt.datetime.strptime(habit.streak_start, '%Y-%m-%d %H:%M')

                    if last_log - streak_start <= dt.timedelta(days=habit.streak + 1):
                        last = dt.datetime.strptime(habit.all_logs[::-1][0], '%Y-%m-%d %H:%M')
                        previous = dt.datetime.strptime(habit.all_logs[::-1][1], '%Y-%m-%d %H:%M')
                        self.assertGreaterEqual(last - previous, dt.timedelta(hours=10))
                        self.assertLessEqual(last - streak_start, dt.timedelta(days=habit.streak+1))

                    else:
                        last = dt.datetime.strptime(habit.all_logs[::-1][0], '%Y-%m-%d %H:%M')
                        previous = dt.datetime.strptime(habit.all_logs[::-1][1], '%Y-%m-%d %H:%M')
                        self.assertGreaterEqual(last - previous, dt.timedelta(hours=10))
                        self.assertGreaterEqual(last - streak_start, dt.timedelta(days=habit.streak+1))


                elif time_since > dt.timedelta(days=6) and habit.frequency == 'weekly':
                    habit.last_log = dt.datetime.now().strftime('%Y-%m-%d %H:%M')
                    habit.all_logs.append(habit.last_log)

                    last_log = dt.datetime.strptime(habit.last_log, '%Y-%m-%d %H:%M')
                    streak_start = dt.datetime.strptime(habit.streak_start, '%Y-%m-%d %H:%M')

                    if last_log - streak_start <= dt.timedelta(days=habit.streak * 7, hours=12):
                        last = dt.datetime.strptime(habit.all_logs[::-1][0], '%Y-%m-%d %H:%M')
                        previous = dt.datetime.strptime(habit.all_logs[::-1][1], '%Y-%m-%d %H:%M')
                        self.assertGreaterEqual(last - previous, dt.timedelta(days=6))
                        self.assertLessEqual(last - streak_start, dt.timedelta(days=habit.streak*7, hours=12))

                    else:
                        last = dt.datetime.strptime(habit.all_logs[::-1][0], '%Y-%m-%d %H:%M')
                        previous = dt.datetime.strptime(habit.all_logs[::-1][1], '%Y-%m-%d %H:%M')
                        self.assertGreaterEqual(last - previous, dt.timedelta(days=6))
                        self.assertGreaterEqual(last - streak_start, dt.timedelta(days=habit.streak*7, hours=12))
                else:
                    last = dt.datetime.now()
                    previous = dt.datetime.strptime(habit.all_logs[::-1][0], '%Y-%m-%d %H:%M')
                    if habit.frequency == 'weekly':
                        self.assertLessEqual(last - previous, dt.timedelta(days=6))
                    else:
                        self.assertLessEqual(last - previous, dt.timedelta(hours=10))

if __name__ == '__main__':
    unittest.main()