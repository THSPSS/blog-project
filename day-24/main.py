# with open("my_file.txt") as file: #take some places in computer
#    contents = file.read()
#    print(contents)   #no need to using close it down
# "../../OneDrive/Desktop/my_file.txt"  relative file path
#"/Users/Main/OneDrive/Desktop/my_file.txt"  absolute file path


with open("C:/Users/Main/OneDrive/Desktop/my_file.txt", mode="a") as file:  #a = append
    file.write("\nNew text.")

with open("new_file.txt", mode="w") as file:  #making new file only avilable in w mode and when file doesn't exist.
        file.write("New text.")