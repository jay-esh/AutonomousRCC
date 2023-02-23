# Step 1
# Importing the necessary libraries
import numpy as np
# import camera as c
import pickle
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.utils import shuffle


def loadingPxs(datafile, labelfile):
    pickle_inData = open(datafile, "rb")
    pickle_inLabel = open(labelfile, "rb")
    X = []
    y = []
    while True:
        try:
            loadx = pickle.load(pickle_inData)
            X.append(preprocessing.normalize(loadx))
            # print(X)

            loady = pickle.load(pickle_inLabel)
            # preprocessing
            y.append(preprocessing.normalize([loady]))
            # print(y[0])
        except EOFError:
            X, y = shuffle(X, y, random_state=0)
            return X, y


x, y = loadingPxs("dataRight.pickle", "labelsRight.pickle")
# x2, y2 = loadingPxs("dataLeft.pickle", "labelsLeft.pickle")

# X, y = shuffle(X, y, random_state=0)
# Step 3
# Splitting the data into tst and train
# 80 - 20 Split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.20, random_state=4)

# Step 4
# Making the Neural Network Classifier
NN = MLPClassifier(activation='relu', solver='lbfgs',
                   hidden_layer_sizes=(32, 32), random_state=1)
# print(x_train[0].tolist()[0])

# print(y_train[0])

trainx = []
for i in range(len(x_train)):
    lisx = []
    for j in x_train[i].tolist():
        for k in j:
            lisx.append(k)
    trainx.append(lisx)

# print(len(train[0]))
x_train = trainx

trainy = []
for i in range(len(y_train)):
    lisy = []
    for j in y_train[i].tolist():
        for k in j:
            lisy.append(k)
    trainy.append(lisy)

testx = []
for i in range(len(x_test)):
    lisx = []
    for j in x_test[i].tolist():
        for k in j:
            lisx.append(k)
    testx.append(lisx)
y_train = trainy
x_test = testx
# print(y_train)
# Step 5
# Training the model on the training data and labels
NN.fit(x_train, y_train)

pickle_out = open("model.pickle", "ab")
pickle.dump(NN, pickle_out)
pickle_out.close()

# accuracy = accuracy_score(y_test, y_pred)*100
# pred = NN.predict(x_test)
# print(pred)


# while True:
#     try:

#     except EOFError:
#         break

# Step 2
# # Loading the dataset
# dataset = load_digits()

# # Step 3
# # Splitting the data into tst and train
# # 80 - 20 Split
# x_train, x_test, y_train, y_test = train_test_split(
#     dataset.data, dataset.target, test_size=0.20, random_state=4)

# # Step 4
# # Making the Neural Network Classifier
# NN = MLPClassifier()

# # Step 5
# # Training the model on the training data and labels
# NN.fit(x_train, y_train)

# # Step 6
# # Testing the model i.e. predicting the labels of the test data.
# y_pred = NN.predict(x_test)

# # Step 7
# # Evaluating the results of the model
# accuracy = accuracy_score(y_test, y_pred)*100
# confusion_mat = confusion_matrix(y_test, y_pred)

# # Step 8
# # Printing the Results
# print("Accuracy for Neural Network is:", accuracy)
# print("Confusion Matrix")
# print(confusion_mat)


# class NeuralNet:
#     def __init__(self) -> None:
#         pass
