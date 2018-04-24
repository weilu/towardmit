import re
from glob import glob
from bs4 import BeautifulSoup

def soup(f):
    return BeautifulSoup(f, 'html.parser')


def remove_answer(problem_node):
    for correct in problem_node.findAll('span', {'class': 'sr'}):
        correct.decompose()
    for text_answer in problem_node.findAll('input', {'type': 'text'}):
        del text_answer['value']
    for select_answer in problem_node.findAll('input', {'type': ['checkbox', 'radio']}):
        del select_answer['checked']
    # remove noise
    for el in problem_node.findAll('div', {'class': 'equation'}):
        el.decompose()


if __name__ == "__main__":
    # TODO: course page <a href= contains jump_to
    # TODO: handle equations & images
    with open('out/quiz.html', 'w') as out:
        for filename in glob('in/*.html'):
            divs = soup(open(filename, 'r')).findAll('div', {'class': 'seq_contents'})
            for div in divs:
                div_node = soup(div.text)
                problems = div_node.findAll('div', {'class': 'problems-wrapper'})
                if problems:
                    tab_header = div_node.find('h2', {'class': 'unit-title'}).text
                    for prob in problems:
                        problem = soup(prob['data-content'])
                        problem_node = problem.find('div', {'class': 'wrapper-problem-response'})
                        remove_answer(problem_node)
                        out.write(problem_node.prettify())
