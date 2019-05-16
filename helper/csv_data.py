#encoding:utf-8
import csv

csvFile = csv.reader(open('../data/train.csv','r',encoding='utf-8'))
print(csvFile)
train = open('../data/kesci/cnews.train.txt', 'w', encoding='utf-8')
test = open('../data/kesci/cnews.test.txt', 'w', encoding='utf-8')
val = open('../data/kesci/cnews.val.txt', 'w', encoding='utf-8')

line = 0
for sentence in csvFile:
    line = line+1
    if len(sentence) < 3:
        print(sentence)
    elif (sentence[2] == 'Positive') or (sentence[2] == 'Negative'):
        content = sentence[2] + "    " + sentence[1];
        content = content.replace('\u3000', '').replace('\n', '') + '\n'
        content = content
        if line <= 5000:
            train.writelines(content)
        else:
            test.writelines(content)
            val.writelines(content)
    else:
        print(sentence)
    # print(sentence)
    #print(sentence[1])

train.close()
test.close()
val.close()