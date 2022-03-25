#! /usr/bin/env python
import sys
import shutil
import os

# Install attached files in appropriate locations
# Find anuga:
try:
    import anuga
except:
    print('\n')
    print('#' * 60)
    print('CANNOT INSTALL THE FILES')
    print('ANUGA must be installed before running this script.')
    print('Find it at https://github.com/GeoscienceAustralia/anuga_core')
    print('#' * 60)
    print('\n')
    sys.exit()
    
path_to_anuga = anuga.__path__[0]

# Files to copy
file1 = 'shallow_water_domain.py'

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)

# Copy files
src1 = os.path.join(path,file1)
dst1 = os.path.join(path_to_anuga,'shallow_water',file1)
shutil.copy2(src1, dst1)

# Success message
#print('Success!')
print('Installed extra codes in appropriate folders')
