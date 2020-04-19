n = int(input())
def Bam(n):
    if n == 0:
        return 1
    return Bam(n-1)*n
print(Bam(n))