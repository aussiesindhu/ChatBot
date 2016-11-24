from wikipedia import Wikipedia
from wiki2plain import Wiki2Plain
import io
content={}
lang = 'simple'
wiki = Wikipedia(lang)

try:
    raw = wiki.article('Arizona')
except:
    raw = None

if raw:
    wiki2plain = Wiki2Plain(raw)
    content = wiki2plain.text

print content
model_file = io.open("per.txt", "wb")
model_file.write(""+content)
model_file.close()
model_file1 = io.open("per1.txt", "wb")
i=0
with open("per.txt", "r") as f:
    while(i<2):
        line = f.readline()
        if "{" in line or "|" in line or "}" in line:
            print("")
        else:
            i+=1
            model_file1.write(""+line)

model_file1.close()



