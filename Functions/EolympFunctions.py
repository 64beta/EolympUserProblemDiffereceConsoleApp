import requests
def SolvedProblems(User):
    a = set()
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
