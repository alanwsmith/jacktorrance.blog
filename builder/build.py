#!/usr/bin/env python3

import glob
import json
import os
import sys

from string import Template

script_dir = sys.path[0]
source_dir = os.path.abspath(os.path.join(script_dir, '..', 'scripts', 'page_makers', 'output'))

class PageBuilder():

    def __init__(self):
        self.pages_dir = '../site/pages'
        self.home_page = '../site/index.html'
        with open('src/TEMPLATE.html') as _template:
            self.template = Template(_template.read())

    def data(self):
        payload = []

        for i in range(0, 123):
            file_list = [
                file for file in glob.glob(f"{source_dir}/{i}-*")
            ]

            file_list.sort()

            for file in file_list:
                with open(file) as _in:
                    payload.append(_in.read())

        return payload


    def make_pages(self):

        words = """The Autobiography Of Jack Torrance 

             A Novel

        By Jack Torrance"""
        previous_link = '234343'
        next_link = '234343'
        display_num = '234343'
        links = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Cover&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/pages/1.html">next</a>'
        random = '<button id="randomButton">hint: the arrow keys work</button>'
        cover = "cover page"
        next_num = 1

        prefetch = '<link rel="prefetch" href="/pages/1.html" />'

        with open(self.home_page, 'w') as _out:
            _out.write(
                self.template.substitute({
                    "WORDS": words,
                    "PREVIOUS": previous_link,
                    "NEXT": next_link,
                    "PAGENUM": display_num,
                    "LINKS": links,
                    "RANDOM": random,
                    "COVER": cover,
                    "PREV_NUM": 0,
                    "NEXT_NUM": next_num,
                    "PREFETCH": prefetch,

                })
            )

        for index, words in enumerate(self.data()):
            print(index)

            # get report data
            lines = words.split("\n")
            line_count = len(lines)

            max_length = 0
            for line in lines:
                character_count = len(line)
                max_length = max(max_length, character_count)

            page_num = index + 1
            previous_num = index
            next_num = page_num + 1
            previous_link = f'''<a href="/pages/{previous_num}.html">prev</a>'''
            next_link = f'''<a href="/pages/{next_num}.html">next</a>'''
            random = '<button id="randomButton">Random Page</button>'
            cover = '<a href="/">cover page</a>'

            prefetch = f'''<link rel="prefetch" href="/pages/{previous_num}.html" />
            <link rel="prefetch" href="/pages/{next_num}.html" />
            '''


            if page_num == 1:
                previous_link = f'''<a href="/">prev</a>'''
                prefetch = '<link rel="prefetch" href="/pages/2.html" />'

            if page_num == 666:
                next_link = f'''&nbsp;&nbsp;&nbsp;&nbsp;'''
                prefetch = '<link rel="prefetch" href="/pages/665.html" />'

            display_num = page_num
            if page_num <= 9:
                display_num = f"&nbsp;&nbsp;{page_num}"
            elif page_num <= 99:
                display_num = f"&nbsp;{page_num}"
                
            links = f"""{previous_link}&nbsp;&nbsp;&nbsp;Page&nbsp;{display_num}&nbsp;&nbsp;&nbsp;{next_link}"""

            data = {
                "WORDS": words,
                "PREVIOUS": previous_link,
                "NEXT": next_link,
                "PAGENUM": display_num,
                "LINKS": links,
                "RANDOM": random,
                "COVER": cover,
                "PREV_NUM": previous_num,
                "NEXT_NUM": next_num,
                "PREFETCH": prefetch,

            }
            output_path = f"{self.pages_dir}/{page_num}.html"
            with open(output_path, 'w') as _out:
                _out.write(
                    self.template.substitute(data)
                )


if __name__ == '__main__':
    import datetime
    print("Building:" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    pb = PageBuilder()
    pb.make_pages()

