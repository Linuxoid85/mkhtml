#!/usr/bin/python

import libmkhtml as lmh

CONFIG = lmh.CONFIG
pages = lmh.settings().get(CONFIG, "toc")

for page in pages:
    lmh.gen().page(page)
