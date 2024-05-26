import random

# instance has id, label, and feature values

def expand(features, numFeatures):
    a = {x for x in range(1,numFeatures+1)}
    return {frozenset(features | {x}) for x in a.difference(features)}

def random_eval():
    return random.random()

def forward_selection(numFeatures):
    features = set()
    for i in range(0,numFeatures):
        features = expand(features, numFeatures)
        maxVal = 0
        bestFeature = None
        for x in features:
            eval = random_eval()
            if eval > maxVal:
                maxVal = eval
                bestFeature = x
        features = bestFeature
        print(features, maxVal)
        
forward_selection(10)






# print(expand(set(), 5))
# print(random_eval())





