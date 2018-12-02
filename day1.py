frequency = 0
reached_frequencies = set()

def find_repeated_frequency():
    global frequency
    global reached_frequencies
    while True:
        for line in lines:
            num = int(line.rstrip('\n'))
            frequency += num
            if frequency in reached_frequencies:
                return
            else:
                reached_frequencies.add(frequency)
        # print("Current freq: {}".format(frequency))

with open('inputs/day1.txt', 'r') as f:
    lines = f.readlines()

    # Step 1
    for line in lines:
        frequency += int(line.rstrip('\n'))
    print("Calibrated frequency: {}".format(frequency))

    # Step 2
    frequency = 0
    find_repeated_frequency()
    print("First repeated frequency: {}".format(frequency))


    



