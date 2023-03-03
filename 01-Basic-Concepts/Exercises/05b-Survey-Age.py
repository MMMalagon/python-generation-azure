import traceback


surveys = []  # [(age, score)]
running = True

under_age = 18
upper_age = 55


def get_input(prompt):
    global running
    value = input(prompt)

    if value.upper() == 'Q':
        running = False
        return None
    else:
        return value


while running:

    age = score = None

    try:

        while running:
            try:
                str_age = get_input("Insert the age or press 'Q' to exit: ")
                if not running:
                    break
                age = int(str_age)
                if age < 0:
                    raise ValueError
            except ValueError as e:
                print("Age must be an integer greater than or equal to zero. Try again.")
            else:
                break

        while running:
            try:
                str_score = get_input("Insert the score or press 'Q' to exit: ")
                if not running:
                    break
                score = int(str_score)
                if score < 0 or score > 10:
                    raise ValueError
            except ValueError as e:
                print("Score must be an integer between 0 and 10. Try again.")
            else:
                break

    except Exception as e:
        print("Some fatal error happened. Here is the error and the traceback:")
        print(e)
        traceback.print_exc()
        exit(1)

    else:
        if running:
            surveys.append((age, score))

if (len(surveys) > 0):
    print("Survey summary:")

    print(f"Total surveys: {len(surveys)}")

    print(f"Mean score: {sum([survey[1] for survey in surveys]) / len(surveys)}")


    under_age_score_list = [survey[1] for survey in surveys if survey[0] < under_age]
    if (len(under_age_score_list) > 0):
        print(f"Mean score for under age ({under_age}): {sum(under_age_score_list) / len(under_age_score_list)}")
    else:
        print(f"No mean score for under age ({under_age})")

    middle_age_score_list = [survey[1] for survey in surveys if survey[0] >= under_age and survey[0] <= upper_age]
    if (len(middle_age_score_list) > 0):
        print(f"Mean score for middle age (between {under_age} and {upper_age}): {sum(middle_age_score_list) / len(middle_age_score_list)}")
    else:
        print(f"No mean score for middle age (between {under_age} and {upper_age})")


    upper_age_score_list = [survey[1] for survey in surveys if survey[0] > upper_age]
    if (len(upper_age_score_list) > 0):
        print(f"Mean score for upper age ({upper_age}): {sum(upper_age_score_list) / len(upper_age_score_list)}")
    else:
        print(f"No mean score for upper age ({upper_age})")

else:
    print("No surveys have been completed.")

print("Exiting...")
