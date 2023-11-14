from neural_net_impl import NeuralNet, main
from _xor_ import Neural
import numpy as np

if __name__ == "__main__":

    inputs = np.array([
                       [0,0,1],
                       [0,1,1],
                       [1,0,1],
                       [1,1,1]
                       ])

    output = np.array([[1],[0],[0],[1]])
    net = NeuralNet(10,10,1)
    forward_result = net.forward(inputs)
    print('forward result: \n', forward_result)
    print('w1 matrix')
    for i in net.w1:
        print(i)

    for i in net.b1:
        print(i)


main()
