s="1111011110000011100000110001011011110010111001010111110001"
nums=int(s,2)
n=0
while nums!=1:
    if nums%2==0:
        nums=nums/2
        n+=1
    else:
        nums+=1
        n+=1
print(n)