import traceback


surveys = []

while True:
    try:
        score_str = input(
            "Insert your score between 0 and 10 or press 'Q' to exit: ")
        if score_str.upper() == 'Q':
            break
        score_num = int(score_str)
        if score_num < 0 or score_num > 10:
            raise ValueError
    except ValueError as e:
        print(
            "Incorrect input format. The score must be an integer between 0 and 10.")
    except Exception as e:
        print("Some fatal error happened. Here is the error and the traceback:")
        print(e)
        traceback.print_exc()
        exit(1)
    else:
        surveys.append(score_num)

if (len(surveys) > 0):
    print("Survey summary:")

    print(f"Total surveys: {len(surveys)}")

    print(f"Mean score: {sum(surveys) / len(surveys)}")

else:
    print("No surveys have been completed.")

print("Exiting...")
