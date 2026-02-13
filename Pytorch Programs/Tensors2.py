import torch

x = torch.randn(3, requires_grad=True)
print(x)
y = x + 2
print(y)
z = y*y*2
print(z)
# q = z.mean()
# print(q)

# q.backward() #dq/dx   created only for scalar values
# print(x.grad)  #jacobian matrix multiplied with gradient vector we get final gradiance
v = torch.tensor([0.1 , 1.0 , 0.001], dtype = torch.float32)
z.backward(v) #dz/dx   created as we have gradient vector v, works only
print(x.grad)