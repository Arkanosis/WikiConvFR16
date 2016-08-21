#! /usr/bin/env python3

import re
import sys
import wikidump

_lang = re.compile(r'=+\s*\{\{langue\|(?P<lang>.+?)\}\}\s*=+')
_synonyms = re.compile(r'=+\s*\{\{S\|synonymes\}\}\s*=+')
_title = re.compile(r'^=+\s*=+')
_word = re.compile(r'^\*\s*\[\[(.+?\|)?(?P<word>.+?)\]\]')

words = set()
relations = set()

def processPage(page):

    if page.ns == 0:

        keepWords = False
        lang = 'fr'

        for line, on, _ in wikidump.matchOnLines(page.text):

            if on(_synonyms):
                keepWords = True
            elif on(_lang):
                lang = _('lang')
            elif on(_title):
                keepWords = False

            if keepWords and lang == 'fr' and on(_word):
                words.add(page.title)
                words.add(_('word'))
                relations.add(tuple(sorted([page.title, _('word')])))

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: {} wikiDump.xml'.format(sys.argv[0].split(os.sep)[-1]))
        sys.exit(1)

    wikidump.parseWithCallback(sys.argv[1], processPage)

    print('words', len(words))
    print('relations', len(relations))
