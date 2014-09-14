from hw1 import Hw1

infilename='review_KcSJUq1kwO8awZRMS6Q49g'
f=open(infilename,'r')
line_num=1
words = []
while(line_num<2):
    line = Hw1.read_line(f.readline())['text']
    words =  Hw1.tokenize(line)
    line_num+=1
print Hw1.stopword(words)

