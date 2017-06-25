#
# This is a first attempt to add all my log book hours
# Using a program to input my numbers instead of cubersome calculators
# It is able to convert the times to hours as well
# So we can know how close to our goal we are
# Future functionality will allow us to import and export csvs
#	to record progress
# @author Karan Goda
# version 1.0.0

#! /usr/bin/env python3

import datetime
import csv

#log_book = open('log_book.csv', 'w')

class log_book_tracker:
    # 100 hours converted to minutes
    day_time_needed = 100 * 60
    # 20 hours converted to minutes
    night_time_needed = 20 * 60

    def __init__(self, day_time, night_time):
        self._day_time = int(day_time)
        self._night_time = int(night_time)
        self._day_time_in_hours = 0
        self._night_time_in_hours = 0

    # Counts minutes for type of time
    def calc_tot_night(self):
        print('I can add up your total night driving time page by page')
        usr_input = input('Times in minutes: ')

        while usr_input != '':
            try:
                log_book_page = usr_input.split()
                temp_total = 0
                for i in log_book_page:
                    temp_total += int(i)
                    self._night_time += int(i)
                #print('Press enter to quit.')
                print(temp_total)
                usr_input = input('Time in minutes: ')

            except ValueError as e:
                print('Press enter to quit.')
                usr_input = input('Time in minutes: ')

    def calc_tot_day(self):
        print('I can add up your total day driving time page by page')
        usr_input = input('Time in minutes: ')

        while usr_input != '':
            try:
                log_book_page = usr_input.split()
                #for line in log_book_page:
                #    print(line, file = log_book)
                temp_total = 0

                for i in log_book_page:
                    temp_total += int(i)
                # The _ will make sure that
                # the value does not get destroyed after the first loop
                    self._day_time += int(i)
                #print('Press enter to quit.')
                print(temp_total)
                usr_input = input('Time in minutes: ')

            except ValueError as e:
                # if e != 'Stop':
                #     print('Sorry you need to enter a valid number.')
                # else:
                #     break

                print('Press enter to quit.')
                usr_input = input('Time in minutes: ')

    def convert_minutes_to_hours(self):
        self._day_time_in_hours = datetime.timedelta(minutes=self._day_time)
        self._night_time_in_hours = datetime.timedelta(minutes=self._night_time)

karan_logBook = log_book_tracker(0, 0)
print('This is a log book tracker. \nIt will count the total hours you did for day and night separately.\n')
action = input('Enter \'Day\' to input total time for day.\nEnter \'Night\' to input total time for night. \nEnter \'Convert to hours\' to convert logbook to hours at the end. \nEnter \'Get day\' to get total input time for day. \nEnter \'Get Night\' to get total input time for night. \nEnter \'Help\' to get console commands to use this logbooker \nEnter \'Quit\' to exit the program.\n\n')
while action.lower() != 'Quit'.lower():
    if action.lower() == 'Help'.lower():
        print('Enter \'Day\' to input total time for day.\nEnter \'Night\' to input total time for night. \nEnter \'Convert to hours\' to convert logbook to hours at the end. \nEnter \'Get day\' to get total input time for day. \nEnter \'Get Night\' to get total input time for night. \nEnter \'Help\' to get console commands to use this logbooker \nEnter \'Quit\' to exit the program.\n')
        action = input('What do you want to do? ')
    elif action.lower() == 'Night'.lower():
        karan_logBook.calc_tot_night()
        action = input('What do you want to do? ')
    elif action.lower() == 'Day'.lower():
        karan_logBook.calc_tot_day()
        action = input('What do you want to do? ')
    elif action.lower() == 'Convert to hours'.lower():
        karan_logBook.convert_minutes_to_hours()
        action = input('What do you want to do? ')
    elif action.lower() == 'Get Day'.lower():
        if karan_logBook._day_time_in_hours == 0:
            print('Total minutes: ' + str(karan_logBook._day_time))
        else:
            print('Total hours: ' + str(karan_logBook._day_time_in_hours))
        action = input('What do you want to do? ')
    elif action.lower() == 'Get Night'.lower():
        if karan_logBook._night_time_in_hours == 0:
            print('Total minutes: ' + str(karan_logBook._night_time))
        else:
            print('Total hours: ' + str(karan_logBook._night_time_in_hours))
        action = input('What do you want to do? ')
    else:
        action = input('What do you want to do? ')

#log_book.close()
