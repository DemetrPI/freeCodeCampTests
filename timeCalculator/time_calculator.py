def add_time(start, duration, weekDay=None):
    # List of week days
    weekDays = ["Sunday", "Monday", "Tuesday",
                "Wednesday", "Thursday", "Friday", "Saturday"]

    # Split the start time into components and parse them
    start_time, start_ampm = start.split()

    start_hour, start_minute = map(int, start_time.split(":"))


    # Split the duration into components and parse them
    duration_hour, duration_minute = map(int, duration.split(":"))


    duration_days = 0

    # Adjust start_hour if it's PM and not 12
    if start_ampm == "PM" and start_hour != 12:
        start_hour += 12

    # Add the duration to the start time
    start_hour += duration_hour
    start_minute += duration_minute

    # Handle minutes exceeding 60 by incrementing hours
    if start_minute >= 60:
        start_hour += start_minute // 60
        start_minute = start_minute % 60

    # Handle hours exceeding 24 to calculate additional days
    if start_hour >= 24:
        duration_days += start_hour // 24
        start_hour = start_hour % 24

    # Determine the AM/PM designation
    if start_hour >= 12 and start_hour != 24:
        total_ampm = "PM"
        start_hour -= 12
    else:
        total_ampm = "AM"

    # Handle the case when start_hour is 0
    if start_hour == 0:
        start_hour = 12

    # Calculate the total days label
    total_days = f" (next day)" if duration_days == 1 else (
        f" ({duration_days} days later)" if duration_days > 1 else "")


    # Format the minute to have leading zero if needed
    start_minute = f"0{start_minute}" if start_minute < 10 else start_minute

    # Construct the new_time string
    new_time = f"{start_hour}:{start_minute} {total_ampm}"


    # Add the new day if weekDay is provided
    if weekDay is not None:
        current_day_index = weekDays.index(weekDay.capitalize())
        future_day_index = (current_day_index + duration_days) % 7
        new_time += f", {weekDays[future_day_index]}"

    # Add the total_days label
    new_time += total_days


    return new_time
