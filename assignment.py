# You can remove 'pass' if you written code in the function
# Exercise 1
def write_shopping_list(items, filename):
    file=open(filename,"w")
    c=1
    for i in items:
        file.write(f"{c}. {i}\n")
        c=c+1
    file.close()
# Exercise 2
def read_names(filename):
    file = open(filename,"r")
    lst = []
    lines = file.readlines()
    for line in lines:
        if line.strip()!="":
            lst.append(line.strip())
    file.close()
    return lst

# Exercise 3
def append_entry(filename, text):
    file = open(filename, "a")
    file.write(text + "\n")
    file.close()
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    return len(lines)
# Exercise 4
def search_file(filename, word):
    file = open(filename, "r")
    lst = []
    c=0
    lines = file.readlines()
    for line in lines:
        c=c+1
        if word in line.strip().lower():
            lst.append(c)
    return lst

# Exercise 5
def number_the_lines(source, destination):
    file_in = open(source, "r")
    file_out = open(destination, "w")
    lines = file_in.readlines()
    c = 0
    for line in lines:
        c = c + 1
        file_out.write(str(c) + ": " + line)
    file_in.close()
    file_out.close()
    return c
