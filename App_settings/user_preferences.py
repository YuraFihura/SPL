from Constans import constants


def set_user_preferences():
    try:
        decimals_input = input("Enter the number of decimal places for results (default is 2): ")
        constants.decimals = int(decimals_input)
    except ValueError:
        print("Invalid input. Using default decimal places.")
        constants.decimals = 2

    auto_save_memory_input = input(
        "Enable automatic memory save after each calculation? (yes/no, default is yes): ").strip().lower()
    if auto_save_memory_input in ("no", "n"):
        constants.auto_save_memory = False
    elif auto_save_memory_input in ("yes", "y"):
        constants.auto_save_memory = True
    else:
        print("Invalid input. Using default value for auto save memory (yes).")
        constants.auto_save_memory = True
