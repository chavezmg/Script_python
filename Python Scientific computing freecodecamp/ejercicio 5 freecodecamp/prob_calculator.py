import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for element in kwargs:
            #colorBall = f"{element}: {kwargs[element]}"
            for ball in range(kwargs[element]):
                self.contents.append(element)
    
    def draw(self, number):
        self.returnList = []
        if number > len(self.contents):
            number = len(self.contents)
        for i in range(0, number):
            bola = random.choice(self.contents) #pick a random ball
            self.contents.remove(bola)          #delete from list
            self.returnList.append(bola)            #append ball to list
        return self.returnList               

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    ballDraw = []
    dictDraw = {}
    expected_balls_list = []
    matches = 0

    for element in expected_balls:
            for ball in range(expected_balls[element]):
                expected_balls_list.append(element)

    for i in range(num_experiments):
        hatcopy = hat.contents.copy()
        ballDraw = hat.draw(num_balls_drawn)        #list with drawed balls

        for ball in ballDraw:
            ballQuantity = ballDraw.count(ball)
            dictDraw[ball] = ballQuantity           #make a dict from drawed list

        #if expected_balls.items() <= dictDraw.items():
        #   matches += 1
        #   print("match")
        if expected_balls.keys() <= dictDraw.keys():
            match = 0
            for key in expected_balls.keys():
                if expected_balls[key] <= dictDraw[key]:
                    match += 1
                else:
                    match -= 1
            if match >= 1:
                matches += 1

        #print("*expected balls: ", expected_balls)   #debuggin purp
        #print("*ball draw: ", dictDraw)              #debuggin purp
        dictDraw = {}                           #reset the dict so they values don't append with next draw
        hat.contents = hatcopy.copy()
    
    print("matches: ", matches)                     #debuggin purp
    probabilidad = matches/num_experiments
    return probabilidad

sombrero = Hat(blue=3, red=2, green=6)
print(experiment(sombrero, {"blue":2, "green":1}, 11, 100))

