s = '01:15:30PM'


def timeConversion(s):
    # Write your code here
    hour = s[0:2]
    minute = s[3:5]
    second = s[6:8]
    AM_or_PM = s[-2:]
    
    res = ''
    if AM_or_PM == 'PM' and hour != '12':
        hour = int(hour)
        hour += 12
        hour = str(hour)
    elif AM_or_PM == 'AM' and hour == '12':
        hour = '00'
    
    res = hour + ':' + minute + ':' + second
    return res


print(timeConversion('12:05:50AM'))

print(timeConversion('12:05:50PM'))

print(timeConversion('06:05:50AM'))