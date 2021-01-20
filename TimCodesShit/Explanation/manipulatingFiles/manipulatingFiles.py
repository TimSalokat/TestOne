
#open a file with read and write rights
with open("/home/kali/Documents/Python/Explanation/manipulatingFiles/test.txt", "r+") as file:
    print("line1 ", file.readlines(1))
    print("line2 ", file.readlines(1))
    print("line3 ", file.readlines(1))