def main():
    with open("input_03.txt", "r", encoding="utf-8") as file:
        memory = "".join(list(file))

    idx = 0 # Start reading the first character in the file
    end_idx = len(memory)
    total = 0

    while idx < end_idx:
        result, idx = search_mul(memory, idx)
        total += result

    print("Total: ", total)


def search_mul(memory, idx):
    """
    Search for the first ocurrence of the mul(x,y) pattern in the memory. Return
    the operation result and the index of the next position after the ocurrence.
    If n
    """

    left_op = 0
    right_op = 0

    idx = memory.find("mul(", idx) # Return the idx of "m" in "mul("
    if idx == -1:
        return 0, len(memory)
    idx = idx + len("mul(") # At this point the idx is at mul([here]

    # Search for a string of 1 to 3 digits ending with comma
    digits = ""
    while idx < (idx+2) and memory[idx].isdigit():
        digits += memory[idx]
        idx += 1
    if idx < len(memory) and memory[idx] == ",":
        left_op = int(digits)
        idx += 1
    else:
        return 0, idx

    # Same as previous but the string must end with ")"
    digits = ""
    while idx < (idx+2) and memory[idx].isdigit():
        digits += memory[idx]
        idx += 1
    if idx < len(memory) and memory[idx] == ")":
        right_op = int(digits)
        idx += 1
    else:
        return 0, idx

    #print(memory[start_idx:left_idx])
    #print(f"Found mul: {left_op} x {right_op}")
    result = left_op * right_op
    return result, idx


if __name__ == "__main__":
    main()

# Total:  175015740