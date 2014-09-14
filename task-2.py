from hw1 import Hw1

infilename='review_KcSJUq1kwO8awZRMS6Q49g'
f=open(infilename,'r')
line_num=1
while(line_num<3):
    line = Hw1.read_line(f.readline())['text']
    print "Original: %s" %line
    print Hw1.tokenize(line)
    line_num+=1

