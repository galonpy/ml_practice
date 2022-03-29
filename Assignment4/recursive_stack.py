"""
Program Stack where recursion depth n =3

line 29
row 3 [1, 3, 3, 1]
line 29
row 2 [1, 2, 1]
line 29
row 1 [1, 1]
line 29
row 0 [1]

ALSO like the blue boxes in the example:

n==3
result = (self.pascal(n-1))
...
data = [1]
for i in range(1,n):
    data.append(result[i - 1] + result[i])
data.append(1)
print(f"row {self.row_num} {data}")
self.row_num+=1
return data
        result = (self.pascal(2))

n==2
result = (self.pascal(n-1))
...
data = [1]
for i in range(1,n):
    data.append(result[i - 1] + result[i])
data.append(1)
print(f"row {self.row_num} {data}")
self.row_num+=1
return data
        result = (self.pascal(1))



n == 1
result = (self.pascal(n))
...
data = [1,1]
print(f"row {self.row_num} {data}")
self.row_num+=1
return data
        self.pascal(0)


n ==0:
result = (self.pascal(n))
...
data = [1]
print(f"row {self.row_num} {data}")
self.row_num+=1
return data
        result = (self.pascal(0))


"""