import Functions.EolympFunctions
import Profiles.EolympProfiles

def Diff():
        a = Functions.EolympFunctions.SolvedProblems(input("USER : "))

        oop = a.difference(Profiles.EolympProfiles.coreUser)
        Cout(oop)

def Reload():
    Profiles.EolympProfiles.coreUser = Functions.EolympFunctions.SolvedProblems(Profiles.EolympProfiles.user)
    print("reload")
def DiffWithSelectedProfiles():
    a = Functions.EolympFunctions.SolvedProblems(input("Core USER : "))
    b = Functions.EolympFunctions.SolvedProblems(input("Target USER : "))

    oop = b.difference(a)
    Cout(oop)







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