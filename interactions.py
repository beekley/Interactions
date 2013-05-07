class Human():
	def giveItem(self,item):
		self.inventory.append(item)
	money = 0
	hunger = 0
	inventory = []
	
class Food():
	filling = 50
	
Paul = Human()
Banana = Food()
