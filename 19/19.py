## Counting Sundays

## How many Sundays
## fell on the first of the month
## during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
START_DATE = 'January 1, 1901'
END_DATE = 'December 31, 2000'

STARTING_YEAR = 1901
ENDING_YEAR = 2000
X = 'Sunday'

import datetime
from collections import Counter
import calendar

count = 0
days_of_week = []
## for some reason, the first month calendar gives us is an empty string
months = [calendar.month_name[i] for i in range(1,13)]

def get_day_of_week(dateStr: str):
    return datetime.datetime.strptime(dateStr, '%B %d, %Y').strftime('%A')

def solve():
    ## this gives us 170 for some reason... correct answer is 171
    # days_of_week = [get_day_of_week(str(month + ' 1, ' + str(year))) for month in months for year in range(STARTING_YEAR, ENDING_YEAR)]

    ## this gives us 171
    for year in range(STARTING_YEAR, ENDING_YEAR+1):
        for month in months:
            date_str = month + ' 1, ' + str(year)
            day_of_week = get_day_of_week(date_str)
            days_of_week.append(day_of_week)
    return Counter(days_of_week)[X]

if __name__ == '__main__':
    num_sundays = solve()
    print(num_sundays)