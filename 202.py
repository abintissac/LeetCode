def split(number):
    split_number=str(number)
    sum_number=0
    for i in split_number:
        sum_number+=int(i)**2
        if sum_number==1:
            return "happy number"
        else:
            split(sum_number)
    print(sum_number)
n=int(input("enter a number"))
split(n)