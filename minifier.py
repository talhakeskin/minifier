import sys # for arguments
import re # regex

# structure:
# python3
# [0] -> minifier.py    # source file
# [1] -> fileName
# usage: 'python3 minifier.py fileName.js'
# works only for JS currently.

def readFile(currentFile):
    newFile = currentFile.split(".js")[0] + ".min.js" # filename.js turns into filename and then filename.min.js
    f1 = open(currentFile, "r+") # read
    # ----------------------------------------
    #add a space at the end of the file if the file does not end with space or line feed
    lines = f1.readlines()
    #print(lines[len(lines) - 1]) # last line
    #print(len(lines[len(lines) - 1])) # length of the last line
    #print(lines[len(lines) - 1][len(lines[len(lines) - 1]) - 1]) # index - 1
    if(ord(lines[len(lines) - 1][len(lines[len(lines) - 1]) - 1]) != 10 or ord(lines[len(lines) - 1][len(lines[len(lines) - 1]) - 1]) != 32): # 10 -> LF, 32 -> Space
        f1.close()
        f1 = open(currentFile, "a+") # append
        f1.write(" ")
        f1.close()
    # ----------------------------------------
    f1 = open(currentFile, "r+") # read
    f2 = open(newFile, "w+") # write
    
    lines = f1.readlines()
    for i in range(0, len(lines)):
        word = ""
        for j in range(0, len(lines[i])):
            if(ord(lines[i][j]) == 10 or ord(lines[i][j]) == 32 or ord(lines[i][j]) == 9): # 10 -> LF, 32 -> Space, 9 -> Horizontal Tab
                if(word == "function" or word == "const" or word == "var" or word == "let" or word == "class" or word == "new" or word == "return"):
                    f2.write(word + " ") # word + 1space
                    word = ""
                else:
                    f2.write(word)
                    word = ""
            elif(ord(lines[i][j-1]) != 58 and ord(lines[i][j]) == 47 and ord(lines[i][j+1]) == 47): # removes comments (only //)
                break
            else:
                word = word + lines[i][j]
    f1.close()
    f2.close()


#print(len(sys.argv)) # length test
#print(sys.argv) # argv test
sys.argv.pop(0) # remove source file from the list
#print(sys.argv) # current argv list test
result = re.search("^[a-zA-Z]([a-zA-Z0-9]{0,})(\.js)$", sys.argv[0]) # filename.js format.
if(result):
    readFile(sys.argv[0])

