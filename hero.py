
class Hero():
    def __init__(self,pos,land):
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1,0.5,1)
        self.hero.setPos(pos)
        self.hero.setScale(0.3)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()
        self.deltaH = 0
        self.deltaP = 0

        self.mode = True
    def cameraBind(self):
        base.disableMouse()
        base.camera.reparentTo(self.hero)  
        base.camera.setPos(0,0,1.5) 
        base.camera.setH(180) 
        self.cameraOn = True
    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0],-pos[1],-pos[2]-3)     
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False
    def accept_events(self):
        base.accept('c',self.changeView)
        #base.accept('n', self.turn_left)
        base.accept('n'+'-repeat', self.controlTask)

        base.accept('w', self.forward)
        base.accept('w'+'-repeat', self.forward)

        base.accept('s', self.back)
        base.accept('s'+'-repeat', self.back)

        base.accept('a', self.left)
        base.accept('a'+'-repeat', self.left)

        base.accept('d', self.right)
        base.accept('d'+'-repeat', self.right)

        base.accept('q', self.up)
        base.accept('q'+'-repeat', self.up)

        base.accept('e', self.down)
        base.accept('e'+'-repeat', self.down)
        base.accept('n', self.turn_left)
        base.accept('n' + '-repeat', self.turn_left)
        base.accept('m', self.turn_right)
        base.accept('m' + '-repeat', self.turn_right)

    def changeView(self): 
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()  
    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)


    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)

    def controlTask(self):  
        if base.mouseWatcherNode.hasMouse():        
            mpos = base.mouseWatcherNode.getMouse()*globalClock.getDt()*50
            print(mpos)
            H = self.deltaH - int(mpos[0]*50) 
            P = self.deltaP - int(mpos[1]*50)
            self.deltaH = int(mpos[0]*50) 
            self.deltaP = int(mpos[1]*50)
            if abs(self.deltaH) >= 0.5:
                self.hero.setH(self.hero.getH() + H)
            if abs(self.deltaP) >= 0.5:
                self.hero.setP(self.hero.getP() + P)       

    def just_move(self,angle):
        pos = self.look_at(angle) 
        self.hero.setPos(pos)
    def try_move(self,angle):
        pass      
    def move_to(self,angle):
        if self.mode:
            self.just_move(angle)        
    def look_at(self,angle):
        from_x = round(self.hero.getX()) 
        from_y = round(self.hero.getY())
        from_z = round(self.hero.getZ())

        dx,dy = self.check_dir(angle)
        return from_x +dx, from_y + dy, from_z
    def check_dir(self,angle):
        if 0 <= angle <= 20:
            return 0, -1 
        elif 20 < angle <= 65:
            return 1, -1 
        elif 65 < angle <= 110:
            return 1, 0 
        elif 110 < angle <= 155:
            return 1, 1 
        elif 155 < angle <= 200:
            return 0, 1 
        elif 200 < angle <= 245:
            return -1, 1   
        elif 245 < angle <= 290:
            return -1, 0 
        elif 290 < angle <= 335:
            return -1, -1
        elif 335 < angle <= 360:
            return 0, -1             
    def forward(self):
        angle = (self.hero.getH() + 0) % 360
        self.move_to(angle)
    def back(self):
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)
    def right(self):
        angle = (self.hero.getH() + 270) % 360
        self.move_to(angle)
    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)
    def up(self):
        self.hero.setZ(self.hero.getZ()+1)
    def down(self):
        self.hero.setZ(self.hero.getZ()-1)
