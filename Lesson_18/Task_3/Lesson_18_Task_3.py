import mymod as m
import sys

print(m.test('test_file.txt'))

# There was a question in the task:
# "Does your PYTHONPATH need to include the directory where you created mymod.py?"
# Let's find out. Yes, it is including the directory now.
print(sys.path)

# What if we delete it, will this work?
sys.path = ''

# Let's check again.
# Make sure taht PYTHONPATH is empty:
print(sys.path)
# And it works anyway!
print(m.test('test_file.txt'))

# Try running your module on itself: e.g., test("mymod.py")
# It prints the right numbers thanks to f.seek(0) method
print(m.test('mymod.py'))
print(m.test('Lesson_18_Task_3.py'))