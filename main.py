import banana
import selector

def remove_items(test_list, item):
    res = [i for i in test_list if i != item]
    return res


class GUI:
    def __init__(self):
        self.selector = selector.Selector()
        self.selector.load1("small-test-dataset-1.txt")
        self.selector.load2("large-test-dataset-1.txt")

    def start(this):
        numFeatures = this.get_numfeatures()
        numFeatures = numFeatures.split(" ")
        algoNum = this.get_algonum()
        this.selector.validate(algoNum, numFeatures)


    def get_numfeatures(this):
        print("Welcome to Feature Selection Algorithm.")
        print("Please enter which features you would like to use with spaces in between: ", end='')
        return input()
    def get_algonum(this):
        print("\nType the number of the algorithm you want to run.")
        print("        1 - Small Dataset")
        print("        2 - Large Dataset")
        return int(input())


a = GUI()
a.start()