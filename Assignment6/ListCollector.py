"""
CS3C, Assignment #6, HTML Trees
Gabriel Alon
ListCollector File
When fed an HTML file, creates a Python list
for every ordered or unordered list in the HTML document
"""

from html.parser import HTMLParser


class ListCollector(HTMLParser):
    result = []

    def getLists(self):
        return self.result

    def handle_starttag(self, tag, attrs):
        if tag == 'ul':
            self.new_list = []
            self.relevant_ul = True
        elif tag == 'ol':
            self.new_list = []
            self.relevant_ol = True

    def handle_endtag(self, tag):
        if tag == 'ul':
            self.result.append(self.new_list)
            self.relevant_ul = False

        elif tag == 'ol':
            self.result.append(self.new_list)
            self.relevant_ul = False

    def handle_data(self, data):
        try:
            if self.relevant_ul == True or self.relevant_ol == True:
                self.new_list.append(data)
        except:
            pass
