#must be out in desktop to run
import csv

#neural network class definition=has =============================
import numpy
import scipy.special
class NeuralNetwork :
    #initialise the neural network---------------------------------
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        #size-------------------------------------------------
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.hnodes_2 = hiddennodes
        self.onodes = outputnodes
        #weight-----------------------------------------------
        self.wih = (numpy.random.rand(self.hnodes, self.inodes) - 0.5)
        self.who = (numpy.random.rand(self.onodes, self.hnodes) - 0.5)
        self.whh = (numpy.random.rand(self.hnodes, self.hnodes) - 0.5)
        #learning rate------------------------------------------
        self.lr = learningrate
        
        #activation function is the sigmoid function-------------------
        self.activation_function = lambda x:scipy.special.expit(x)
        pass
    

    #train  the neural network-----------------------------------
    def train(self, inputs_list, targets_list):
        
        # convert inputs lists into 2d matrix-------------------------
        inputs = numpy.array(inputs_list, ndmin = 2). T
        targets = numpy.array(targets_list, ndmin = 2). T
        
         
        #calculate signals into hidden layer 1------------------------
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        
        #calculate signals into hidden layer 2------------------------
        hidden2_inputs = numpy.dot(self.whh, hidden_outputs)
        hidden2_outputs = self.activation_function(hidden2_inputs)
        
        #calculate signals into final output layer----------------------
        final_inputs = numpy.dot(self.who, hidden2_outputs)
        final_outputs = self.activation_function(final_inputs)
        
        #error -----------------------------------------------
        output_errors = targets - final_outputs
        
        #hidden layer2 error-------------------------------------
        hidden2_errors = numpy.dot(self.who.T, output_errors)
        #hidden layer2 error-------------------------------------
        hidden_errors = numpy.dot(self.whh.T, hidden2_errors)
       #update weights ----------------------------------------
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden2_outputs))
        self.whh += self.lr * numpy.dot((hidden2_errors * hidden2_outputs * (1.0 - hidden2_outputs)), numpy.transpose(hidden_outputs))
        self.wih  += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
        
        pass
    
    #query the NN===========================================
    def query(self, inputs_list):
        #convert input into 2D array
        inputs = numpy.array(inputs_list, ndmin = 2) .T
        
        #calculate signals into hidden layer 1
        hidden1_inputs = numpy.dot(self.wih, inputs)
        hidden1_outputs = self.activation_function(hidden1_inputs)
        
        #calculate signals into hidden layer 2
        hidden2_inputs = numpy.dot(self.whh, hidden1_outputs)
        hidden2_outputs = self.activation_function(hidden2_inputs)
        
        #calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden2_outputs)
        final_outputs = self.activation_function(final_inputs)
        
        return final_outputs
        
input_nodes = 784
hidden_nodes = 200
output_nodes = 10
learning_rate = 0.1

#a instance of NeuralNetwork 
n = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

#------------------------------------------------train part
#load the mnist training data CSV file into a list
training_data_file = open("mnist_dataset/train.csv",'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

#train the neural network

epochs = 5

for e in range(epochs):
    for record in training_data_list:
        all_values = record.split(',')
        if all_values[0] == 'label' :
            continue
        inputs = ((numpy.asfarray(all_values[1:])/255.0)*0.99)+0.01
        #asarray 将数据转化为ndarray类型（一种多维数组）
        #将图片像素点归一化到0.01-1.00
        targets = numpy.zeros(output_nodes)+0.01
        targets[int(all_values[0])] = 0.99
        #target 是这行代表的数字的标签 第几个输出是1，则为几
        n.train(inputs, targets)
        pass
    pass

#------------------------------------------test part

#load the mnist test data CSV file into a list
test_data_file = open("mnist_dataset/test.csv", 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

def create_csv():
    path = "mnist_dataset/sample_submission.csv"
    with open(path,'w') as f:
        csv_write = csv.writer(f)
        csv_head = ["ImageId","Label"]
        csv_write.writerow(csv_head)

create_csv()


#test the neural network

scordcard = []
i = 1
for record in test_data_list:
    all_values = record.split(',')
    if all_values[0] == 'pixel0':
        continue
    inputs = ((numpy.asfarray(all_values[0:])/255.0 )* 0.99) + 0.01
    outputs = n.query(inputs)
    label = numpy.argmax(outputs)
    writein = [i,label]
    path = 'mnist_dataset/sample_submission.csv'
    with open(path,'a+') as f:
        csv_w = csv.writer(f)
        csv_w.writerow(writein)
    f.close()
    



#calculate the performance score
