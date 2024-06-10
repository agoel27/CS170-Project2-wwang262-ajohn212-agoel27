import banana
import selector
import random
import re

reg = re.compile('\{(.*)\}')

class GUI:
    def __init__(self):
        self.selector = selector.Selector()
        self.algonum = self.get_algonum()
        self.database_name = self.get_database_name()
        self.numInstances = 0
        self.defaultRate = 0
        #self.selector.load1("small-test-dataset-1.txt")
        #self.selector.load2("large-test-dataset-1.txt")

    def start(self):

        numInstances = 0
        numOne = 0
        file = open(self.database_name, "r")
        while True:
            content = file.readline()
            feature = content.split(" ")
            if not content:
                break
            feature = [i for i in feature if i != ""]
            feature = [float(i) for i in feature]
            if feature[0] == 1.0:
                numOne += 1
            numInstances += 1
        file.close()
        self.numInstances = numInstances
        if 1 - numOne/numInstances > numOne/numInstances:
            self.defaultRate = 1 - numOne/numInstances
        else:
            self.defaultRate = numOne/numInstances

        # finding number of features
        file = open(self.database_name, "r")
        content = file.readline()
        feature = content.split(" ")
        feature = [i for i in feature if i != ""]
        self.numFeatures = len(feature) - 1
        print("This dataset has " + str(self.numFeatures) + " features with " + str(numInstances) + " instances")
        file.close()

        # running algorithm
        if self.algonum == 1:
            self.forward_selection(self.numFeatures)
        else:
            self.backward_elimination(self.numFeatures)
        # this.selector.validate(database_name, numFeatures)


    def get_algonum(self):
        print("Welcome to William Wang, Anthony Johnson, Aryan Goel Feature Selection Algorithm.")
        print("\nType the number of the algorithm you want to run.")
        print("        1 - Forward Selection")
        print("        2 - Backward Selection")
        return int(input())
    def get_database_name(self):
        print("\nPlease type the name of the database with the training data: ", end='')
        return input()

    def expand_forward(self, features, numFeatures):
        a = {x for x in range(1,numFeatures+1)}
        return {frozenset(features | {x}) for x in a.difference(features)}

    def expand_backward(self, features):
        return {frozenset(features - {x}) for x in features}

    def pick_best(self, features):
        bestFeature = None
        maxVal = 0
        for x in features:
            eval = self.selector.validate(self.database_name, list(x))
            print("        Using feature(s) {{{}}} accuracy is {:.1f}%".format(reg.findall(str(x))[0],eval*100))
            if eval > maxVal:
                maxVal = eval
                bestFeature = x
        return bestFeature, maxVal


    def random_eval(self):
        return random.random()

    def forward_selection(self, numFeatures):
        features = set()

        lastAccuracy = self.defaultRate
        bestAccuracy = lastAccuracy
        bestFeatureSet = features
        print("\nUsing no features , I get an accuracy of {:.1f}%".format(lastAccuracy*100))
        print("\nBeginning search.\n")
        for i in range(0,numFeatures):
            features = self.expand_forward(features, numFeatures)
            features, maxVal = self.pick_best(features)
            print()
            if lastAccuracy > maxVal:
                print("(Warning, Accuracy has decreased!)")
            print("Feature set {{{}}} was best, accuracy is {:.1f}%\n".format(reg.findall(str(features))[0],maxVal*100))
            if maxVal > bestAccuracy:
                bestAccuracy = maxVal
                bestFeatureSet = features
            lastAccuracy = maxVal
        print("Finished search!! The best feature subset is {{{}}}, which has an accuracy of {:.1f}%".format(reg.findall(str(bestFeatureSet))[0],bestAccuracy*100))


    def backward_elimination(self, numFeatures):
        features = frozenset({x for x in range(1,numFeatures+1)})
        initial_feature_list = []
        for i in range(1, numFeatures + 1):
            initial_feature_list.append(i)
        lastAccuracy = self.selector.validate(self.database_name, initial_feature_list)
        bestAccuracy = lastAccuracy
        bestFeatureSet = features
        print("\nUsing all features, I get an accuracy of {:.1f}%".format(lastAccuracy*100))
        print("\nBeginning search.\n")

        for i in range(0,numFeatures-1):
            features = self.expand_backward(features)
            features, maxVal = self.pick_best(features)
            print()
            if lastAccuracy > maxVal:
                print("(Warning, Accuracy has decreased!)")
            print("Feature set {{{}}} was best, accuracy is {:.1f}%\n".format(reg.findall(str(features))[0],maxVal*100))
            if maxVal > bestAccuracy:
                bestAccuracy = maxVal
                bestFeatureSet = features
            lastAccuracy = maxVal
        print("Finished search!! The best feature subset is {{{}}}, which has an accuracy of {:.1f}%".format(reg.findall(str(bestFeatureSet))[0],bestAccuracy*100))


a = GUI()
a.start()

# forward_selection(5)