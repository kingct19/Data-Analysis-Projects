#Task3
#Chandler King
#50260521

import numpy as np
from sklearn import datasets

digits = datasets.load_digits()

sample_index = int(input("Please enter the last two digits of your school ID: "))
sample_image = digits.data[sample_index]
sample_value = digits.target[sample_index]

print("Two-dimensional array representing sample image:")
print(sample_image)

print("Numeric value of digit the image represents:")
print(sample_value)

import matplotlib.pyplot as plt

plt.imshow(np.reshape(sample_image, (8, 8)), cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(digits.data,digits.target, random_state=11, test_size=(sample_index%10)/100)


print("Number of training examples:", len(X_train))
print("Number of testing examples:", len(X_test))

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=6)

knn.fit(X_train,y_train)

predicted = knn.predict(X_test)

score = knn.score(X_test, y_test)

print('Accuracy score: ', score)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test,predicted)

row = sample_index % 10
print('The {}th row of the confusion matrix represents the actual values of the digits that have been predicted incorrectly.'.format(row))

print('The {}th row of the confusion matrix is:'.format(row))
print(cm[row])

names = []
for digit in digits.target_names:
    names.append(str(digit))

print(names)