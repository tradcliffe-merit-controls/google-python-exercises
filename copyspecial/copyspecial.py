#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_files(dir):
  ptrn_matches = []
  filenames = os.listdir(dir)
  for file in filenames:
    match = re.search(r'\w*__\w*__\.\w*', file)
    if match:
        abs_path = os.path.abspath(os.path.join(dir, file))
        ptrn_matches.append(abs_path)
  return ptrn_matches

def cpy_special_files(dir, files):
  here = os.path.abspath('./')
  print(here)
  if not os.path.exists(dir):
    os.mkdir(dir)
  for f in files:
      shutil.copy(f, dir)

def zip_special_files(new_name, files):
#   absolute path does not work on wsl. SO this won't work here but it is the solution. FOr wsl need to have the ~/code instead of the home/tradcliffe/code
# in real coding situations I would try and check if I was in wsl

  if len(files) == 0:
    print('No files found')
    sys.exit(1)

  cmd = 'zip -j ' + new_name + ' ' + ' '.join(files)
  print('Doing something, hoping for the best: ' + cmd)
  (status, output) = subprocess.getstatusoutput(cmd)
  if status:
    print('error?')
    sys.stderr.write(output)
    sys.exit(1)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print('usage: [--todir dir][--tozip zipfile] dir [dir ...]')
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if not args: # A zero length array evaluates to "False".
    print('error: must specify one or more dirs')
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  fetch_files = get_special_files(args[0])
  if todir:
    print('todir')
    cpy_special_files(todir, fetch_files)
  elif tozip:
    print('tozip')
    zip_special_files(tozip, fetch_files)
  else: 
    if len(fetch_files) > 0: 
      for file in fetch_files:
        print(file)
    else:
      print('No special files')
      

if __name__ == '__main__':
  main()
