### load library for regular expression
import re
### HTML source codes
string = '<a href="https://www.chicagobooth.edu/faculty/directory/g/veronica-guerrieri" id="13"> Veronica Guerrieri</a>'
### . means any character, + means one or more occurrences, the whole sentence means to find all patterns that match anything between ">" and "</a>"
x = re.findall('>.+</a>', string)
print(x)
### The output is: ['> Veronica Guerrieri</a>'], You need to remove ">" and "</a>"