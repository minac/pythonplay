#!/usr/bin/python
'''
Python script to print a random common misconception from Wikipedia's page of common misconceptions
'''

import wikipedia
import re
from random import randint

# Get wikipedia page
locm = wikipedia.page("List of common misconceptions")

# Split it line by line
lines = re.split(r'\n', locm.content)

# Remove end section of page
noEndPage = []
for line in lines:
    if line != "== See also ==":
        noEndPage.append(line)
    else:
        break

# Remove titles and empty lines
locm_content = []
for line in noEndPage:
    if not(re.match(r'===', line)) and not(re.match(r'^$', line)):
        locm_content.append(line)

# Generate random index of locm array
rand = randint(0, len(locm_content))

# Print random Common Misconception
print locm_content[rand]
