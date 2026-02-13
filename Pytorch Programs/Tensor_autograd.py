import torch

weights = torch.ones(4, requires_grad=True)

# for epoch in range(2):
#     # model_output = (weights*3).sum()

#     # model_output.backward()

#     # print(weights.grad)  #Follows iteration, because of next line, it won't change

#     # weights.grad.zero_()    #returns original, also affect the upper mentioned one

#     optimizer = torch.optim.SGD(weights, lr = 0.01)
#     optimizer.step()              #something is wrong in this code, it isn't working
#     optimizer.zero_grad()



weights.grad.zero_()