#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg


with open("data.txt") as datafile:
    data = datafile.readlines()

data = [entry.rstrip().split(" | ") for entry in data]
p1_data = [vals[1].split(" ") for vals in data]
data_flat = []
for vals in p1_data:
    for item in vals:
        data_flat.append(item)

counter = 0
for vals in data_flat:
    if len(vals) == 2 or len(vals) == 3 or len(vals) == 4 or len(vals) == 7:
        counter += 1

print(counter)
