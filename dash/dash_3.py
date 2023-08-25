import re
from collections import Counter
import pandas as pd
import numpy as np

def remove_non_ascii(string):
    return string.encode('ascii', errors='ignore').decode()


# print(remove_non_ascii('a€bñcá'))  # 👉️ 'abc'
# print(remove_non_ascii('a_b^0'))  # 👉️ a_b^0


def remove_space(val):
    return [item for item in val if item.strip()]


def check():
    # Sample list with empty strings and spaces
    # asd = {'column_name'['asdderft02_dffdrr03/04   asd']}
    # df = re.sub(' +', ' ', asd).strip()
    # reg = ['\n', 'and', '&', ',']
    # regex_pattern = '|'.join(map(re.escape, reg))
    # match = Counter(re.findall(regex_pattern, df))
    # out = re.sub(regex_pattern, '[^=^]', df)
    # out_ = out.split('[^=^]')
    # dfdf = [len(i) for i in out_]
    # ['asdderft02_dffdrr03 ', ' asd', 'as ', ' asdderft02/rfddffdrr03 asdderft02/03']



    # opt = ['/', '_', '-']
    # condition = lambda x: x < 3
    # for i in out_:
    #     col_pattern = '|'.join(map(re.escape, opt))
    #     match = Counter(re.findall(col_pattern, i))
    #     output = next((key for key, value in match.items() if condition(value)), None)
    #     if output:
    #         sdsd = i.find(output)
    #
    #     print(output)
    # print(match)


    splitter = lambda string, splitter: abs(string.find(splitter) - (len(string) // 2)) <= 1


    # matc = re.findall(r'[^a-zA-Z0-9]', df)
    # ma = list(dict.fromkeys(matc))
    # print(matc)
#

raw = {'column_name': ["1 _  ", "1 _  "], 'b': ["01", "vdom"]}
# raw_2 = {"a": [1, 2, 3], "b": [23, 45, 67]}
df = pd.DataFrame(raw)
# df_1 = pd.DataFrame(raw_2)
# quer = df_1.iloc[0].to_dict()
for i in range(2):
    index = df[df.column_name == "1 _  "].index
    print(index)
    df.drop(index, inplace=True)
    print(df)
# print(quer)
# opee = quer.pop('a')
# print(quer, opee)
import string
def is_special_or_space(x):
    if x[-1] in string.punctuation:
        x = x[:-1]
    if x[0] in string.punctuation:
        x = x[1:]
    return x
# print(is_special_or_space("_j_habsjd"))



# print(index)
# print(df)
# mask = df['column_name'].str.contains(r'^.*[0-9].*$')
# mask = df['column_name'].str.contains(r'^(?=.*[a-zA-Z])(?=.*[0-9]).*$')
# df = df[np.logical_not(mask)]
# print(df.loc[0, 'column_name'])
# hos = df.loc[0, 'column_name'].strip()
# print(hos)
# print(df)
def contains_numbers(string):
    pattern = r'^(?=.*[a-zA-Z])(?=.*[0-9]).*$'
    match = re.match(pattern, string)
    return bool(match)

# print(contains_numbers("as *d "))
# print(contains_numbers("as12_jh*"))
# df = df[df['column_name'].str.isalnum()]
# print(df)
# remover = lambda x:
# df['column_name'].apply(remover)
#
# # df.loc[df['column_name'].str.count('_') == 1, 'column_name'] = df['column_name'].str.replace('_', '[^=^]')
#
# # Replace if string contains exactly one hyphen in midrange in 'column_name'
# df['column_name'] = df['column_name'].str.replace('^([^\-]*)\-([^\-]*)$', r'\1[^=^]\2', regex=True)
#
# # Replace the hyphen with desired character ('X')
# df['column_name'] = df['column_name'].str.replace('|', 'X')
#
# # Restore the hyphen in midrange with the desired character ('X')
# df['column_name'] = df['column_name'].str.replace('|', '-')
#
# # Print the DataFrame after replacement
# print("\nAfter:")
# print(df)
# ada = "asdasd_982789_as"
# re.sub()
