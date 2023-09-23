# use this script to parse the derewo datasets
# execute this script from the root folder of the project

import os

dataset_path = "./datasets/derewo/"
source_file = dataset_path + "derewo-v-30000g-2007-12-31-0.1/derewo-v-30000g-2007-12-31-0.1"
target_filename = "derewo-30000g.txt"

# create the output folder if it doesn't exist
if not os.path.exists(dataset_path + "parsed/"):
    os.makedirs(dataset_path + "parsed/")
target_file = dataset_path + "parsed/" + target_filename

# read the source file
source_lines = []
past_header = False
with open(source_file, 'r') as file:
    for line in file:
        if past_header and len(line.strip()) > 0:
            source_lines.append(line.strip().lower())
        if line.startswith("--------------"):
            past_header = True

# remove numbers
words = []
for line in source_lines:
    words.append(line.split("\t")[0])

words.sort()

# write the output file
with open(target_file, 'w') as file:
    for word in words:
        file.write(word + "\n")
