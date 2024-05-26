import random
import re

reg = re.compile('\{(.*)\}')

# instance has id, label, and feature values



def expand_forward(features, numFeatures):
    a = {x for x in range(1,numFeatures+1)}
    return {frozenset(features | {x}) for x in a.difference(features)}

def expand_backward(features):
    return {frozenset(features - {x}) for x in features}

def pick_best(features):
    bestFeature = None
    maxVal = 0
    for x in features:
        eval = random_eval()
        print("        Using feature(s) {{{}}} accuracy is {:.1f}%".format(reg.findall(str(x))[0],eval*100))
        if eval > maxVal:
            maxVal = eval
            bestFeature = x
    return bestFeature, maxVal


def random_eval():
    return random.random()

def forward_selection(numFeatures):
    features = set()
    lastAccuracy = random_eval()
    bestAccuracy = lastAccuracy
    bestFeatureSet = features
    print("\nUsing no features and “random” evaluation, I get an accuracy of {:.1f}%".format(lastAccuracy*100))
    print("\nBeginning search.\n")
    for i in range(0,numFeatures):
        features = expand_forward(features, numFeatures)
        features, maxVal = pick_best(features)
        print()
        if lastAccuracy > maxVal:
            print("(Warning, Accuracy has decreased!)")
        print("Feature set {{{}}} was best, accuracy is {:.1f}%\n".format(reg.findall(str(features))[0],maxVal*100))
        if maxVal > bestAccuracy:
            bestAccuracy = maxVal
            bestFeatureSet = features
        lastAccuracy = maxVal
    print("Finished search!! The best feature subset is {{{}}}, which has an accuracy of {:.1f}%".format(reg.findall(str(bestFeatureSet))[0],bestAccuracy*100))


def backward_elimination(numFeatures):
    features = frozenset({x for x in range(1,numFeatures+1)})
    lastAccuracy = random_eval()
    bestAccuracy = lastAccuracy
    bestFeatureSet = features
    print("\nUsing all features and “random” evaluation, I get an accuracy of {:.1f}%".format(lastAccuracy*100))
    print("\nBeginning search.\n")

    for i in range(0,numFeatures-1):
        features = expand_backward(features)
        features, maxVal = pick_best(features)
        print()
        if lastAccuracy > maxVal:
            print("(Warning, Accuracy has decreased!)")
        print("Feature set {{{}}} was best, accuracy is {:.1f}%\n".format(reg.findall(str(features))[0],maxVal*100))
        if maxVal > bestAccuracy:
            bestAccuracy = maxVal
            bestFeatureSet = features
        lastAccuracy = maxVal
    print("Finished search!! The best feature subset is {{{}}}, which has an accuracy of {:.1f}%".format(reg.findall(str(bestFeatureSet))[0],bestAccuracy*100))




