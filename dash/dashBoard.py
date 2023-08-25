import re

import re


def extract_space_and_special_characters(string):
    # Regular expression pattern to match spaces and special characters
    pattern = r'[-/_\s]'

    # Find all matches of spaces and special characters in the string
    matches = re.findall(pattern, string.strip())

    if len(matches) == 1:
        return "".join(matches)
    else:
        return False

print(extract_space_and_special_characters(" asd / asd "))

# import pandas as pd
#
# # raw_data = {"raw_1": ['abc def', 'a bc', 'abc/123', 'abc-12', 'spe', 'spae']}
# raw_data = {"raw_1": ['as', 'asf', 'sad'], 'raw_2': ['1', '2', '3']}
# df = pd.DataFrame(raw_data)
# # # pattern = r'[^\w\s]|\s'
# # pattern = r'[^A-Za-z0-9\s]|\s'
# # filterdf = df[df['raw_1'].str.contains(pattern, regex=True)]
# #
# # print(df)
# # print(filterdf)
# asd = " ,_,-,/"
# # for i in asd.split(','):
# #     df.loc[df['raw_1'].str.strip().str.count(i) == 1, 'raw_1'] = df['raw_1'].apply(lambda x: x.strip().replace(i, '[^=^]').replace('\\', '\\\\'))
#
# # df['raw_1'] = df['raw_1'].apply(lambda x: [i for i in x if i.strip()])
# # print(df)
#
# index = df.loc[df['raw_1'] == 'asf'].index[0]
# print(index)
# daa = df.loc[index, 'raw_2']
# print(daa)