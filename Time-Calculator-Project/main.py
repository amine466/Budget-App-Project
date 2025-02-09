def add_time(start, duration, day=None):
    # Extract start time and AM/PM state
    time, state = start.split()  # Splits into ['5:11', 'PM']
    hour, minutes = map(int, time.split(':'))  # Splits '5:11' into 5 and 11

    # Extract duration time
    duration_hour, duration_minutes = map(int, duration.split(':'))

    # Add minutes and handle overflow
    new_minutes = minutes + duration_minutes
    extra_hours = new_minutes // 60  # Carry over to hours if minutes exceed 60
    new_minutes = new_minutes % 60  # Keep minutes within 0-59

    # Add hours and overflow from minutes
    new_hour = hour + duration_hour + extra_hours
    total_hours = new_hour  # Keep track of total hours passed
    days_later = total_hours // 24  # Full days later
    periods = total_hours // 12  # How many AM/PM switches have occurred

    # Keep hour within 12-hour format
    new_hour = new_hour % 12
    if new_hour == 0:
        new_hour = 12  # Handle midnight case properly

    # Determine AM/PM state change
    if periods % 2 == 1:
        state = 'PM' if state == 'AM' else 'AM'

    # Adjust days_later based on AM/PM crossing
    if state == 'AM' and start.endswith('PM'):
        days_later += 1

    # Handle days later string
    day_str = ''
    if days_later == 1:
        day_str = ' (next day)'
    elif days_later > 1:
        day_str = f' ({days_later} days later)'

    # Handle day of the week if provided
    if day:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_day_index = days_of_week.index(day.capitalize())
        result_day_index = (start_day_index + days_later) % 7
        day_str = f", {days_of_week[result_day_index]}{day_str}"

    # Format final output
    new_time = f"{new_hour}:{str(new_minutes).zfill(2)} {state}{day_str}"
    return new_time
  
# Execute function
add_time('3:30 PM', '2:12', 'Monday')  # Expected: '5:42 PM, Monday'
