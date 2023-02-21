#pop out two celeb 
#count out the remaining
musicians = []
n = int(input("enter the number of names required"))
for i in range (0,n):
    elem=str(input("enter the names of musicians:"))
    musicians.append(elem)
print("the created list of names",musicians)
celebs=musicians.copy()
print(celebs)
celebs.sort()
print(celebs)
celebs.pop()
print(celebs)