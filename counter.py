def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")
    handle = open(file_name)
    days = list()
    days_count = dict()
    for line in handle:
        if line.startswith('From'):
            line_split = line.split()
            if len(line_split) > 2:
                days.append(line_split[2])
            
    for day in days:
        days_count[day] = days_count.get(day, 0) + 1
    
    print(days_count)



## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
