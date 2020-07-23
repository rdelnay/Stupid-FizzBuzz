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
for i in range(1,16):
    if i% 3== 0 and i%5==0:
        print(c[:4:3]+c[2]*2+c[1::3]+c[2]*2)
    elif i%3==0:
        print(c[:4:3]+c[2]*2)
    elif i%5==0:
        print(c[1::3]+c[2]*2)
    else:
        print(str(i))