def main():
    # Read input as two lists
    left_list = list()
    right_list = list()
    with open("./input_01.txt", "r") as f:
        line = f.readline().split()
        while line:
            left_list.append(int(line[0]))
            right_list.append(int(line[1]))
            line = f.readline().split()

    sum = 0 
    while len(left_list) > 0: 
        # Find smallest from left_list and right_list
        left_min = min(left_list)
        right_min = min(right_list)
        # Compute the distance appart and add to the sum
        distance_appart = abs(left_min - right_min)
        sum += distance_appart
        # Remove the items from both lists
        left_list.remove(left_min)
        right_list.remove(right_min)

    print(sum)


if __name__ == "__main__":
    main()