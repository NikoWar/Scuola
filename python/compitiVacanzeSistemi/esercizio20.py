from sys import argv

script, input_file = argv   #file argument

current_line = 0

def print_all(f):
    print(f.read()) #print the content of the file

def rewind(f):
    f.seek(0)   #goto the first byte in the code

def print_a_line(f):
    current_line += 1
    print(current_line, f.readline()) #print only the n line

current_file = open(input_file) #open file and assignament

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")


print_a_line(current_file)

print_a_line(current_file)

print_a_line(current_file)