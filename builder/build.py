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
        links = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Cover&nbsp;&nbsp;&nbsp;&nbsp;<a href="/pages/1.html">next</a>'
        random = '<button id="randomButton">&nbsp;</button>'
        cover = "cover page"

        with open(self.home_page, 'w') as _out:
            _out.write(
                self.template.substitute({
                    "WORDS": words,
                    "PREVIOUS": previous_link,
                    "NEXT": next_link,
                    "PAGENUM": display_num,
                    "LINKS": links,
                    "RANDOM": random,
                    "COVER": cover
                })
            )

        for index, words in enumerate(self.data()):

            # Max lines is 16

            # get report data
            lines = words.split("\n")
            line_count = len(lines)

            # if line_count > 13:
            #     print(f"{index} - {line_count}")

            max_length = 0
            for line in lines:
                character_count = len(line)
                max_length = max(max_length, character_count)

            if max_length > 58:
                print(f"{index} - {max_length}")



            page_num = index + 1
            previous_num = index
            next_num = page_num + 1
            previous_link = f'''<a href="/pages/{previous_num}.html">prev</a>'''
            next_link = f'''<a href="/pages/{next_num}.html">next</a>'''
            random = '<button id="randomButton">Random Page</button>'
            cover = '<a href="/">cover page</a>'


            if page_num == 1:
                previous_link = f'''<a href="/">prev</a>'''

            if page_num == 666:
                next_link = f'''&nbsp;&nbsp;&nbsp;&nbsp;'''

            display_num = page_num
            if page_num <= 9:
                display_num = f"&nbsp;&nbsp;{page_num}"
            elif page_num <= 99:
                display_num = f"&nbsp;{page_num}"
                

            links = f"""{previous_link}&nbsp;&nbsp;&nbsp;Page{display_num}&nbsp;&nbsp;&nbsp;{next_link}"""

            data = {
                "WORDS": words,
                "PREVIOUS": previous_link,
                "NEXT": next_link,
                "PAGENUM": display_num,
                "LINKS": links,
                "RANDOM": random,
                "COVER": cover,

            }
            output_path = f"{self.pages_dir}/{page_num}.html"
            with open(output_path, 'w') as _out:
                _out.write(
                    self.template.substitute(data)
                )




if __name__ == '__main__':
    pb = PageBuilder()
    pb.make_pages()

