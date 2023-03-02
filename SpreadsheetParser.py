# parser.py
# Ethan Mayer
# 2/28/23

import csv

print("Spreadsheet Parser Script")
print("The only function of this parser at the moment is to split the "cluster-site-camera-year" data format in the first column to "cluster", "site", and "camera" in the first 3 columns, respectively.")
print("Please enter the filename of the spreadsheet WITH the file extension (example: sheet.csv):")
filename = input()

# csv file name
#filename = "2.27.raw.csv"
output = "output.csv"

# read csv file
try:
    with open(filename, 'r') as file, open(output, "w", newline='') as outFile:
        # create csv reader and writers
        reader = csv.reader(file, delimiter = ',')
        writer = csv.writer(outFile, delimiter = ',')

        # extracting field names through first row
        header = next(reader)
        writer.writerow(header)
        header = next(reader)
        writer.writerow(header)

        # extracting each data row one by one
        for row in reader:
            colValues = []
            colN = 0

            # parsing each column of a row
            for col in row:
                dash = 0
                cluster = ""
                site = ""
                cam = ""

                # parsing each column
                if colN < 3:
                    # parse through each character
                    for i, char in enumerate(str(col)):
                        # check first for cluster
                        if char == '-' and dash == 0:
                            cluster = col[0:i]
                            dash = dash + 1
                            colValues.append(cluster)
                        # check second for site and third for cam
                        # both done here since the third dash is not guaranteed
                        elif char == '-' and dash == 1:
                            site = col[i-2:i]
                            for j, c in enumerate(site):
                                if j == 0 and c == '0':
                                    site = site[1]
                            dash = dash + 1
                            colValues.append(site)
                            cam = col[i+2:i+4]
                            colValues.append(cam)
                            break
                else:
                    # write rest of columns untouched
                    colValues.append(col)

                colN = colN + 1

            # write row to csv file
            writer.writerow(colValues)
except:
    print("Error: the filename you have provided was not found.")


