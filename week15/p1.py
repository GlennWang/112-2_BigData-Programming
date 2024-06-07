import re

fname = 'MySQL-OperationPractice-Chinese-BigData.html'
with open(fname, "r", encoding='big5') as fp:
    data = fp.read()

data = re.sub("<.+?>",'', data)
print(data)

lines = data.split('\n')

rules = ['mysql&gt;', '-&gt;', '+', '|',]
result = []

for line in lines:
    for rule in rules:
        if rule in line:
            line = line.lstrip()
            if rule == 'mysql&gt;':
                line = re.sub('mysql&gt; ', '', line)
                line = re.sub('&gt;', '<', line)
                line = re.sub('&gt;', '>', line)
            elif rule == '-&gt;':
                line = re.sub('-&gt; ', '', line)
            result.append(line)
            break

print(result)
result = '\n'.join(result)

with open('mySQL-code.txt', "w") as fp:
    fp.write(result)