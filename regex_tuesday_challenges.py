import re

# TODO: Optimize with atomic grouping and possessive quantifiers
def highlight_repeat_words(text):  # Challenge: Week 1
    """
    Finds and highlights repeated words in a body of text by wrapping the
    all but the first repeated word(s) in a <strong> element.
    For example, 'this is is a test' should return
    'this is <strong>is</strong> a test'.

    :param string: any text
    :return: transformed text
    """

    return re.sub(r'\b(\S+) (\1)\b', r'\1 <strong>\2</strong>',
                  text, flags=re.IGNORECASE)


def match_css_grayscale(text):  # Challenge: Week 2
    """
    Matches valid css colors that are grayscale,
    i.e. its red, green and blue values are equal (for rgb). Accepts formats:
    hex (3 or 6 digits), rgb, rgba, hsl, hsla.

    for hsl being grayscale:
        if h=0, s must == 100% or 0%
        else l or s must == 0%

    :param string: any text
    :return: match obj if grayscale color, None otherwise
    """

    grayscale_re = re.fullmatch(r"""
            [#](?P<hex>[0-9a-f]{1,2})(?P=hex){2}|  # hex

            (?:(?P<rgb>rgb)|(?P<hsl>hsl))(?P<a>a)?[(][ ]*0*  # rgb(a) or hsl(s)
            (?(rgb)
                (?P<r>(?:(?:(?:\d|\d{2}|  # capture valid r value
                         1\d{2}|2[0-4]\d|
                         25[0-4])(?:[.]\d+)?)|255) |
                (?:(?:(?:\d|\d{2})(?:[.]\d*)?)|100)%)
                [ ]*,[ ]*0*(?P=r)[ ]*,[ ]*0*(?P=r))  # check same g, b
            (?(hsl)
                (?:(?:0[ ]*,[ ]*0*   # if h==0, s must == 100% or 0%
                     (?:(?:(?:\d|\d{2})(?:[.]\d*)?)|100)%
                     [ ]*,[ ]*0*(?:100|0)(?:[.]0*)?%) |
                (?:(?:(?:(?:\d{1,2}|[1-2]\d{2}|  # else l or s must == 0%
                          3[0-5]\d)(?:[.]\d*)?)|360)[ ]*,[ ]*0*
                   (?:(?:(?:(?:(?:\d|\d{2})([.]\d*)?)|100)%
                       [ ]*,[ ]*0(?:[.]0*)?%) |
                   (?:0(?:[.]0*)?%[ ]*,[ ]*0*
                       (?:(?:(?:\d|\d{2})(?:[.]\d*)?)|100)%)
                   )
                )
            ))
            (?(a)[ ]*,[ ]*\d+(?:[.]\d+)?%?)[ ]*[)]  # check a if necessary
            """, text, re.VERBOSE|re.IGNORECASE)

    return grayscale_re


def match_valid_date(text): # Challenge: Week 3
    """
    Matches valid dates of format: YYYY/MM/DD HH:MM(:SS),
    where year is between 1000 and 2012, and all months are
    regarded as having 30 days.

    :param string: any text
    :return: match obj if valid date, None otherwise
    """

    date_re = re.fullmatch(r"""
            (1\d{3}|200\d|20[1][0-2])/           # YYYY
            (0[1-9]|1[0-2])/                     # MM
            (0[1-9]|[1-2]\d|30)[ ]               # DD
            ([0-1]\d|2[0-3]):[0-5]\d(:[0-5]\d)?  # HH:MM(:SS)
            """, text, re.VERBOSE)

    return date_re

def md_italics_to_html(text): # Challenge: Week 4
    """
    This simple markdown parser replaces valid instances of italicized text
    with their html representation, ignore bold text in the markdown.

    For example, '*this is italic*' should return
    '<em>this is italic</em>'.

    :param string: any text
    :return: transformed text
    """

    return re.sub(r'(?<![*])[*]((?:[^*]|[*]{2})+)[*](?![*])',
                  r'<em>\1</em>', text)


def match_valid_nums(text): # Challenge: Week 5
    """
    Matches correctly formatted numbers, incl. those with thousands separators
    and decimal places. It is compatible with both main number syntaxes,
    e.g. 10,000,000.45 and 10 000 000,45.
    It should not match invalid numbers such as 123.456.789.

    :param string: any text
    :return: match obj if valid number, None otherwise
    """

    valid_num_re = re.fullmatch(r"""
            \d{1,3}(,\d{3})*([.]\d+)?|
            \d{1,3}([ ]\d{3})*(,\d+)?
            """, text, re.VERBOSE)

    return valid_num_re

def match_valid_ipv4(text): # Challenge: Week 6
    """
    Matches valid IPv4 addresses in varous formats (dotted decimal,
    dotted hexadecimal, dotted octal, hexadecimal, decimal and octal).

    Non-dotted octal has max value: (0)37777777777
    Non-dotted int has max value: 4294967295

    :param string: any text
    :return: match obj if valid IPv4, None otherwise
    """

    valid_ipv4_re = re.fullmatch(r"""
            (0x[0-9a-f]{2}|0[0-3][0-7]{2}|  # dotted hex and octal
                (255|25[0-4]|2[0-4]\d|1\d{2}|\d{2}|\d))  # dotted decimal
                ([.](0x[0-9a-f]{2}|0[0-3][0-7]{2}|       # repeat with .
                (255|25[0-4]|2[0-4]\d|1\d{2}|\d{2}|\d))){3}|
            0x[0-9a-f]{8}|     # non-dotted hex
                0?([0-7]{11}|[0-2][0-7]{10}|3[0-7]{10})|  # non-dotted octal
                ([0-3]?\d{9}|  # non-dotted decimal
                ([0-3]\d{9}|4[0-1]\d{8}|42[0-8]\d{7}|429[0-3]\d{6}|
                    4294[0-8]\d{5}|42949[0-5]\d{4}|429496[0-6]\d{3}|
                    4294967[0-1]|d{2}|42949672[0-8]\d|429496729[0-5]))
            """, text, re.VERBOSE|re.IGNORECASE)

    return valid_ipv4_re

def match_valid_domain(text):  # Challenge: Week 7
    """
    Match valid domain names with protocols (http and https) in front of them
    and an optional slash (/) behind them.

    :param string: any text
    :return: match obj if valid domain, None otherwise
    """

    valid_domain = re.fullmatch(r"""
            https?://(?![0-9a-z.-]{254,})(  # max len of domain name is 253
            ((?![0-9a-z-]{64,})(            # max of each label is 63
            [0-9a-z]+(-[0-9a-z]+)*[.]))+
            [a-z]{1,63}/?)
            """, text, re.VERBOSE|re.IGNORECASE)

    return valid_domain

def highlight_repeat_list_items(text):  # Challenge: Week 8
    """
    Finds repeated items in a markdown list and highlights all but the first.

    Example input:
    * Repeated list item
    * Repeated list item
    Example output:
    * Repeated list item
    * **Repeated list item**

    :param string: any text
    :return: transformed text
    """

    return re.sub(r'([*][ ]+(\w.+)\n[*][ ]+)(\2(?=\n|$))', r'\1**\3**',
                  text, flags=re.IGNORECASE)

def md_links_to_html(text):  # Challenge: Week 9
    """
    Parse markdown links into html links.

    Example input:
    [text](http://example.com)
    Example output:
    <a href="http://example.com">text</a>

    :param string: any text
    :return: transformed text
    """

    return re.sub(r"""
            (?<!\S|!)[[]([^\[\]]+)[]][(](
            https?://(?![0-9a-z.-]{254,})(  # max len of domain name is 253
            ((?![0-9a-z-]{64,})(            # max of each label is 63
            [0-9a-z]+(-[0-9a-z]+)*[.]))+
            [a-z]{1,63}/?))[)](?!\S)
            """, r'<a href="\2">\1</a>', text, flags=re.IGNORECASE|re.VERBOSE)

def tokenize_text(text):  # Challenge: Week 10
    """
    Converts text to a comma-separated list of its component words.

    Criteria is as follows:
    - quoted text should be treated as a single token
    - compound words joined by a single hyphen are treated as a single token
    - all other hyphen occurrences should be stripped
    - contractions like "can't" should be treated as a single token
    - in all other instances, punctuation should be stripped

    Example input:
    don't tell Suzie Smith-Hopper that I broke Daniel's toy horse
    Example output:
    don't,tell,Suzie,Smith-Hopper,that,I,broke,Daniel's,toy,horse

    :param string: any text
    :return: transformed text
    """

    tokens = re.sub(r"""
                (;[ ]|[ ]|-{2,}|^)
                ((['\"](?P<quoted>[a-z]+([- ][a-z]+)*)['\"])|
                ('?(?P<single>[a-z]+([-'][a-z]+)*))'?)
            """, r'\g<single>\g<quoted>,',  # will only replace with one group
                    text, flags=re.IGNORECASE|re.VERBOSE)

    return tokens[:-1]  # remove last separator


def match_alpha_ascending(text):  # Challenge: Week 11
    """
    Match if letters are in alphabetic order, ignoring whitespace

    :param string: any text
    :return: match obj if in alphabetic order, None otherwise
    """

    valid_domain = re.fullmatch(r"""
            a?[ ]*b?[ ]*c?[ ]*d?[ ]*e?[ ]*f?[ ]*g?[ ]*h?[ ]*i?[ ]*
            j?[ ]*k?[ ]*l?[ ]*m?[ ]*n?[ ]*o?[ ]*p?[ ]*q?[ ]*r?[ ]*
            s?[ ]*t?[ ]*u?[ ]*v?[ ]*w?[ ]*x?[ ]*y?[ ]*z?
            """, text, re.VERBOSE|re.IGNORECASE)

    return valid_domain

def fix_whitespace(text):  # Challenge: Week 12
    """
    Replaces whitespace, except newlines, with a single space between words
    and a double space between sentences.

    Example input:
    Multiple	tabs	here. Multiple	tabs	here
    Example output:
    Multiple tabs here. Multiple tabs here

    :param string: any text
    :return: transformed text
    """

    fixed = re.sub(r"""
            (([a-z]+|\d+([.]\d*)*)(\.[ ]|\.$)?)[ \t\r\f\v]*
            """, r'\1 ', text, flags=re.IGNORECASE|re.VERBOSE)

    return fixed[:-1]  # remove last space


def match_elements_50_or_less(text):  # Challenge: Week 14
    """
    Match if input is a valid short name for elements on the period table
    with an amotic number of 50 or less.

    :param string: any text
    :return: match obj if valid element, None otherwise
    """

    elem_match = re.fullmatch(r"""
            A[grs]|B[e,r]?|C[adloru]?|Fe?|
            G[ae]|He?|In|Kr?|Li|M[gno]|
            N[abei]?|O|Pd?|R[bhu]|S[ceinr]?|
            T[ic]|V|Y|Z[n,r]
            """, text, re.VERBOSE)

    return elem_match




