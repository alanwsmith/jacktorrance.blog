#!/usr/bin/env python3

import json

from string import Template


class PageBuilder():

    def __init__(self):
        self.pages_dir = '../site/pages'
        self.home_page = '../site/index.html'
        with open('src/TEMPLATE.html') as _template:
            self.template = Template(_template.read())


    def data(self):
        with open('src/data.js') as _data:
            data = _data.read()
            return data.split("`\n,`")


    def make_pages(self):

        words = """The Autobiography Of Jack Torrance 

             A Novel

        By Jack Torrance"""
        previous_link = '234343'
        next_link = '234343'
        display_num = '234343'
        links = '&nbsp;&nbsp;&nbsp;&nbsp;Cover&nbsp;<a href="/pages/1.html">next</a>'

        with open(self.home_page, 'w') as _out:
            _out.write(
                self.template.substitute({
                    "WORDS": words,
                    "PREVIOUS": previous_link,
                    "NEXT": next_link,
                    "PAGENUM": display_num,
                    "LINKS": links
                })
            )

        for index, words in enumerate(self.data()):
            page_num = index + 1
            previous_num = index
            next_num = page_num + 1
            previous_link = f'''<a href="/pages/{previous_num}.html">prev</a>'''
            next_link = f'''<a href="/pages/{next_num}.html">next</a>'''

            if page_num == 1:
                previous_link = f'''<a href="/">prev</a>'''

            if page_num == 666:
                next_link = f'''&nbsp;&nbsp;&nbsp;&nbsp;'''

            display_num = page_num
            if page_num <= 9:
                display_num = f"&nbsp;&nbsp;{page_num}"
            elif page_num <= 99:
                display_num = f"&nbsp;{page_num}"
                

            links = f"""<a href="/pages/2.html">prev</a>&nbsp;&nbsp;&nbsp;Page&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;<a href="/pages/3.html">next</a>"""

            data = {
                "WORDS": words,
                "PREVIOUS": previous_link,
                "NEXT": next_link,
                "PAGENUM": display_num,
                "LINKS": links

            }
            output_path = f"{self.pages_dir}/{page_num}.html"
            with open(output_path, 'w') as _out:
                _out.write(
                    self.template.substitute(data)
                )




if __name__ == '__main__':
    pb = PageBuilder()
    pb.make_pages()

