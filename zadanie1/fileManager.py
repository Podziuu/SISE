class FileManager:

    def getPuzzle(fileName):
        with open("ukladanki/" + fileName, "r") as file:
            lines = file.readlines()
            dimensions = list(map(int, lines[0].split()))

            state = []
            for line in lines[1:]:
                row = list(map(int, line.split()))
                state.extend(row)

            return dimensions, state

    def writeToFile(text, fileName, type=None):
        if(type == "sol"):
            with open("results/" + fileName, 'w') as file:
                if(text[0] == -1):
                    file.write("-1")
                else:
                    file.write(str(text[1]))
                    file.write("\n")
                    solution = ''.join(text[0])
                    file.write(solution)
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