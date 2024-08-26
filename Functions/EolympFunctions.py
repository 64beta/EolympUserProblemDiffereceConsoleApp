import requests
from bs4 import BeautifulSoup
from math import ceil

from requests.adapters import HTTPAdapter
from urllib3 import Retry


def Rank(User):

    url = f'https://www.groups.eolymp.com/az/users/{User}'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    xpath_expression = 'body > main > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div > div:nth-child(1) > div > div'
    div_element = soup.select_one(xpath_expression)
    try:
        a = int(div_element.text)
        return a
    except:
        return -1

def UpDownSurroundingRankList(User,rank):

    RankList = []
    p_page = ceil(rank/25) - 1
    while(True):
        url = f'https://www.groups.eolymp.com/az/users/ranking?page={p_page}'
        response = requests.get(url)
        html_ = response.text

        if html_.count(User) == 0:
            p_page+=1
        else:
            soup = BeautifulSoup(response.content, 'html.parser')
            for i in range(25):
                RankList.append(soup.select_one(f'body > main > div:nth-child(2) > div:nth-child(2) > table > tbody > tr:nth-child({i}) > td:nth-child(2) > a'))
            break

    return RankList







def SolvedProblemsz(User):
    a = set()
    url = f'https://groups.eolymp.com/en/users/{User}/punchcard'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',}
    proxies = {'http': 'http://localhost:3128','https': 'http://localhost:1080',}
    #response = requests.get(url, headers=headers)
    response = requests.get(url, headers=headers, proxies=proxies)
    #response = requests.get(url)
    html_ = response.text
    print(html_.count("100%\" href=\"/en/problems/"))
    p = 0
    f = ""
    for i in range(html_.count("100%\" href=\"/en/problems/")):
        p = html_.find("100%\" href=\"/en/problems/", p) + 1
        if f == html_[p + 24:p + 29]:
            continue
        else:
            f = html_[p + 24:p + 29]
            a.add(f)
    return a



import requests

def SolvedProblems(User):
    solved_problems = set()
    url = f'https://groups.eolymp.com/en/users/{User}/punchcard'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    try:
        # Attempt to connect without a proxy
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises HTTPError for bad responses

        html_content = response.text
        print(html_content.count("100%\" href=\"/en/problems/"))

        p = 0
        last_problem_id = ""
        for _ in range(html_content.count("100%\" href=\"/en/problems/")):
            p = html_content.find("100%\" href=\"/en/problems/", p) + 1
            if last_problem_id == html_content[p + 24:p + 29]:
                continue
            else:
                last_problem_id = html_content[p + 24:p + 29]
                solved_problems.add(last_problem_id)

    except requests.exceptions.ProxyError as e:
        print(f"Proxy error: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return solved_problems

