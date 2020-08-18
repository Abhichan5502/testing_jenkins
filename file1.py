file = open ('jenkins.txt' , 'r')
print file.read()
file.close()

file = open ('jenkins.txt' , 'a')
#inp = input('input some chars')
file.write('abcd')
file.close()

file = open ('jenkins.txt' , 'r')
print file.read()
file.close()
