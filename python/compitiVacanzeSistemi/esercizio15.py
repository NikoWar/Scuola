from sys import argv

script, filename = argv #tupla assignament

txt = open(filename)    #second argument file opening

print(f"Here's your file {filename}:")  #print the name of the file
print(txt.read())   #print the content of the file

print("Type the filename again:")   
file_again = input("> ")    #input function to write the filename again

txt_again = open(file_again)    #open file again

print(txt_again.read()) #print the content

txt.close()
txt_again.close()
