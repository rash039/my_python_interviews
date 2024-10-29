def print_details(data: dict):
    try:
        name = data["name"]
        roll = data["roll"]
        print(f"Name is {name}")
        print(f"Roll is {roll}")
    except Exception as e:
        print("General exception")
    except KeyError as e:
        print(f"{e.args[0]} is missing")

info = {"name_1": "Jack", "roll": "1"}
print_details(info)