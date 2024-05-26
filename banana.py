import random

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
        if eval > maxVal:
            maxVal = eval
            bestFeature = x
    return bestFeature, maxVal


def random_eval():
    return random.random()

def forward_selection(numFeatures):
    features = set()
    for i in range(0,numFeatures):
        features = expand_forward(features, numFeatures)
        features, maxVal = pick_best(features)
        print(features, maxVal)

def backward_selection(numFeatures):
    features = frozenset({x for x in range(1,numFeatures+1)})
    eval = random_eval()
    print(features, eval)
    for i in range(0,numFeatures-1):
        features = expand_backward(features)
        features, maxVal = pick_best(features)
        print(features, maxVal)
        
# forward_selection(10)
backward_selection(10)






# print(expand_backward({1,2,3,4,5,6}))
# print(expand_forward(set(), 5))
# print(random_eval())





