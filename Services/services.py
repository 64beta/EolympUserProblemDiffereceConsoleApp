import Functions.EolympFunctions
import Profiles.EolympProfiles

def Diff():
        a = Functions.EolympFunctions.SolvedProblems(input("USER : "))

        Result = a.difference(Profiles.EolympProfiles.coreUser)
        Cout(Result)

def Reload():
    Profiles.EolympProfiles.coreUser = Functions.EolympFunctions.SolvedProblems(Profiles.EolympProfiles.user)
    print("reload")
def DiffWithSelectedProfiles():
    a = Functions.EolympFunctions.SolvedProblems(input("Core USER : "))
    b = Functions.EolympFunctions.SolvedProblems(input("Target USER : "))

    Result = b.difference(a)
    Cout(Result)
def DiffWithGroupProfiles():
    oop = set()
    while(True):
        a = input("Prompt : ")
        if a == "0":
            break
        else:
            for i in Functions.EolympFunctions.SolvedProblems(a):
                oop.add(i)
    Result = oop.difference(Profiles.EolympProfiles.coreUser)
    Cout(Result)



#for User Interface
def Cout(oop):
    print(len(oop))
    for i in oop:
        r = ""
        for z in i:
            if z.isalnum():
                r += z
            else:
                break

        print("https://www.eolymp.com/az/problems/" + r)