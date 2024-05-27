import banana
import math


def remove_items(test_list, item):
    res = [i for i in test_list if i != item]
    return res


# Calculates the Euclidean Distance between two points in nth dimension
def euclidean(feature1, feature2):
    total = 0
    for i in range(len(feature1)):
        diff = feature1[i] - feature2[i]
        total += pow(diff,2)
    return math.sqrt(total)


class Classifier:
    def __init__(self):
        self._features = []

    # Returns the dataset as a list
    def get_features(self):
        return self._features

    # appends new features to the dataset
    def train(self, features):
        self._features.append(features)

    # clears the data from the dataset
    def clear(self):
        self._features = []

    # tests Euclidean distance between all data points to the test case,
    # then gets the nearest data point and returns its label (the first element in the list)
    # Note: disregards the first element in the list when calculating distance
    def test(self, test_feature):
        closest = []
        closest_distance = math.inf
        for feature_in_features in self._features:
            distance = euclidean(feature_in_features[1:], test_feature[1:])
            if distance < closest_distance:
                closest = feature_in_features
                closest_distance = distance
        return closest[0]


class Validator:
    def __init__(self):
        self._features = []

    # clears the dataset
    def clear(self):
        self._features = []

    # Appends new data to the dataset
    def train(self, features):
        self._features.append(features)

    # Validates the dataset using leave-one-out validation
    def validate(self):
        test_count = 0
        total = 0
        for i in range(len(self._features)):
            test_classifier = Classifier()
            test_set = self._features.copy()
            test_feature = test_set.pop(i)
            for j in range(len(test_set)):
                test_classifier.train(test_set[j])
            test_label = test_feature[0]
            predicted_label = test_classifier.test(test_feature)
            print("expected label is", test_label, "predicted label is", predicted_label)
            if test_label == predicted_label:
                test_count += 1
            total += 1
        return test_count/total


# initialize validator
# opens test files and loads the data into the validator
# Small Dataset: (only the label, feature 3, feature 5, and feature 7)
# Large Dataset: (only the label, feature 3, feature 5, and feature 7)
validator = Validator()
file = open("small-test-dataset-1.txt", "r")
count = 0
while True:
    content = file.readline()
    feature = content.split(" ")
    if not content:
        break
    feature = remove_items(feature, "")
    feature = [float(i) for i in feature]
    feature = [feature[0], feature[3], feature[5], feature[7]]
    validator.train(feature)
    count += 1
file.close()

print("Small dataset {3,5,7} Accuracy:", validator.validate())
validator.clear()

file = open("large-test-dataset-1.txt", "r")
count = 0
while True:
    content = file.readline()
    feature = content.split(" ")
    if not content:
        break
    feature = remove_items(feature, "")
    feature = [float(i) for i in feature]
    feature = [feature[0], feature[1], feature[15], feature[27]]
    validator.train(feature)
    count += 1
file.close()

print("Large dataset {1,15,27} Accuracy:", validator.validate())