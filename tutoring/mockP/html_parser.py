import sys
import re

with open(input(), 'r') as file:
    for i, line in enumerate(file):
        print(re.sub("[0-9a-zA-Z]+@[a-zA-Z]+.[a-zA-Z]+","",line))
        
