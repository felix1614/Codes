import js2py

# codeInString = 'a = 8\nb=7\nsum=a+b\nprint("sum =",sum)'
# codeObject = compile(codeInString, 'sumstring', 'exec')

# asdas  = "a = 20\nif a % 2 == 0:\n    print('even')\nelse:   ('odd')"
# codeObject = compile(asdas, 'sumstring', 'exec')
# exec(codeObject)

"""JAVASCRIPT TO PYTHON CONVERTOR"""

dfd = "res = 0;\r\nvarrr=[];\r\nfunction test(){" \
      "if ( (-111.94327545166016)<1 ) {\r\n" \
      "    res = (26619.900390625)+(-111.94327545166016)\r\n}\r\n" \
      "else {\r\n    " \
      "res = (25580.751953125)\r\n}\r\n" \
      "varrr.push(res);\r\n" \
      "tag_10027=res\r\n" \
      "if ( tag_10027 < 1 ) {\r\n    " \
      "res = (26619.900390625)\r\n" \
      "}\r\nelse {\r\n" \
      "    res = (-111.94327545166016)\r\n}\r\n" \
      "varrr.push(res);\r\n" \
      "if (  (26619.900390625)<1 ) {\r\n" \
      "    res = (-111.94327545166016)+(26619.900390625)\r\n}\r\n" \
      "else {\r\n    " \
      "res = (25580.751953125)\r\n}\r\n" \
      "varrr.push(res);\r\nreturn varrr\r\n}\r\ntest()"

test = js2py.eval_js(dfd)
print(test)
