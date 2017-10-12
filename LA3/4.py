from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk import FreqDist

#file
f=open('read.txt','r')
fr=str(f.read())

#Tokenization
a=sent_tokenize(fr)
b=word_tokenize(fr)
print'Sentence Tokenizaton:\n'
a1=a[0].split('\n')
print(a1)
print'\n-----\n'
print'Word Tokenizaton:\n'
print b

#POS
e=pos_tag(b)
e1=[v for v in e if v[1] != 'VB']
e2=" ".join([v[0] for v in e1])
print'\n-----\n'
print'Parts of Speech:\n'
print(e1)
print'Parts of Speech:\n'
print(e2)

#Lemmatization
print'\n-----\n'
print'Lemmatization:\n'
l=WordNetLemmatizer()
for k in range(len(b)):
    e1 = l.lemmatize(b[k])
    print ("The word \'" + b[k] + "\' in a Lemmatized Version: " + e1)

#Frequency
fd=FreqDist(e2.split(' '))
print'\n-----\n'
print'Word Frequency:\n'
print(list(fd.most_common(1000)))

#Top5
print'\n-----\n'
print'Top 5 words:\n'
top5=list(fd.most_common(5))
top5d=dict(top5)
top5w=top5d.keys()
print(top5w)

#Original
print'\n-----\n'
print'Concatenated Common Sentences:\n'
z1=[]
new=""
def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')
for i in range(2):
    for j in range(4):
        x=contains_word(a1[i], top5w[j])
        if (x==1):
            #print("\n"+a1[i])
            z1.append(a1[i])
            z=set(z1)
            new=' '.join(z)
print(new)