import torch

# #creating an empty tensor
# t1 = torch.empty(3)

import torch.nn as nn

# a = torch.ones(5,5)
# print(a)

# sum = torch.sum(a, axis = 1)
# print(sum)

a = torch.ones([5,2])
squeezed = torch.squeeze(a)
unsqueezed = torch.unsqueeze(a, dim = 1)
print(unsqueezed)
print(squeezed)