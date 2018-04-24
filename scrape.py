import re
from glob import glob
from bs4 import BeautifulSoup

def soup(f):
    return BeautifulSoup(f, 'html.parser')


if __name__ == "__main__":
    # TODO: course page <a href= contains jump_to
    with open('out/quiz.html', 'w') as out:
        filename = 'in/section_sample.html'
        divs = soup(open(filename, 'r')).findAll('div', {'class': 'seq_contents'})
        for div in divs:
            div_node = soup(div.text)
            problems = div_node.findAll('div', {'class': 'problems-wrapper'})
            if problems:
                tab_header = div_node.find('h2', {'class': 'unit-title'}).text
                for prob in problems:
                    problem = soup(prob['data-content'])
                    problem_body = problem.find('div', {'class': 'wrapper-problem-response'}).prettify()
                    out.write(problem_body)
