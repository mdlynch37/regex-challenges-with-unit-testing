import re


def is_valid_credit_card_num(cc_num): # difficulty-level: medium

    cc_num = re.sub(r'^(\d{4})-(\d{4})-(\d{4})-(\d{4})$',
                    r'\1\2\3\4', cc_num)  # strip valid dashes

    if re.search(r'(?=[4-6])^(?:([0-9])(?!\1{3})){16}$', cc_num):
        return 'Valid'
    else:
        return 'Invalid'


cc_nums = []
n = int(input())
for _ in range(n):
    print(is_valid_credit_card_num(input()))
