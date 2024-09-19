from Constans.constants import history, decimals

def add_to_history(expression, result):
    history.append(f"{expression} = {result:.{decimals}f}")

def show_history():
    if history:
        for entry in history:
            print(entry)
    else:
        print("History is empty.")
