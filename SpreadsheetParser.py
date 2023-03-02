# parser.py
# Ethan Mayer
# 2/28/23
# Created for use by the Vanderbilt University Department of Biology's Ecology research labatories

# Imports
import csv

# Input text prompts for user
print("Spreadsheet Parser Script")
print("The only function of this parser at the moment is to split the \"cluster-site-camera-year\" data format in the first column to \"cluster\", \site\", and \"camera\" in the first 3 columns, respectively.")

# Prompt for filename
print("Please enter the filename of the spreadsheet WITH the file extension (example: sheet.csv):")
filename = input()

# If input is not a valid string, reprompt
while (type(filename) is not str):
    print("Error: please input a valid filename:")
    filename = input()

# Prompt for number of lines to skip
print("Please enter the number of rows to skip (the first row is usually skipped because it contains titles, thus input \"1\", but you may have done the second row (first row of data) by hand, thus input \"2\"):")
skip = input()

# If input is not a valid integer, reprompt
while (type(skip) is not int):
    print("Error: please input an integer:")
    skip = input()

# Output csv file name
output = "output.csv"

# Read the provided csv file and create the output csv file
try:
    with open(filename, 'r') as file, open(output, "w", newline='') as outFile:
        # Create csv reader and writers
        reader = csv.reader(file, delimiter = ',')
        writer = csv.writer(outFile, delimiter = ',')

        # Extract the user-specified number of rows without touching them (column titles in the first row, usually)
        for i in range(skip):
            header = next(reader)
            writer.writerow(header)

        # Parse each row of the current spreadsheet
        for row in reader:
            colValues = []
            colN = 0 # Which column we are on (only looking to parse columns 1-3)

            # Parse each column of the current row
            for col in row:
                dash = 0
                cluster = ""
                site = ""
                cam = ""

                # Parse the contents of each cell of the current column
                if colN < 3:

                    # Parse through each character
                    # (Looking for dash deliminated date in the form cluster-sxx-cxx-xxF where cluster is a string, x is an integer, s stands for site, c stands for sluter, F stands for F(all) or S(pring))
                    for i, char in enumerate(str(col)):

                        # Check first word for cluster
                        if char == '-' and dash == 0:
                            cluster = col[0:i]
                            dash = dash + 1
                            colValues.append(cluster)

                        # Check second word for site number and third word for camera number
                        # Both done here since the third dash is NOT guaranteed
                        elif char == '-' and dash == 1:
                            site = col[i-2:i]
                            for j, c in enumerate(site):
                                if j == 0 and c == '0':
                                    site = site[1]
                            dash = dash + 1
                            colValues.append(site)
                            cam = col[i+2:i+4]
                            colValues.append(cam)
                            break # Once all relevant data is extracted, break and stop looking for the data
                else:
                    # Write rest of cells untouched
                    colValues.append(col)

                colN = colN + 1

            # Write the new row to the output csv file
            writer.writerow(colValues)
except:
    # Either file name was wrong, file is not found in the current directory, or this script has a lack of read/write permissions
    print("Error: the filename you have provided was not found in the current directory.")