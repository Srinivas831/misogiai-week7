# square

# res = lambda x:x**2
# print(res(3))

# fact = lambda x:x* for x in range(x+1,1,-1)
# from functools import reduce
# fact = lambda x: reduce(lambda a,b:a*b, range(x,0,-1))
# print(fact(5))

# res=1
# for i in range(5, 1, -1):
#   res = res*i
# print(res)



# string manupulation

# str = "Hello World"
# res = lambda x:x[::-1]
# print(res("Hello World"))

# def rev(l):
#   bag=""
#   for i in range(len(l)-1,-1,-1):
#     bag+=l[i]
#   return bag
# print(rev("Hello world"))




# List operations

# filter evens
arr = [1,2,3,4,5,6]

# res = list(filter(lambda x:x%2==0,arr))
# print(res)


# sum of list
# from functools import reduce
# res = reduce( lambda a,b:a+b, arr)
# print(res)


words = ["hello", "world", "python"]

upp= [i.upper() for i in words if len(i)>5]
other = [i.upper() if len(i)>5 else i for i in words]
print(other)