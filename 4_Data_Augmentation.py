
# this does extrapolation of data with different
# permutations and combination
# authors: Meghana Hegde (meghana.hegde@sjsu.edu)
 

import csv
from itertools import permutations

# define source csv and dest csv here.
csv_file = "Transformed_data.csv" # your souce file path
final_csv_file = 'training_dataset_final.csv' # dest file path

disease_to_symptoms = {}
final_lines = []
row_combos = []

def get_symptom_index(row):
    # prepare a dictionary of disease to symptom mapping
    # {'Disease': [index2, index3, index 10].....,}
    # this tells which symptom index is set as"
    symptom_list = []
    for index, element in enumerate(row):
        if index == 0:
            # first is the actual disease name - skip
            continue
        
        # this symptom is set to
        if element == "1.0":
            symptom_list.append(index)

    return symptom_list 

def sublists(values, start, end):
    # this is not an absolute permutation but chooses higher indexs in list
    return [values[m:n + 1] for m in range(start, end+1) for n in range(m, end+1)]

def sublists_recursive(values, index=0, current=[]):
    # more correct recursive solution
    global row_combos

    if index == len(values):
        if len(current) >= len(values)/2:
            row_combos.append(current)
        return
    sublists_recursive(values, index+1, current)
    sublists_recursive(values, index+1, current + [values[index]])

def generate_permutations(key, value):
    # generate all perms of the key value pair
    global final_lines

    # get the permutations of valid indices
    #print(key)
    #print(value)
    symptoms_len = len(value)

    new_index_rows = sublists(value, 0, len(value) -1)

    # prepare the entire row based on a new permutation
    for row in new_index_rows:

        # this is some optimization - dont pick up list of symptoms
        # which are very short compared to original list
        # that leads to very bad prediction
        # lets tune it to 1/4 of original symptoms and greater.
        if len(row) < int(symptoms_len/4):
            continue

        # bad row?
        if row is None:
            continue

        if len(row) == 0:
            continue

        new_line = []

        # first column - the disease itself
        new_line.append(key)

        # 404 features total - whichever index is valid - set 1.0 for that.
        for index in range(1, 405):
            if index == 0:
                continue
            if index in row:
                new_line.append("1.0")
            else:
                new_line.append("0.0")

        final_lines.append(new_line)
        

# source file; read it
with open(csv_file, 'r') as file:

    csv_reader = csv.reader(file)
    header = next(csv_reader)

    for row in csv_reader:
        # Each row is a list representing the fields in that row
        disease_to_symptoms[row[0]] = get_symptom_index(row)
        final_lines.append(row)

# walk through all key value mappings to generate more logs
for key, value in disease_to_symptoms.items():
    generate_permutations(key, value)

print(len(final_lines))

# write it back to extrapolated CSV
with open(final_csv_file, 'wt') as myFile:
    wr = csv.writer(myFile)
    wr.writerow(header)
    wr.writerows(final_lines)

