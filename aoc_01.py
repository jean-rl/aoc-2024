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

    # Create a read-only right list
    right_list_ro = right_list.copy()

    similarity_score = 0
    total_distance = 0 
    while len(left_list) > 0: 
        # Find smallest from left_list and right_list
        left_min = min(left_list)
        right_min = min(right_list)
        # Compute the distance appart and add to the sum
        distance_appart = abs(left_min - right_min)
        total_distance += distance_appart
        # Compute the similarity score
        similarity_score += (right_list_ro.count(left_min) * left_min)
        # Remove the items from both lists
        left_list.remove(left_min)
        right_list.remove(right_min)

    print("Total distance between lists: ", total_distance)
    print("Similarity score between lists: ", similarity_score)


if __name__ == "__main__":
    main()