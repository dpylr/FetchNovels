#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from urllib.parse import urljoin

from pyquery import PyQuery

from .. import serial, utils

BASE_URL = 'http://www.dzxsw.la/book/{}/index.html'
INTRO_URL = 'http://www.dzxsw.la/book/{}/'


class Dzxsw(serial.SerialNovel):

    def __init__(self, tid):
        super().__init__(utils.base_to_url(BASE_URL, tid), '#content',
                         utils.base_to_url(INTRO_URL, tid), '#cintro',
                         tid=tid)

    def get_title_and_author(self):
        name = self.doc('.title').text()
        pat = re.compile(r'作者：(.+)', re.U)
        st = self.doc('.item').filter(
            lambda i, e: re.match(pat, PyQuery(e).text())
        )
        author = re.match(pat, st.text()).group(1)
        return name, author

    @property
    def chapter_list(self):
        clist = self.doc('.chapterList')('ul').eq(1)('li').filter(
            lambda i, e: PyQuery(e)('a').attr('href')
        ).map(
            lambda i, e: (
                i,
                urljoin(utils.get_base_url(self.url),
                        PyQuery(e)('a').attr('href')),
                PyQuery(e).text()
            )
        )
        return clist
