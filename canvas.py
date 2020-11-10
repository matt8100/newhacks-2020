from bs4 import BeautifulSoup as bs
from canvasapi import Canvas

API_URL = "https://q.utoronto.ca/"

# Get length for a PaginatedList object
def pListLen(input):
    len = 0
    for _ in input:
        len += 1
    return len

def retrieveUrls(API_TOKEN):
    canvas = Canvas(API_URL, API_TOKEN)

    # Pages access is determined by the instructor. Ideally, I would be gathering page content from all courses, but the only course I have access to the pages for is my Calc 2 course
    aps163 = canvas.get_course(178707)
    pages = aps163.get_pages()

    pageUrls = []
    bodies = []

    # Get all page URLS
    for i in range(pListLen(pages)):
        pageUrls.append(pages[i].url)

    return pageUrls

def retrieveText(API_TOKEN):
    canvas = Canvas(API_URL, API_TOKEN)

    # Pages access is determined by the instructor. Ideally, I would be gathering page content from all courses, but the only course I have access to the pages for is my Calc 2 course
    aps163 = canvas.get_course(178707)
    pages = aps163.get_pages()

    pageUrls = []
    bodies = []

    # Get all page URLS
    for i in range(pListLen(pages)):
        pageUrls.append(pages[i].url)

    # Get all HTML bodies
    for i in range(len(pageUrls)):
        html = bs(aps163.get_page(pageUrls[i]).body, "html.parser")
        text = html.get_text()
        bodies.append(text)

    return bodies

def search(query, data):
    match = [q for q, i in enumerate(data) if query in i.lower()]
    return match

token = "11834~zlGR3h7CESBJfXA2N0DRBXLxw69IhT1hGpaJzNN8Gkn2boYrFKYAaNhoqhqibaz0"
query = "integration"
# text = retrieveText(token)
# url = retrieveUrls(token)

# results = search(query, text)
print(query)