from Constans.constants import memory, decimals

def memory_operations(command, result=None):
    if command == "M+":
        if memory[0] is not None:
            memory[0] += result
        else:
            memory[0] = result
        return f"Memory updated to: {memory[0]:.{decimals}f}" if memory[0] is not None else "Memory updated to: None"
    elif command == "M-":
        if memory[0] is not None:
            memory[0] -= result
        else:
            memory[0] = -result
        return f"Memory updated to: {memory[0]:.{decimals}f}" if memory[0] is not None else "Memory updated to: None"
    elif command == "MR":
        return f"Memory contains: {memory[0]:.{decimals}f}" if memory[0] is not None else "Memory is empty."
    elif command == "MC":
        memory[0] = None
        return "Memory cleared."
    else:
        return "Error: Invalid memory command."
