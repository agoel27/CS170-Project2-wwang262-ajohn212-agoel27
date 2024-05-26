import banana

class GUI:
    def start(this):
        numFeatures = this.get_numfeatures()
        algoNum = this.get_algonum()
        algorithms = [banana.forward_selection,banana.backward_elimination]
        algorithms[algoNum-1](numFeatures)



    def get_numfeatures(this):
        print("Welcome to [Team Names] Feature Selection Algorithm.")
        print("Please enter total number of features: ") 
        return int(input())
    def get_algonum(this):
        print("Type the number of the algorithm you want to run.")
        print("1 - Forward Selection")
        print("2 - Backward Elimination")
        return int(input())


a = GUI()
a.start()