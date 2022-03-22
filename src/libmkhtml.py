#!/usr/bin/python3

import os
import json
import markdown
from markdown.extensions.toc import TocExtension

CONFIG = "./mkhtml.json"

class settings():

    def _parse(self, config):
        try:
            with open(config) as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            return None
        except KeyError:
            return None
    
    def get(self, config, param):
        data = self._parse(config)
        
        if data == None:
            return None
        
        try:
            param = data[param]
            return param
        except KeyError:
            return None

class gen():
    
    def get_tags(self, page):
        with open(f"{page}.md") as f:
            data = f.read()
            data = data.split(sep='\n')
            title = data[0][2:]

            header = f"""<!DOCTYPE html>\n<html>\n<head>
            <meta charset="utf-8">
            <link href="css/styles.css" rel="stylesheet" type="text/css">
            <title>{title}</title>
            </head>\n<body>
            """

            footer = "<hr><p>Вернуться на <a href=\"/index.html\">домашнюю страницу</a>.</p>\n<p>Copyright (C) 2022 Michail Krasnov</p>\n</body></html>"
            
        return (header, footer)
    
    def page(self, page):
        if not os.path.isfile(f"{page}.md"):
            raise FileNotFoundError(f"Error: page '{page}' not found!")
        
        with open(f"{page}.md") as f:
            content = f.read()
        
        page_old = page
        readme = False

        if page == "README":
            page = "index"
            readme = True

        with open(f"{page}.html", "w") as f:
            exts = [
                TocExtension(), "fenced_code", "tables",
                "def_list", "footnotes", "codehilite"
            ]
            #exts.append(settings().get(CONFIG, "extensions"))
            
            data = markdown.markdown(content, extensions=exts)
            page = page_old
            tags = self.get_tags(page)

            if not readme:
                data = f"{tags[0]}\n{data}\n{tags[1]}"
            else:
                data = f"{tags[0]}\n{data}"
            
            f.write(data)
