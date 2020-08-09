'''Task 1
Files
1) Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it.
2) Then write another script that opens myfile.txt, and reads and prints its contents.
3) Run your two scripts from the system command line.
4) Does the new file show up in the directory where you ran your scripts?
5) What if you add a different directory path to the filename passed to open?
Note: file write methods do not add newline characters to your strings;
add an explicit ‘\n’ at the end of the string if you want to fully terminate the line in the file.'''

# 1) Script 1 can be this:
with open('../Archive/myfile.txt', 'w') as f:
    f.write('Hello file world!\n')
# 2) Script 2 can be this:
with open('../Archive/myfile.txt') as f:
    print(f.read())

# 3) To run this from a command line I will open directory with terminal command 'cd', check that
# script is within directory using command 'ls -la',
# and then I will open python file with the command 'python3 Lesson_9_Task_1.py'.

# 4) Again we use 'ls -la' to make sure that file was created in the folder. Yes it is!

# 5) I can open this file even from my home directory. To go to home directory we use command 'cd', and there I use
# command 'python3 Py/GitHub/Lesson_09/Lesson_9_Task_1.py' to open file at any directory, only need to specify
# correct full Path using '/' for directories.