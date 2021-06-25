import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        self.args = kwargs
        for color, number in kwargs.items():
            for i in range(number):
                self.contents.append(color)
    
    def draw(self,maxDraws):
        if maxDraws < len(self.contents):
            drawList = []
            for i in range(maxDraws):
                position = random.randrange(len(self.contents))
                drawList.append(self.contents[position])
                self.contents.pop(position)
            return drawList
        else:
            drawList,self.contents = self.contents,[]
            return drawList
        
def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    success = 0
    for experiment in range(num_experiments):
        copyHat = copy.deepcopy(hat)
        drawnList = copyHat.draw(num_balls_drawn)
        succesfulExperiment = 1
        for requiredColor,requiredNumber in expected_balls.items():
            experimentDraw = drawnList.count(requiredColor)
            if experimentDraw < requiredNumber:
                succesfulExperiment = 0
                break
        if succesfulExperiment:
            success+=1
    return success/num_experiments