import re
text="He11o w0rld 123!"
result=re.sub(r'\d','',text)
print(result)
