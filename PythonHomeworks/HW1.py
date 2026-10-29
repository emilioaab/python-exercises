
def finishTime(startTime, flightTime):
    """
    Calculates the final time after adding flightTime to the given startTime, handling overflow.

    Parameters:
        startTime (tuple): A tuple containing hours, minutes, and seconds for the start time.
        flightTime (int): Flight time in seconds to add to the start time.

    Returns:
        str: Formatted string of the final time and day offset if applicable.
    """
    hours, minutes, seconds = startTime
    extra_seconds = flightTime

    # Input validation
    if not (0 <= hours < 24) or not (0 <= minutes < 60) or not (0 <= seconds < 60):
        errors = []
        if not (0 <= hours < 24):
            errors.append(f"{hours} hours value error !!!")
        if not (0 <= minutes < 60):
            errors.append(f"{minutes} minutes value error !!!")
        if not (0 <= seconds < 60):
            errors.append(f"{seconds} seconds value error !!!")
        return '\n'.join(errors)

    # Convert time to seconds and add extra seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds + extra_seconds

    # Calculate final time components
    days_added = total_seconds // (24 * 3600)
    final_seconds = total_seconds % 60
    final_minutes = (total_seconds // 60) % 60
    final_hours = (total_seconds // 3600) % 24

    # Format the final time
    formatted_time = f"{final_hours:02}:{final_minutes:02}:{final_seconds:02}({days_added})"
    day_suffix = f" (+{days_added} day{'s' if days_added > 1 else ''})" if days_added else ""
    return f"the finish time[{formatted_time}]: {final_hours} hour{'s' if final_hours != 1 else ''}, {final_minutes} minute{'s' if final_minutes != 1 else ''}, {final_seconds} second{'s' if final_seconds != 1 else ''}{day_suffix}"

# Adjusting the function to accept startTime as a tuple and flightTime in seconds according to the updated requirement.
# Adjusting the example calls to match the updated function signature
test_cases = [
    ((2, 3, 5), 0),
    ((23, 5, 10), 0),
    ((0, 0, 0), 83110),
    ((0, 0, 0), 3667),
    ((0, 0, 0), 82800),
    ((0, 0, 0), 82810),
    ((0, 0, 0), 91215),
    ((0, 0, 0), 177615),
    ((100, 200, 300), 0)  # This case is expected to show validation errors
]
print("Q#1")
for case in test_cases:
    startTime, flightTime = case
    # Manually format the string to achieve the desired format
    print(f"finishTime({startTime[0]},{startTime[1]},{startTime[2]},{flightTime})\n{finishTime(startTime, flightTime)}")




def digits(number):
    """
    Adjusted function to print the number of digits in a given number and its parity (even or odd),
    with the digit count spelled out.
    """
    # Mapping of numbers to words for the count of digits
    number_to_word = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
                      6: "six", 7: "seven", 8: "eight", 9: "nine"}

    digit_count = len(str(abs(number)))  # Count the number of digits.
    digit_count_word = number_to_word.get(digit_count, str(digit_count))  # Convert digit count to word.

    # Adjust parity checking to match the corrected output logic if needed.
    parity = "even" if digit_count % 2 == 0 else "odd"  # This should be adjusted based on the actual requirement.

    # Print the result with digit count as word and parity.
    print(f"digits({number})\n{digit_count_word} digit{'s' if digit_count > 1 else ''} - {parity}")


print('\nQ#2')
digits(6)
digits(63)
digits(163)
digits(1653)
digits(16453)


def correctNumber(number):
    """

    :param number:
    :return:
    """




