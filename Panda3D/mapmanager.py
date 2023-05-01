# напиши здесь код создания и управления картой
class Mapmanager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.color = (0.2,0.2,0.35,1)
        self.startNew()
    def addblock(self,position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)
        self.block.setTag('at',str(position))
    def startNew(self):
        self.land = render.attachNewNode('Land') 
    def loadLand(self,filename):
        with open(filename,'r') as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')                               
                line = list(map(int,line))
                for z in range(len(line)-1):
                    for z0 in range(line[z]+1):
                        block = self.addblock((x,y,z0))
                    x += 1
                y += 1 
    def isEmpty(self,pos):
        block = self.Find_Block(pos)
        if block:
            return False
        return True
    def Find_Block(self,pos):
        return self.land.findAllMatches('=at='+ str(pos))

    def FindHighestEmty(self,pos):
        x,y,z = pos
        z = 1
        while self.isEmpty((x,y,z)):
            z +=1
        return x,y,z       




