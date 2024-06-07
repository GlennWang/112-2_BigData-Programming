import re

# Read the HTML file with Big5 encoding
fname = 'MySQL-OperationPractice-Chinese-BigData.html'
with open(fname, "r", encoding='big5') as fp:
    data = fp.read()

# Remove HTML tags
data = re.sub("<.+?>", '', data)

# Split the data into lines
lines = data.split('\n')

# Initialize result list to store MySQL commands
result = []

# Process each line
for line in lines:
    if 'mysql&gt;' in line:
        # Remove leading spaces and specific HTML entities
        line = line.lstrip()
        line = re.sub('mysql&gt; ', '', line)
        line = re.sub('&nbsp;', ' ', line)
        line = re.sub('&lt;', '<', line)
        line = re.sub('&gt;', '>', line)
        # Append cleaned line to result
        result.append(line)

# Join the result into a single string with newlines
result = '\n'.join(result)

# Write the result to a new text file
with open('mySQL-onlycode.txt', "w", encoding='utf-8') as fp:
    fp.write(result)

print("MySQL commands have been extracted and saved to 'mySQL-code.txt'.")
