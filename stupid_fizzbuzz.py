# the regular way...
'''
for i in range(1,101):
    if i% 3== 0 and i%5==0:
        print('fizzbuzz')
    elif i%3==0:
        print('fizz')
    elif i%5==0:
        print('buzz')
    else:
        print(str(i))
'''

# the stupid way
c = 'fbziu'
'''
for i in range(1,16):
    if i%int(str(ord(c[-3]))[0])+int(str(ord(c[-3]))[1])==\
        int(str(ord(c[-5]))[-2]) and i%int(str(ord(c[-2]))[-1])==\
            int(str(ord(c[-5]))[-2]):
        print(c[:4:3]+c[2]*2+c[1::3]+c[2]*2)
    elif i%int(str(ord(c[-3]))[0])+int(str(ord(c[-3]))[1])==\
        int(str(ord(c[-5]))[-2]):
        print(c[:4:3]+c[2]*2)
    elif i%int(str(ord(c[-2]))[-1])==int(str(ord(c[-5]))[-2]):
        print(c[1::3]+c[2]*2)
    else:
        print(str(i))
'''

#the job security way
x = 'lol idk'
for i in range(1,101):
    if i% int(str(ord(x[3]))[0])==int(str(ord(x[-2]))[-1]) and \
        i%int(str(ord(x[-3]))[-1])==int(str(ord(x[-2]))[-1]):
        print(chr(ord(x[5])+2)+x[4]+(chr(ord(x[1])+11)*2)+\
            chr(ord(x[5])-2)+chr(ord(x[1])+6)+(chr(ord(x[1])+11)*2))
    elif i%int(str(ord(x[3]))[0])==int(str(ord(x[-2]))[-1]):
        print(chr(ord(x[5])+2)+x[4]+(chr(ord(x[1])+11)*2))
    elif i%int(str(ord(x[-3]))[-1])==int(str(ord(x[-2]))[-1]):
        print(chr(ord(x[5])-2)+chr(ord(x[1])+6)+(chr(ord(x[1])+11)*2))
    else:
        print(str(i))