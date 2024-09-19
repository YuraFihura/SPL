from Function.calculator import calculate
from Function.memory import memory_operations
from Function.history import add_to_history, show_history

from Constans.constants import decimals, memory, auto_save_memory
from App_settings.user_preferences import set_user_preferences

while True:
    try:
        action = input(
            "Do you want to configure settings, use memory operations, or view history? "
            "(S for settings, M+, M-, MR, MC, H for history, or press Enter to continue with calculation): ").upper()
        if action == "S":
            set_user_preferences()
            continue
        elif action in ("M+", "M-", "MR", "MC"):
            result = None  # result is used to store the result of the calculation for memory operations
            if action in ("M+", "M-", "MR"):
                # Perform calculation if action requires memory operations
                number1 = float(input("Enter the first number: "))
                operator = input("Enter the operator (+, -, *, /, ^, √, %): ")
                if operator == "√":
                    result = calculate(number1, 0, operator)
                else:
                    number2 = float(input("Enter the second number: "))
                    result = calculate(number1, number2, operator)

            print(memory_operations(action, result))
            continue
        elif action == "H":
            show_history()
            continue

        # Perform calculations if no memory or history action is selected
        number1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /, ^, √, %): ")
        if operator == "√":
            result = calculate(number1, 0, operator)
            expression = f"√{number1}"
        else:
            number2 = float(input("Enter the second number: "))
            result = calculate(number1, number2, operator)
            expression = f"{number1} {operator} {number2}"

        print(f"Result: {result:.{decimals}f}")

        if isinstance(result, (int, float)):  # Only add valid results to history
            add_to_history(expression, result)
            if auto_save_memory:
                memory[0] = result  # Automatically store the result in memory if enabled

    except ValueError:
        print("Error: Please write the correct number.")

    repeat = input("Would you like to perform another calculation? (Yes/No): ").lower()
    if repeat != "yes":
        print("Program terminated.")
        break
