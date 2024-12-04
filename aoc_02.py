def main():
    reports = list()
    with open("./input_02.txt", "r", encoding="utf-8") as file:
        # Better way to read the input, instead of using while loop
        for line in file:
            report_str = line.split()
            reports.append([int(x) for x in report_str])

    safe_counter = 0
    for report in reports:
        if check_safety(report) is True:
            safe_counter += 1
        elif problem_dampener(report) is True:
            safe_counter += 1

    print("Safe counter: ", safe_counter)

def check_safety(report):
    if sorted(report) == report or sorted(report, reverse=True) == report:            
        for previous, current in zip(report, report[1:]):
            diff = abs(previous - current)
            if 1 <= diff <= 3:
                continue
            return False
        return True
    
def problem_dampener(report):
    for i, _ in enumerate(report):
        _report = report.copy()
        _report.pop(i)
        if check_safety(_report) is True:
            return True
    return False

if __name__ == "__main__":
    main()