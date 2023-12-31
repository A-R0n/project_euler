## Counting Sundays

## How many Sundays
## fell on the first of the month
## during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
STARTING_YEAR = 1901
ENDING_YEAR = 2000
X = 'Sunday'

import datetime
from collections import Counter
import calendar

def get_day_of_week(dateStr: str):
    return datetime.datetime.strptime(dateStr, '%B %d, %Y').strftime('%A')

def solve():
    days_of_week = []
    months = [calendar.month_name[i] for i in range(1,13)]
    days_of_week = [get_day_of_week(str(month + ' 1, ' + str(year))) for month in months for year in range(STARTING_YEAR, ENDING_YEAR+1)]
    return Counter(days_of_week)[X]

if __name__ == '__main__':
    num_sundays = solve()
    print(num_sundays)