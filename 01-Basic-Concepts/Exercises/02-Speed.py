import traceback

slow_speed = 30  # kph
high_speed = 75  # kph


def get_input(prompt):
    value = input(prompt)
    if value.upper() == 'Q':
        print("Exiting...")
        exit(0)  # We can also return None and handle there
    return value


def assert_greater_or_equal_than(input, reference):
    if input < reference:
        raise ValueError


while True:
    try:
        str_distance = get_input(
            "Insert the travel distance (in meters) or press 'Q' to exit: ")
        distance = float(str_distance)
        assert_greater_or_equal_than(distance, 0)

        str_duration = get_input(
            "Insert the travel time (in minutes) or press 'Q' to exit: ")
        duration = float(str_duration)
        assert_greater_or_equal_than(duration, 0)

    except ValueError as e:
        print("Input value must be greater than or equal than zero. Try again.")
    except Exception as e:
        print("Some fatal error happened. Here is the error and the traceback:")
        print(e)
        traceback.print_exc()
        exit(1)
    else:
        break

speed = (distance / 1000) / (duration / 60)

print(f"Train speed is: {speed:.2f} kph")

if speed > high_speed:
    print(
        f"The train is above the upper speed limit ({high_speed} kph)!")
elif speed < slow_speed:
    print(
        f"The train is below the lower speed limit ({slow_speed} kph)!")
else:
    print(
        f"The train is running at the legal speed (between {slow_speed} and {high_speed} kph)!")
