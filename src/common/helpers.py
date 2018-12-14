import re

def extract_and_print(string_result):
    print(string_result)
    # part_1, part_2, part_3 = string_result.split('COP')
    # print(part_2)
    price = re.search(r"([$])[.\d] |([$])(.\d) ", string_result)
    symbol, number = price.group().split('$')
    return number