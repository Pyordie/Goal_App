import functions
import time


user_text = "Type add, show, edit, delete or exit:"
today_Date = time.strftime("%Y-%h-%d")
print(f"Today is {today_Date}")
while True:
    user_inp = input(user_text).strip()

    if user_inp.startswith("add"):

        goals = functions.get_goals()

        goal = user_inp[4:] + "\n"
        goals.append(goal.capitalize())

        functions.update_goals(goals)

    elif user_inp.startswith("show"):

        goals = functions.get_goals()

        goals = [item.strip("\n") for item in goals]
        for index, item in enumerate(goals):
            output = f"{index + 1}- {item.title()}"
            print(output)

    elif user_inp.startswith("edit"):
        try:
            goals = functions.get_goals()

            number = int(user_inp[5:])
            new_goal = input("Type new goal :")
            goals[number - 1] = new_goal + "\n"

            functions.update_goals(goals)
        except ValueError:
            print("you entered the wrong command !")
            continue
    elif user_inp.startswith("delete"):
        try:
            goals = functions.get_goals()

            goal_t_delete = int(user_inp[7:])
            deleted = goals[goal_t_delete - 1].strip("\n")
            goals.pop(goal_t_delete - 1)
            print(f"Goal ({deleted}) is removed from the list.")

            functions.update_goals(goals)
        except ValueError:
            print("There is no item with that number !")
            continue
    elif "exit":
        break
    else:
        print("You entered a wrong command.")
print("bye".capitalize())
