def group_by_owners(files):
    df = list(files.keys())
    val = list(files.values())
    fg = dict()
    for i in list(files.values()):
        if i not in fg.keys():
            fg[i] = [df[val.index(i)]]
            df.pop(val.index(i))
            val.pop(val.index(i))
        elif i in fg.keys():
            fg[i].append(df[val.index(i)])
            df.pop(val.index(i))
    return fg


if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Input1.txt': 'Randy',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))