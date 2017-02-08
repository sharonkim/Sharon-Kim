class Vertebrate(object):

    def __init__(self):
        self.has_backbone = True

class Bird(Vertebrate):

    def __init__(self):
        super(Bird, self).__init__()
        self.feathers = True
        self.warm_blooded = True
        self.lays_eggs = True

class Lizard(Vertebrate):

    def __init__(self):
        super(Lizard, self).__init__()
        self.warm_blooded = False
        self.lays_eggs = True
        self.has_scales = True

class Dinosaur(Bird, Lizard):

    def __init__(self):
        super(Dinosaur, self).__init__()
        self.feathers = False

dino = Dinosaur()
print dino.has_scales
print dino.lays_eggs
print dino.feathers
print dino.warm_blooded
print dino.has_backbone
