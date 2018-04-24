import re
import shlex
import os
import time
import sys
from random import randint
from glob import glob
from bs4 import BeautifulSoup
from subprocess import check_output, CalledProcessError

DEVNULL = open(os.devnull, 'wb', 0)
HTTP_HEADS = open('in/headers').read()


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
    for el in problem_node.findAll('div', {'class': ['equation', 'action', 'notification']}):
        el.decompose()
    # fix images
    for el in problem_node.findAll('img'):
        if el['src'].startswith('//'):
            el['src'] = 'http:' + el['src']


def download_course_sections(course_index_filename):
    dirname = os.path.basename(course_index_filename).replace('.html', '')
    indir = 'in/{}'.format(dirname)
    os.makedirs(indir, exist_ok=True)

    # only need one jump_to link from each li.subsection.accordion
    index = soup(open(course_index_filename))
    downloaded = []
    for li in index.select('li.subsection.accordion'):
        section_link = li.find('a', {'class': 'outline-item'})['href']
        filename = indir + '/' + section_link.split('@')[-1]
        maybe_download(section_link, filename)
        downloaded.append(filename)
    return downloaded


def parse_coures_sections(course_id, section_files):
    with open('out/{}_quiz.html'.format(course_id), 'w') as out:
        for filename in section_files:
            divs = soup(open(filename, 'r')).findAll('div', {'class': 'seq_contents'})
            for div in divs:
                div_node = soup(div.text)
                problems = div_node.findAll('div', {'class': 'problems-wrapper'})
                if problems:
                    tab_header = div_node.find('h2', {'class': 'unit-title'})
                    out.write(str(tab_header))
                    for prob in problems:
                        problem = soup(prob['data-content'])
                        problem_node = problem.find('div', {'class': 'problem'})
                        remove_answer(problem_node)
                        out.write(problem_node.prettify())


def maybe_download(url, outfile):
    if os.path.exists(outfile) and os.stat(outfile).st_size:
        print('{} already exists'.format(outfile))
        return

    try:
        print('Fetching {} into {}'.format(url, outfile))
        curl_cmd = "bash scrape.sh " + url + " " + outfile
        http_code = int(check_output(shlex.split(curl_cmd), stderr=DEVNULL))
        print('Completed with http status {}'.format(http_code))
    except CalledProcessError:
        print(sys.exc_info())
        sleep_sec = randint(1, 10)
        print('Sleep for {} seconds before retry'.format(sleep_sec))
        time.sleep(sleep_sec)
        maybe_download(url, outfile)



if __name__ == "__main__":
    courses = ['MITx+JPAL102x+1T2018', 'MITx+14.740x+1T2018',
               'MITx+14.310x+1T2018', 'MITx+14.73x+1T2018',
               'MITx+14.100x+1T2018']
    for course_id in courses:
        outfile = 'in/index/{}.html'.format(course_id)
        url = 'https://courses.edx.org/courses/course-v1:{}/course/'.format(course_id)
        maybe_download(url, outfile)
        section_files = download_course_sections(outfile)
        parse_coures_sections(course_id, section_files)

