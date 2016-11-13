#!/usr/bin/env python3
# Adpated from a code taken from @dorianpula 
# Markdown documentation with Sphinx <http://dorianpula.ca/2015/09/02/markdown-documentation-with-sphinx/>

import io
import os
from docutils import core as docutils_core

path_info = os.environ.get('PATH_INFO', '')[1:]
if path_info:
    with io.open(path_info) as src:
        beta = src.read()
        html = docutils_core.publish_string(beta, writer_name='html')
        print('Content-Type: text/html')
        print()
        print(html.decode('utf-8'))
