with open("practice2.txt","w") as f:
    f.write("1,2,45,55,76")
    f.close()

with open("practice2.txt","r") as f:
    data=f.read()
    count=0
    """num=""
    for i in range(len(data)):
        if(data[i]==","):
            print(int(num))
            num=""
        else:
            num+=data[i]
    """

    nums=data.split(",")
    for val in nums:
        if(int(val)%2==0):
            count+=1
    print(count)


        


