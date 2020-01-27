with open(r"C:\Users\DELL\Downloads\rosalind_iev.txt","r") as my_file:
    for line in my_file:
        string = line.split()
def expected(string):
    sum = (int(string[0])*1 + int(string[1])*1 + int(string[2])*1 + int(string[3])*3/4 + int(string[4])*1/2)*2
    return sum
