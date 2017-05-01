##FileName = ("hack.txt")
##access = "w"
##myFile = open(FileName,access)
##myFile.write("w+%d=pass& wasswd \n")
##myFile.write("this is password hacking softwere")
##myFile.close()
##print("HACKED!!!")



##fileName = "hack.txt"
##WRITE = "w"
##APPEND = "a"
##
##live = input("where are you li8ve ") 
##date = input("ENTER your info: ")
##
##File = open(fileName,mode = WRITE)
##File.write(live)
##File.write(date)
##File.close()
##print()





##Filename = open("hack.txt","r")
##firstLine = Filename.readline()
####print(firstLine)
##
##secondLine = Filename.readline()
##print(secondLine)

#===============================================================================================
     #             my small ptoject 1 success
#===============================================================================================
print("what would you like to learn choose below")
print("=========================================")

list = ['learn [kali linux]','learn [linux]' ,'learn [pentasting]','learn [hacking]']
for H in list:
    print(H)
print("---------------------------------------------")

part1 = input("what do you learn: ")
if part1 == "hacking" :
    Filename = open("hack.txt","r")
    WRITE = Filename.read()
    print(WRITE)
    print("---------------------------------------------")
    
elif part1 == "pen" :
    H = open("pen.txt")
    c = H.read()
    print(c)

elif part1 == "linux" :
    H = open("linux.txt")
    c = H.read()
    print(c)
        
elif part1 == "kali" :
    H = open("kali.txt")
    c = H.read()
    print(c)
    
else:
    print("sorry we can't find your choose\n try agian ")



#===============================================================================================
     #             my small ptoject 1 success
#===============================================================================================











