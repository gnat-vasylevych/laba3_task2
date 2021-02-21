import json


def get_file():
    # file_path = input("Enter the path to file: ")
    file_path = "frienfs_list_Obama.json"
    with open(file_path, encoding='utf-8') as file:
        return json.load(file)


def show_keys(object):
    if type(object) == dict:
        for key, val in object.items():
            print(key, ':', type(val))
    elif type(object) == list:
        for index in range(len(object)):
            print("element number", index, "is", type(object[index]))
    print()


def navigation(object):
    print("Here are the available keys\n")
    show_keys(object)
    print("To go a level back type in BACK")
    choice = input("Enter the key or the index: ")
    if choice == "BACK":
        return True
    if type(object) == list:
        choice = int(choice)
    check = type(object[choice])
    if check == list or check == dict:
        command = navigation(object[choice])
        if command:
            navigation(object)
    else:
        print(object[choice])


def main():
    data = get_file()
    navigation(data)


main()