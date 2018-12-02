two_equals = 0
three_equals = 0
valid_ids = []

def count_id(line):
    global two_equals
    global three_equals
    global valid_ids
    chars = {}
    for c in line:
        if c not in chars:
            chars[c] = 0
        chars[c] += 1
    found_two = False
    found_three = False
    # Check count
    for c in chars:
        if chars[c] == 2:
            found_two = True
        elif chars[c] == 3:
            found_three = True
    # Update total count
    if found_two:
        two_equals += 1
    if found_three:
        three_equals += 1
    if found_two or found_three:
        valid_ids.append(line)

def get_different_chars(id1, id2):
    different_chars = 0
    for i in range(0, len(id1) - 1):
        if id1[i] != id2[i]:
            different_chars += 1
    return different_chars

def get_common_chars(id1, ids2):
    common_chars = ""
    for i in range(0, len(id1) - 1):
        if id1[i] == id2[i]:
            common_chars += id1[i]
    return common_chars

with open('inputs/day2.txt', 'r') as f:
    lines = f.readlines()

    # Process data
    for line in lines:
        count_id(line)
    
    print("Found {} with two equals".format(two_equals))
    print("Found {} with three equals".format(three_equals))

# Checksum
checksum = two_equals * three_equals
print("Checksum: {}".format(checksum))

# Check valid IDs
for id in valid_ids:
    for id2 in valid_ids:
        different_chars = get_different_chars(id, id2)
        if different_chars == 1:
            print("\nFound two boxes with almost identical IDs: {} and {}".format(id.rstrip('\n'), id2.rstrip('\n')))
            common_chars = get_common_chars(id, id2)
            print("The common chars are: {}".format(common_chars))
