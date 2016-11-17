import re


def detect_html_tags(html_input):
    tags = re.findall(r'< *(\w+)(?: */?>| [a-z]+=)', html_input)
    tags = list(set(tags))

    return ';'.join(sorted(tags))


html_fragments = []
n = int(input())
for _ in range(n):
    html_fragments += [input()]

print(detect_html_tags(''.join(html_fragments)))
