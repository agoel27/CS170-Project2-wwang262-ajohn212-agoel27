import math
import time
import pandas as pd 


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


class Selector():
    def __init__(self):
        self.dataset = []
        #self.dataset2 = []
        self.validator = Validator()

    def load(self, filename):
        self.dataset = []
        file = open(filename, "r")
        count = 0
        while True:
            content = file.readline()
            feature = content.split(" ")
            if not content:
                break
            feature = remove_items(feature, "")
            feature = [float(i) for i in feature]
            self.dataset.append(feature)
        file.close()

        df = pd.DataFrame(self.dataset)
        for column in df.columns[1:]: 
            df[column] = df[column]  / df[column].abs().max()
        
        print(df.to_string())

        self.dataset = df.values.tolist()

    def validate(self, database_name, list_of_features):
        curr = time.time()
        list_of_features = [int(i) for i in list_of_features]
        self.load(database_name)
        dataset = self.dataset
        for feature in dataset:
            new_feature = [feature[0]]
            for i in list_of_features:
                if i != 0:
                    new_feature.append(feature[i])
            self.validator.train(new_feature)
        #print("Using features ", list_of_features)
        accuracy = self.validator.validate()
        self.validator.clear()
        #print("Accuracy: ", accuracy)
        curr = time.time()-curr
        #print("Time taken to train:", round(curr,4), "s")
        return accuracy

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
        # print("Instance", test_feature, "is class ", closest[0])
        # print("Its nearest neighbor is ", closest, "which is class", closest[0])
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
        curr = time.time()
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
            if test_label == predicted_label:
                test_count += 1
            total += 1
        curr = time.time()-curr
        # print("Time taken to validate:", round(curr,4), "s")
        return test_count/total
