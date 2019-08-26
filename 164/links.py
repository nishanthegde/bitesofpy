import sys
import re

INTERNAL_LINKS = ('pybit.es', 'codechalleng.es')


def make_html_links():

    link_regex = re.compile(r'^(https?:\/\/[^\s,]+)[,\s]+(.+)')

    if not sys.stdin.isatty():
        for line in sys.stdin:
            # print(type(line.strip()))
            l = line.strip()
            if 'http' not in l.lower() or l.count(',') > 1:
                continue
            else:
                link_href = link_regex.search(l).group(1).strip()
                target = " target=\"_blank\""
                if any(i in link_href for i in INTERNAL_LINKS):
                    target = ""
                link_name = link_regex.search(l).group(2).strip()
                print("<a href=\"{}\"{}>{}</a>".format(link_href, target, link_name))
                # op += l
    else:
        print("just")


def main():
    pass


if __name__ == '__main__':
    make_html_links()
    # main()
