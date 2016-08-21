#! /usr/bin/env python3

import sys
import wikidump

def processPage(page):

    print('=' * 80)
    print(page.ns)
    print(page.title)
    print(page.text)

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: {} wikiDump.xml'.format(sys.argv[0].split(os.sep)[-1]))
        sys.exit(1)

    wikidump.parseWithCallback(sys.argv[1], processPage)
