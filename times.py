import read
import pandas as pd
import datetime
from dateutil.parser import parse
data = read.load_data()

def hour_extract(series):
    datetimeobj = parse(series)
    hour = datetimeobj.hour
    
    return hour



data['hour'] = data['submission_time'].apply(hour_extract)


hours = data['hour'].value_counts(sort = True, ascending = False)
#hours = hours[0:24:] #shows 24 hours
for name, value in hours.items():
    print("{0}: {1}".format(name, value))

    

    
import read
import pandas as pd
import datetime
from dateutil.parser import parse
data = read.load_data()

def hour_extract(series):
    datetimeobj = parse(series)
    hour = datetimeobj.hour
    
    return hour
    
data['hour'] = data['submission_time'].apply(hour_extract)
hours = data['hour'].value_counts(sort = True, ascending = False)

#hours = hours[0:24:] #shows 24 hours
for name, value in hours.items():
    print("{0}: {1}".format(name, value))


def day_extract(series):
    datetimeobj = parse(series)
    day = datetimeobj.day
    
    return day
    
data['day'] = data['submission_time'].apply(day_extract)
day = data['day'].value_counts(sort = True, ascending = False)

#days = days[0:24:] #shows 31 days
for name, value in day.items():
    print("{0}: {1}".format(name, value)) 

def month_extract(series):
    datetimeobj = parse(series)
    month = datetimeobj.month 
    
    return month

data['month'] = data['submission_time'].apply(month_extract)
month = data['month'].value_counts(sort = True, ascending = False)

#months = month[0:24:] #shows 12 months    
for name, value in month.items():
    print("{0}: {1}".format(name, value))
        
       
