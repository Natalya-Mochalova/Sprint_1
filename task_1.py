time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0

for time_path in time_string.split(','):

    for time in time_path.split():
        if 'h' in time:
            hours = int(time.replace('h', ''))
            total_minutes += hours * 60
        elif 'm' in time:
            minutes = int(time.replace('m', ''))
            total_minutes += minutes
        elif 's' in time:
            seconds = int(time.replace('s', ''))
            total_minutes += seconds // 60

print(total_minutes)