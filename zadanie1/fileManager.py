class FileManager:
    # def __init__(self):

    def writeToFile(text, fileName, type=None):
        if(type == "sol"):
            with open("results/" + fileName, 'w') as file:
                if(text[0] == -1):
                    file.write("-1")
                else:
                    file.write(str(text[1]))
                    file.write("\n")
                    file.write(str(text[0]))
                    file.close()
        elif(type == "stats"):
            with open("results/" + fileName, 'w') as file:
                if(text[0] == -1):
                    file.write("-1")
                else:
                    file.write(str(len(text[0])))
                file.write("\n")
                file.write(str(text[2]))
                file.write("\n")
                file.write(str(text[3]))
                file.write("\n")
                file.write(str(text[4]))
                file.write("\n")
                file.write(str(text[5]))
                file.close()