
class Food:
    def set (self,type,weight):
        self.type = type
        self.weight = weight


    def calcCalories(self):
        if (self.type == 1):                          # tomato
            self.calory = self.weight * 0.4
        elif(self.type==2):                            # Cucumber
            self.calory= self.weight * 0.2
        elif(self.type==3):                            # cheese
            self.calory=self.weight * 0.8
        elif(self.type==4):                            # bread
            self.calory= self.weight * 0.5

bread=Food()
bread.set(4,500)
bread.calcCalories()


cucumber = Food()
cucumber.set(2,800)
cucumber.calcCalories()

cheese = Food()
cheese.set(3,150)
cheese.calcCalories()

foodList =[]
foodList.append(bread)
foodList.append(cucumber)
foodList.append(cheese)

for food in foodList:
    print(food.calory)

