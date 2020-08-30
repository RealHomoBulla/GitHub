'''Task 2
The sys module.
The “sys.path” list is initialized from the PYTHONPATH environment variable.
Is it possible to change it from within Python? If so, does it affect where Python looks for module files?
Run some interactive tests to find it out.'''

import sys

print(sys.path)
# ['/Users/homo_bulla/Py/GitHub/Lesson_18', '/Users/homo_bulla/Py/GitHub',    # PYTHONPATH is this one
# '/Library/Frameworks/Python.framework/Versions/3.8/lib/python38.zip',
# '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8',
# '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload',
# '/Users/homo_bulla/Library/Python/3.8/lib/python/site-packages',            # Will try to change to THIS ONE
# '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages']

# sys.path is just a list with strings, so we can print elements of list by index.
print(sys.path[0])

# I want to change PYTHONPATH to '/Users/homo_bulla/Library/Python/3.8/lib/python/site-packages',
sys.path[0] = '/Users/homo_bulla/'
print(sys.path[0])
# It works.

# But if we try this:
#    import Lesson_18.Task_1.Lesson_18_Task_1 as m
#    print(m.x)
# We will get an error "ModuleNotFoundError: No module named 'some_module'"









