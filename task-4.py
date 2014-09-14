from hw1 import Hw1

input_file = 'review_KcSJUq1kwO8awZRMS6Q49g'
f = open(input_file, 'r')
line_num = 1
while (line_num < 2 ):
    line = Hw1.read_line(f.readline())['text']
    words = Hw1.stopword(Hw1.tokenize(line))
    line_num +=1
print Hw1.stemming(words)

