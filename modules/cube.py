class RubiksCube:
    def __init__(self, canvas, offset):
        self.faces = []         # Will be initialized later, each face has 9 tiles
        self.offset = offset    # Offset from origin, used for rendering equations
        
        self.vertices = []      #TODO
        self.edges = []         #TODO
    
    origin_cubelet = {
        "verts": [
            [-50,-50,-50],
            [50,-50,-50],
            [50,-50,50],
            [-50,-50,50],
            [-50,50,-50],
            [50,50,-50],
            [50,50,50],
            [-50,50,50]
        ],
        "edges": [
            [0,1], [0,3], [2,1], [2,3],
            [4,5], [4,7], [6,5], [6,7],
            [0,4], [1,5], [2,6], [3,7],
            [0,7], [3,6], [2,5], [1,4],
            [4,6], [1,3]
        ],
        "faces": [
            [0,4,7,"#FFFFFF"], [0,7,3,"#FFFFFF"], #1
            [3,7,6,"#FFFF00"], [3,6,5,"#FFFF00"], #2
            [2,6,5,"#FF0000"], [2,5,1,"#FF0000"], #3
            [1,5,3,"#00FF00"], [1,4,0,"#00FF00"], #4
            [1,0,3,"#0000FF"], [1,3,2,"#0000FF"], #5
            [4,5,6,"#00FFFF"], [4,6,7,"#00FFFF"]  #6
        ]
    }

    def applyRotation(self, face, rotation):
        pass

    def render(self, canvas):
        pass

class CubeTile:
    def __init__(self, colour, face, pos):
        self.colour = colour
        self.pos = pos
        self.face = face

        self.vertices = []      #TODO
        self.coords = []        #TODO