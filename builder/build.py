#!/usr/bin/env python3

import json

from string import Template


class PageBuilder():

    def __init__(self):
        self.pages_dir = '../site/pages'
        with open('src/TEMPLATE.html') as _template:
            self.template = Template(_template.read())


    def data(self):
        with open('src/data.js') as _data:
            data = _data.read()
            return data.split("`\n,`")


    def make_pages(self):
        for index, words in enumerate(self.data()):
            data = {"WORDS": words}
            page_num = index + 1
            output_path = f"{self.pages_dir}/{page_num}.html"
            with open(output_path, 'w') as _out:
                _out.write(
                    self.template.substitute(data)
                )


if __name__ == '__main__':
    pb = PageBuilder()
    pb.make_pages()

