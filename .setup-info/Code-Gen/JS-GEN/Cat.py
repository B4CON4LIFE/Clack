myfile = open("gen\\filenames.txt", "r")
myline = myfile.readline()
repoHost = "gba-host"
gameType = "gba-alt"
while myline:
    print(myline)
    myline = myfile.readline()
    myline1 = myline.replace("\n", "',")
    with open("gen\gen.txt", "a") as f:
        f.write(f"'../{repoHost}/{gameType}/{myline1}\n")