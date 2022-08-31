import hashlib
import os


def hshing(file):
    hsh_md = hashlib.sha256()
    with open(file, "rb") as f:
        for chunk in iter(lambda: f.read(), b""):
            hsh_md.update(chunk)
            print(hsh_md.hexdigest())
            return hsh_md.hexdigest()


# c = hshing()
# file = input("Enter File Name: ")
# if os.path.exists(f"/tmp/ilens/tar/{file}.tar.gz"):
    # os.system(f"tar -xvzf /tmp/ilens/tar/{file}.tar.gz -C /tmp/ilens/tar")
    # os.system(f"find . -type f -name '*.txt'")
#     df = hshing(f"/tmp/ilens/tar/{file}/{file}")
#     if df == input("Enter Hash code: "):
#         print("No changes detected")
#         # os.system(f"sh /home/{'$USER'}/Scripts/update_{file}")
#     else:
#         print("changes Detected")
# else:
#     print("please update the file in the directory")
file = input("Enter file path: ")
df = hshing(file)
if df == input("Enter Hash code: "):
    print("No changes detected")
else:
    print("changes_detected")