# Writing to the file
with open("BRON.txt", "w") as f:
    f.write("This is my analysis.\n")
    f.write("The purpose of this activity is to practice file handling in Python.\n")
    f.write("We learn how to open, read, write, and print text files line by line.\n")

# Reading from the file
with open("BRON.txt", "r") as f:
    for line in f:
        print(line.strip())
