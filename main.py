import requests

def funset(User):
    a = {1}
    url = f'https://www.eolymp.com/az/users/{User}/punchcard'
    response = requests.get(url)
    html_ = response.text
    p = 0
    f = ""
    for i in range(html_.count("100%\" href=\"/az/problems/")):
        p = html_.find("100%\" href=\"/az/problems/", p) + 1
        if f == html_[p + 24:p + 29]:
            continue
        else:
            f = html_[p + 24:p + 29]
            a.add(f)
    return a

user = "beta64"
print("diff\nrld")
coreUser = funset(user)
while(True):
    command = input("COMMAND : ")
    if command == "diff":
        a = funset(input("USER : "))

        oop = a.difference(coreUser)

        print(len(oop))
        for i in oop:
            r = ""
            for z in i:
                if z.isalnum():
                    r += z
                else:
                    break

            print("https://www.eolymp.com/az/problems/" + r)
    elif command == "rld":
        coreUser = funset(user)
    elif command == "diff2":
        a = funset(input("Core USER : "))
        b = funset(input("Target USER : "))

        oop = b.difference(a)

        print(len(oop))
        for i in oop:
            r = ""
            for z in i:
                if z.isalnum():
                    r += z
                else:
                    break

            print("https://www.eolymp.com/az/problems/" + r)