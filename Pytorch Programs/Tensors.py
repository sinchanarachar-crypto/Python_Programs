import torch
import numpy as np

# # # x = torch.empty(3)
# # # print(x)

# # x=torch.ones(2,3)
# # print(x.dtype)

# a = torch.rand(2,2)
# b = torch.rand(2,2)
# c = torch.add(a,b)     #c = torch.sub(a,b) for subtraction  c = torch.mul(a,b) for multiplication   c= torch.div(a,b) for division
# print(c)

# #--- trailing underscore will do operation at particular time itself

# b.add_(a)  #same as we did for 'c' above
# print(b)   b.sub_(a) for subtraction b.mul_(a) for multiplication   b.div_(a) for division

# x = torch.rand(5,3)
# print(x)         #slicing
# print(x[:,0])    #prints 0th column of all rows in row form(horizontal)
# print(x[1,1])    #gives tensor at that point
# print(x[1,1].item())  #return item at that point

# x = torch.rand(4,4)
# y = x.view(16)     #reshaping tensor   y = x.view(-1,8) it's size will be 2 x 8
# print(x)
# print(y)

# a = torch.ones(5)
# b = a.numpy()
# print(b , type(b))  #tensor to numpy

# a.add_(1)
# print(a , b)  #everything is stored in cpu with same memory allocation , so even b value will be changed eventhough we didn't do it manually

# if torch.cuda.is_available():
#     device = torch.device("cuda")
#     x = torch.ones(3, device = device)
#     y = torch.ones(5)
#     y = y.to(device)    #works if cuda toolkit is there along with GPU
#     z = x + y               #numpy works only on CPU tensors, not on GPU tensors
#     print(z)

x = torch.ones(5, requires_grad= True)  #This tells that later gradience need to be found in  upcoming calculations when mentioned
print(x)

