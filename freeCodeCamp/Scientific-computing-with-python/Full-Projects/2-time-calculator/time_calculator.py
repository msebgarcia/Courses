def add_time(current_time, adding_time, day = 'None'):
	adding_hours,adding_minutes = adding_time.split(':')
	current_daytime = current_time.split()[1]
	current_hour,current_minutes = current_time.split()[0].split(':')

	result_time = [int(current_hour)+int(adding_hours),int(current_minutes)+int(adding_minutes)]

	print(result_time)

	if result_time[1] >= 60:
		result_time[0] += result_time[1]//60
		result_time[1] %= 60

	n_days_later = result_time[0]//24

	result_time[0] -= n_days_later*24

	if result_time[0] > 12:
		result_time[0] -= 12
		result_daytime = ' AM' if (current_daytime == 'PM') else ' PM'
	elif result_time[0] == 12:
		result_daytime = ' AM' if (current_daytime == 'PM') else ' PM'
	else:
		result_daytime = ' '+current_daytime

	n_days_later += 1 if result_daytime==' AM' and current_daytime == 'PM' else 0

	result_time = str(result_time[0]) + ':' + '{:0>2}'.format(result_time[1]) + result_daytime

	if (day!='None'):
		week_days = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday',
		}
		current_day = list(week_days.values()).index(day.capitalize())
		result_time += ', ' + week_days.get((current_day + n_days_later)%7)

	if n_days_later == 1:
		result_time += ' (next day)'
	elif n_days_later > 1:
		result_time += f' ({n_days_later} days later)'
	else:
		pass

	return result_time