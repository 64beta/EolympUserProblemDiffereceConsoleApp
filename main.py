import Services.services

print("diff\nrld\ndiff2\ndiffg")

while(True):
    command = input("COMMAND : ")
    if command == "diff":
        Services.services.Diff()
    elif command == "rld":
        Services.services.Reload()
    elif command == "diff2":
        Services.services.DiffWithSelectedProfiles()
    elif command == "diffg":
        Services.services.DiffWithGroupProfiles()

