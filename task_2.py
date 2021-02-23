"""
This module helps user to navigate through any json file
"""
import json


def get_file():
    """
    Reads json file into python dictionary
    """
    file_path = input("Enter the path to file: ")
    with open(file_path, encoding='utf-8') as file:
        return json.load(file)


def show_keys(entity):
    """
    Shows all the keys of the object if it is dictionary or shows
    all the elements if it is list
    >>> show_keys([1, 2, {}])
    element number 0 is <class 'int'>
    element number 1 is <class 'int'>
    element number 2 is <class 'dict'>
    <BLANKLINE>
    >>> show_keys({"1": 1, "2": [], "pf": 'yeah'})
    1 : <class 'int'>
    2 : <class 'list'>
    pf : <class 'str'>
    <BLANKLINE>
    """
    if type(entity) == dict:
        for key, val in entity.items():
            print(key, ':', type(val))
    elif type(entity) == list:
        for index in range(len(entity)):
            print("element number", index, "is", type(entity[index]))
    print()


def navigation(entity):
    """
    Main function for navigation. Shows the keys on the current level and user chooses the key or moves on the previous
    level (command BACK)
    """
    while True:
        print("\nHere are the available keys\n")
        show_keys(entity)
        print("To go a level back type in BACK")
        choice = input("Enter the key or the index: ")
        if choice == "BACK":
            return True
        else:
            if type(entity) == list:
                try:
                    entity[int(choice)]
                except (ValueError, IndexError):
                    print("\nThere is no such key on this level\n")
                    continue
            elif type(entity) == dict:
                try:
                    entity[choice]
                except KeyError:
                    print("\nThere is no such key on this level\n")
                    continue
            break

    if type(entity) == list:
        choice = int(choice)
    check = type(entity[choice])
    if check == list or check == dict:
        command = navigation(entity[choice])
        if command:
            return navigation(entity)
    else:
        print(entity[choice])


def main():
    data = get_file()
    navigation(data)


if __name__ == "__main__":
    main()
