#------ Libraries ------#
import random,os,sys
from activation_functions import unitStep
import numpy as np

#:Command-Line-Method {{{
def command_line():
    """
    """
    args = sys.argv
    args.pop(0) #removing the module name in the arguments.
    _type = None
    info = []
    try:
        if 'train' in args:
            info.append(True)
            args.remove('train')

        if 'or' in args:
            _type = 'or'
        elif 'and' in args:
            _type = 'and'
        elif 'info' in args:
            print()
        else:
            print('[!] Gate "%s" not implemented yet.'%args[0])
            print('You can choose: "or", "and"')
        info.append(_type)

        return info
    except:
        print('Usage: perceptron.py [-neuron type <"or","and">] [-training <"train">] [-info <"info">]')
        exit()
        }}}

#------ Class implementation -----#
class Perceptron(object):
    """
    @Public class: Perceptron.
    @Attributes:
        -
    """
    def __init__(self, info):
        """
        """
        if True in info:
            self.training()
            info.remove(True)

        self.neuron_type = info.pop()
        print('Neuron type: %s'%self.neuron_type)

    def start(self):
        """
        """
        if self.neuron_type:

            file = open("weights.txt","r")
            weights_file = file.read()
            file.close()
            weights = []

            for weight in weights_file.split("\n"):
                weights.append(float(weight))

            x1 = int(input("In_1: "))
            x2 = int(input("In_2: "))

            _sum = x1 * weights[0] + x2 * weights[1] + weights[2]
            out = unitStep(_sum)

            print("{}, {} = {}".format(x1,x2,out))

    def training(self):
        DATA   = np.array([[0,0,0],[0,1,1],[1,0,1],[1,1,1]])
        WEIGHT = np.array([random.random()*10, random.random()*10, random.random()*10])
        LEARN = True
        OUT = 2.50
        EPOCH = 0
        FILE = open("weights.txt", "w")

        while LEARN:
            LEARN = False
            EPOCH += 1
            print(" Training: ", EPOCH, " weight -----> ", WEIGHT)

            for i in range(len(DATA)):

                #Neuron
                _sum = DATA[i][0] * WEIGHT[0] + DATA[i][1] * WEIGHT[1] + WEIGHT[2]

                #Activation Step Function 
                out = unitStep(_sum)
                if out != DATA[i][2]:

                    WEIGHT[0] = random.random() * 10 - random.random() * 10
                    WEIGHT[1] = random.random() * 10 - random.random() * 10
                    WEIGHT[2] = random.random() * 10 - random.random() * 10
                    LEARN = True
        ######## Weight Save ##########
        FILE.write(str(WEIGHT[0]) + "\n" + str(WEIGHT[1]) + "\n" + str(WEIGHT[2]))
        FILE.close()
        print("\n")

if __name__ == '__main__':
    user_input = command_line() # if the user use the script through a command line
    neuron = Perceptron(info=user_input)
    neuron.start()

