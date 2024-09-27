

# It is used to find the patterns in the string data  and manipulating strings
# Ex: Phone number,email,country code, pincode etc
# It is mainly useful in building a compiler to read the code and the respective keywords in a language
# It used to extract information from logfiles,spread sheets, or even textual data
# Use Cases
# 1. Searching and replacing text in files
# 2. Validating text input such as password and emailaddress
# 3. Rename a hundred files at a time.

# Matching the characters
# Character - Description
# 1. \d  - Match any digit
# 2. \s  - Match any whitespace
# 3. \w  - Match any alphanumeric char
# 4. \D  - Match any non-digit
# 5. \S  - Match any non-whitespace
# 5  \W  - Match any non-alphanumeric char

# Tools and website for Regex
# 1. RegexOne
# 2. RegExr

# How to write a Regex Expression for pattern Matching
# /. --> It highlights the entire data
# . --> It highlights the single character
# \w --> Matching each and every character
# \d --> Searches for digit
# \s --> Highlights the empty spaces which are given
# \D --> Highlights all the non-numeric data
# \W --> Highlights all the non-alphanumeric data
# \S --> Highlights all the non-empty spaces
# /the --> It matches/highlights every where the character or the word 'the' is present
# With the above expression we can also identify/count  the number of characters or text is given in a document

# \w+ --> It matches the entire word following a specific character without highlighting a special character more than one character matching
# \w* --> It matches more the zero character

# Pattern for matching a simple email address--> \w+@\w+.\w+
# We need to make pattern which makes universally accepting lot of email address
# [abc] --> matches only a,b, or c
# [^abc] --> not a,b or c
# \w{3} --> matches the character along with the length{3} matches the character containg a length of 3
# \w{3,} --> matches the character which has a length of 3 or greater than 3
# (\w+)_|. --> It matches the character followed by underscore or .
# Patterns in email address matching
# 1. (\w+)(_|.)(\w+)@(\w+)\.[a-z]{3} --> dhanush_aravind@gamil.com
# 2. (\w+)(_|.)(w+)@(\w+)\.[a-z]{2,3} --> dhanush_aravind@gamil.in/com
# always use cheatsheet to create patterns.

line = 'I Love Data Science'



line.split()

import re
# First we need to compile the regular expression to identify no syntax error is present
regex =  re.compile('\s+')
regex.split(line)

for s in ["  ","abc  ","  abc"]:
  if regex.match(s):
    print(repr(s), "matches")
  else:
    print(repr(s), "does not match")

# Difference between print() and repr():
print("Hello World!")
repr("Hello World!") #It is very much useful if there are any empty spaces in the string

line.index("Data")

regex = re.compile('Data')
match = regex.search(line)
match.start()

line.replace('Data Science','Dhanush')

regex = re.compile("Data Science")
regex.sub('Aravindh',line)

text = "Dhanush Aravindh is a Data Scientist and his mail is dhanush.aravindh@gmail.com"

# Extracting the strings from email
# Whenever we use round braces it will create a group
# It extracts username and domain separately
email = re.compile('(\w+)\.(\w+)@(\w+)\.[a-z]{3}')
email.findall(text)

# When we have to extract the entire email we can use
import re
email = re.compile('[\w.]+@\w+\.[a-z]{3}')
email.findall(text)

# Apply regex in raw string format
# Every character is printed with tab space \t
print('a\tb\tc')

# Every character is printed in a new line
print('a\nb\nc')

# Whenever reading a string we may face this error. while handling string in python
# to overide the escape character we can use 'r'+ string format

print(r'a\tb\tc')

email3 = re.compile(r'([\w.]+)@(\w+)\.([a-z]{3})')
email3.findall(text)

email4 = re.compile(r'(?P<user>[\w.]+)@(?P<domain>\w+)\.(?P<suffix>[a-z]{3})')
regex = email4.match('dhanush.aravind@gmail.com')
regex.groupdict()

# We have used the tags to identify user,domain and suffix









