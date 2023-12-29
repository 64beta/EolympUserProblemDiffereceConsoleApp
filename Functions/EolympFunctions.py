import requests
from bs4 import BeautifulSoup

def Rank(User):

    url = f'https://www.eolymp.com/az/users/{User}'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    xpath_expression = 'body > main > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div > div:nth-child(1) > div > div'
    div_element = soup.select_one(xpath_expression)
    try:
        a = div_element.text
        return a
    except:
        return ""



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
