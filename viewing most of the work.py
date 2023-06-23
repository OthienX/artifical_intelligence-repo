#x , y , z = 'banana', 'cherry', 'orange'
#print(x)
#print(y)
#print(z)

def myfunction():
    global x
    x = "fantastic"
    #print('python is'+x)
    myfunction()
#print('python is' + x)
for i in 'banana':
    print(i)
