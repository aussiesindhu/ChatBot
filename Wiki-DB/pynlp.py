from pycorenlp import StanfordCoreNLP
import io
import re

#'Tom is a smart boy. He know a lot of thing.'
list=[]
if __name__ == '__main__':
    nlp = StanfordCoreNLP('http://localhost:9000')
    model_file = io.open("per1.txt", "r")
    #text = model_file.read()
    #text=str(text)
    query = ('Tell me some facts about Arizona')
    text1 = ('Arizona is a state in the United States of America and it is considered part of the Southwestern United States and is bordered by New Mexico to the east, Utah to the north, Nevada to the northwest, California to the west, its northeast corner touches part of Colorado, this area is known as the Four Corners. To the south of Arizona is the country Mexico with which it shares a border of 389 miles (626 km). The state is called the "Grand Canyon State" and the "Copper State" as it is the home of the Grand Canyon and has produced large amounts of copper from its mineral deposits.')
    #print text
    #text1 = (
        #'The capital of California is Sacramento. It is the third largest state in size.')

    output = nlp.annotate(text1, properties={
        'annotators': 'tokenize,ssplit,pos,depparse,parse',
        'outputFormat': 'json'
    })
    content = (output['sentences'][0]['parse'])

    output1 = nlp.annotate(query, properties={
        'annotators': 'tokenize,ssplit,pos,depparse,parse',
        'outputFormat': 'json'
    })
    content1 = (output1['sentences'][0]['parse'])

    #print(content)
    model_file = io.open("nlp.txt", "wb")
    model_file.write(" " + content)
    model_file.close()
    with open("nlp.txt", "r") as f:
        for line in f:
            #line = f.readline()
            #if line == " ":
                #break
            if "NNP" in line:
                #print line
                words=line.split()
                for i in words:
                    removeSpecialChars = i.replace("(", "")
                    removeSpecialChars = removeSpecialChars.replace(")", "")
                    list.append(removeSpecialChars)
                #print(list)
                for w,words in enumerate(list):
                    if "NNP" in words:
                        str = list[w+1]
                        #print str
                        break
    #print text
    op=[]
    textnew = text1
    if " It " in text1:
        textnew= text1.replace("It",str)
    if " it." in text1:
        textnew = textnew.replace("it.", str+".")
    if " He " in text1:
        textnew = text1.replace("He", str)
        textnew = textnew.replace("he", str)
    if " She " in text1:
        textnew = text1.replace("She", str)
        textnew = textnew.replace("she", str)
    #print textnew
    newtext=""
    for w in textnew:
        #print w
        if w is not ".":
            newtext = newtext+w
        else:
            op.append(newtext)
            newtext =""
    list1=[]
    #print(op)
    str1 = ""
    for line in content1:
        if "NNP" in line:
            words = line.split()
            for i in words:
                removeSpecialChars = i.replace("(", "")
                removeSpecialChars = removeSpecialChars.replace(")", "")
                list1.append(removeSpecialChars)
            # print(list)

            for w, words in enumerate(list1):
                if "NNP" in words:
                    str1 = list1[w + 1]
                    # print str
                    break
    print str1

    for u in op:
        if "is" in u:
            bestline = u
            break
        #elif str1 in u:
            #bestline = u
            #break
    print("Query: " , ' '.join(query))
    print("Fetched Data from wikipedia: ", ' '.join(text1))
    print("Best Matched answer: " , ' '.join(bestline) )






