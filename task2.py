# Initialize variables
total_runners = 0
total_time = 0
fastest_time = float("inf")
slowest_time = 0
fastest_runner = 0

print("Park Run Timer")
print("~~~~~~~~~~~~~~~")
print()
print("Let's go!\n")
# Read input until "END" is reached
while True:
    line = input(">")
    if line == "END":
        break

    # Split the input line into runner number and time
    parts = line.split("::")
    if len(parts) != 2:
        print("Error in data stream. Ignoring. Carry on.")
        continue

    # Extract runner number and time
    try:
        runner_number = int(parts[0])
        time = int(parts[1])
    except ValueError:
        print("Error in data stream. Ignoring. Carry on.")
        continue

    # Update statistics
    total_runners += 1
    total_time += time
    if time < fastest_time:
        fastest_time = time
        fastest_runner = runner_number
    if time > slowest_time:
        slowest_time = time

# Calculate average time
try:
    average_time = total_time / total_runners

    # Convert times to minutes and seconds
    fastest_time_minutes = fastest_time // 60
    fastest_time_seconds = fastest_time % 60
    slowest_time_minutes = slowest_time // 60
    slowest_time_seconds = slowest_time % 60
    average_time_minutes = average_time // 60
    average_time_seconds = average_time % 60

    print()
    
    print("Total Runners:", total_runners)
    
    print("Average Time: ", int(average_time_minutes), "minutes," if int(average_time_minutes) > 1 else "minute,", int(average_time_seconds), "seconds")
    print("Fastest Time: ", fastest_time_minutes, "minutes," if fastest_time_minutes > 1 else "minute,", fastest_time_seconds, "seconds")
    print("Slowest Time: ", slowest_time_minutes, "minutes," if slowest_time_minutes > 1 else "minute", slowest_time_seconds, "seconds")
    print()
    print("Best Time Here: Runner #", fastest_runner)
    
except ZeroDivisionError:
    print("No data found. Nothing to do. What a pity.")
