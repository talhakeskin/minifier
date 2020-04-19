import sys # for arguments

#args = len(sys.argv) -1
# structure:
# python3
# [0] -> minify
# [1] -> fileName
# [2] -> 'as'
# [3] -> newFileName
# usage: 'python3 minify currentFile.txt as newFile.txt'

def readFile(currentFile, newFile):
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
                if(word == "function" or word == "const" or word == "var" or word == "let" or word == "class"):
                    f2.write(word + " ") # word + 1space
                    word = ""
                else:
                    f2.write(word)
                    word = ""
            elif(ord(lines[i][j]) == 47): # 47 -> Slash. It does not include comments.
                break
            else:
                word = word + lines[i][j]
    f1.close()
    f2.close()

readFile("jsFile.js", "output.js")  
