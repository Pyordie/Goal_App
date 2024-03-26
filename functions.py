def get_goals():
    with open("goals.txt", "r") as file:
        goals_local = file.readlines()
    return goals_local


def update_goals(local_goals):
    with open("goals.txt", "w") as file:
        file.writelines(local_goals)

if __name__ == "__main__":
    print("functions is running as main.")