import traceback

slow_speed = 30  # kph
high_speed = 75  # kph

while True:
    try:
        str_distance = input("Insert the path lenght (in meters): ")
        distance = int(str_distance)
        assert distance >= 0

        str_duration = input("Insert the travel time (in minutes): ")
        duration = int(str_duration)
        assert duration >= 0

    except AssertionError as e:
        print("Input value must be greater than or equal than zero. Try again.")
    except ValueError as e:
        print("Incorrect integer format. Please, review the input and try again.")
    except Exception as e:
        print("Some fatal error happened. Here is the error and the traceback:")
        print(e)
        traceback.print_exc()
        exit(1)
    else:
        break

speed = float(distance / duration) * 60 / 1000

print(f"Train speed is: {speed:.1f} kph")

if speed > high_speed:
    print(f"The train is above the upper speed limit ({high_speed} kph)!")
elif speed < slow_speed:
    print(
        f"The train is below the lower speed limit ({slow_speed} kph)!")
else:
    print(
        f"The train is running at the right speed (between {slow_speed} and {high_speed} kph)!")
