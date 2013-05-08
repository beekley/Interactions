class Human():
	def __init__(self, myname="Paul"):
        self.name = myname
		
	def giveItem(self,item):
		self.inventory.append(item)
	
	def purchaseItem(self, buyer, itemType):
		itemCount = 0
		for item in self.inventory:
			if isinstance(item, itemType):
				itemCount += 1
		
		if itemCount > 1:
			for item in self.inventory:
				if isinstance(item, itemType) and buyer.money >= item.cost:
					buyer.inventory.append(item)
					self.inventory.remove(item)
					self.money -= item.cost
					seller.money += item.cost
			return True
		else:
			return False
				
	def checkHunger(self):
		if self.hunger >= 100:
			for seller in Town:
				if seller.name != self.name:
					purchaseItem(seller, Food)
			
		if self.hunger >= 50:
			for item in self.inventory:
				if isinstance(item, Food) and self.hunger > 0:
					self.hunger -= item.filling
					self.inventory.remove(item)
					
			if self.hunger >= 50:
				print('%s is pretty hungry.' %self.name)
		if self.hunger < 0:	
			self.hunger = 0
	
	def update(self):
		self.hunger += 10
		self.checkHunger()
			
	money = 0
	hunger = 0
	inventory = []
	
class Food():
	filling = 50
	cost = 10

def Update():
	for person in Town:
		person.update()
	
Banana = Food()
Paul = Human()
Steve = Human()
Town = [Paul, Steve]

Steve.giveItem(Banana)
Steve.giveItem(Banana)
Steve.giveItem(Banana)
