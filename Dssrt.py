import tkFileDialog
import re
file_path = tkFileDialog.askopenfilename()

print(file_path)


input_file = open(file_path)
lower_file = input_file.read().lower()
splitted = lower_file.split()
#without_pun = "".join(c for c in lower_file if c not in ('!',',',"'",'"','?','.',':','!','@','#','$','%','^','&','*','(',')','_','+','=''`','~'))
without_pun = re.sub('[^a-z\ \']+', " ", lower_file)
text = list(without_pun.split())

test1 = raw_input('Please enter the first word : ')
test2 = raw_input('Please enter second word : ')
word_A = 0
situation = 0
together = 0
for word in text:
        situation = situation + 1
        if (test1 == word):
            word_A = word_A + 1
            for n in range(1,6):
                try:
                  if(test2 == text[situation +n]):
                    together = together +1
                except IndexError:
                    1+1
                try:
                    if (test2 == text[situation - n]):
                        together = together + 1         
                except IndexError:
                    1+1
if word_A != 0:
    print("The Co-occurance ratio is : " + str(round(1.0*together/word_A,2)))
else:
    print("The Co-occurance ratio is 0.00")
