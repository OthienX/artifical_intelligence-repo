def fuzzbuss(input):
    if input  %3==0:
        return 'fuzz'
    if input %5 == 0:
        return 'buss'
    if input %15 ==0:
        return 'fuzzbuss'
print(fuzzbuss(5))



