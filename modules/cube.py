class RubiksCube:
    def __init__(self, canvas, offset):
        self.faces = []         # Will be initialized later, each face has 9 tiles
        self.offset = offset    # Offset from origin, used for rendering equations
        
        self.vertices = []      #TODO
        self.edges = []         #TODO
    
    @NotImplemented
    def applyRotation(self, face, rotation):
        pass

    @NotImplemented
    def render(self, canvas):
        pass

class CubeTile:
    def __init__(self, colour, face, pos):
        self.colour = colour
        self.pos = pos
        self.face = face

        self.vertices = []      #TODO
        self.coords = []        #TODO