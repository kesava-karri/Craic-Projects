#!/usr/bin/python3.9
"""
Note:
Using subprocess module as it's much safer in comparison to using os module
"""

import subprocess

with open('count.txt', 'r+') as f:
  count = f.read()
  inputName = str(input("Enter the file name: "))
  concatenatedName = f"{count}. {inputName}"
  fileJS = f"{concatenatedName}/{inputName}.js"
  fileTS = f"{concatenatedName}/{inputName}.ts"
  
  subprocess.run(['mkdir', concatenatedName])
  subprocess.run(['touch', fileJS])
  subprocess.run(['touch', fileTS])
  # Use seek between read & write to move the cursor to the start of file
  f.seek(0)
  count = int(count) + 1
  f.write(str(count))
  # Truncate to make sure that the new data if longer still gets considered
  f.truncate()
