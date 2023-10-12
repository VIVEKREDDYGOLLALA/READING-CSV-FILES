CSV Data Processor

This Python script provides functions to parse and process CSV data. It includes features to handle headers, values, and create dictionaries for each item in the data.

Functions:
1.parse_headers(header_line)
This function takes a header line from a CSV file and returns a list of headers after stripping whitespace and splitting by commas.

2.parse_values(data_line)
This function processes a line of data from a CSV file. It converts numerical values to floats and handles empty fields, returning a list of values.

3.create_item_dict(values, headers)
This function creates a dictionary where the elements of values become the values and the elements of headers become the keys.

4.read_csv(path)
This function reads a CSV file from the specified path, processes the data, and returns a list of dictionaries representing the items.

Usage
python<>
Copy code
data_dict = read_csv('reading files/deniro.csv')
print(data_dict)

Instructions::
1.Ensure you have a CSV file named deniro.csv in the reading files directory.
2.Use the read_csv() function to read and process the data.
Note:
1.This script assumes that the CSV file has headers in the first line and data starting from the second line.
2.It also handles cases where fields are empty or contain numerical or string values.






