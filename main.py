import Services.services

print("diff\nrld\ndiff2")

while(True):
    command = input("COMMAND : ")
    if command == "diff":
        Services.services.Diff()
    elif command == "rld":
        Services.services.Reload()
    elif command == "diff2":
        Services.services.DiffWithSelectedProfiles()
