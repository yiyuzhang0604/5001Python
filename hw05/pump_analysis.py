import re
# Please run my code with command: python3, otherwise the out put looks differnt

def main():
    filename = input("Enter the file name:")
    print(filename)
    try:
        f = open(filename, "r")
    except FileNotFoundError as e:
        print("Can't open", filename)
        return

    int_list = []
    minute = 0
    power = 0
    for line in f:
        usage = int(line.rstrip('\n'))
        if(usage >= 900):
            minute += 1
            power += usage

        int_list.append(usage)

    # report the time interms of hours
    hour = 60
    day = 24
    total_hours = len(int_list)/hour
    day2 = round(total_hours/day, 3)
    print("Data covers a total of", total_hours, "hours\n(That's", day2, "days)")

    # report for pump
    rate = 2
    gallons = minute * rate
    day_gallon = minute * day * rate
    print("Pump was running for ", minute, "minutes, producing", gallons, "gallons\n(That's", day_gallon, "gallons per day)")

    # report for total power
    wtt = 1000
    power_kwh = round((power/wtt)/hour, 3)
    print("Pump required a total of", power, "watt minutes of power\nThat's", power_kwh, "kWh")

    calculate(5, int_list, rate)
    calculate(100, int_list, rate)

    detect(int_list)


def calculate(target, int_list, rate):
    curr_gallon = 0
    time = 0

    for n in int_list:
        if(curr_gallon < target):
            time += 1
            if not(n == -1 or n == 0):
                curr_gallon += rate

    if (curr_gallon < target):
        time = -1
    else:
        time += 1

    print("It took", time, "minutes of data to reach", target, "gallons")


# extra credits
def detect(int_list,):
    curr_time = 0
    long_list = []
    threshold = 500
    target_min = 120
    for i in range(len(int_list)-1):
        if(int_list[i] >= threshold and int_list[i+1] >= threshold):
            curr_time += 1
        elif(int_list[i] >= threshold and int_list[i+1] < threshold):
            curr_time += 1
            long_list.append([i, curr_time])
        else:
            curr_time = 0

    print("Information on water softener recharges:")
    for long_l in long_list:
        if(long_l[1] >= target_min):
            start_time = long_l[0]-long_l[1]+2
            print(long_l[1], "minutes run started at", start_time)


main()



