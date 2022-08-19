class AdjacencyMatrix:
    """ Don't use numpy as there is ton of buil-ins. """

    def __init__(self):
        self.matrix = []
        self.size = 0
    
    def add_edge(self, vi, vj):
        assert vi >= 0; vj >= 0; vi != vj  # avoid self connected vertices

        if vi >= self.size or vj >= self.size:
            raise IndexError("Index out of matrix range. Node does not exist.")
 
        self.matrix[vi][vj] = 1
        self.matrix[vj][vi] = 1

    def remove_edge(self, vi, vj):
        assert vi >= 0; vj >= 0; vi != vj  # avoid self connected vertices

        if vi >= self.size or vj >= self.size:
            raise IndexError("Index out of matrix range. Vertex does not exist.")
 
        if not (self.matrix[vi][vj] == 1 and self.matrix[vj][vi] == 1):
            print(f"Vertices {vi} and {vj} are not connected. No changes to the graph.")
            return
        self.matrix[vi][vj] = 0
        self.matrix[vj][vi] = 0
        print(f"Vertices {vi} and {vj} have been disconnected.")


    def add_vertex(self):
        """ Add a vertex in order. """
        if len(self.matrix) == 0:
            self.matrix = [[0]]
            self.size = 1
            return 
        
        new_row = [0 for _ in range(0, self.size)]
        self.matrix.append(new_row)
        self.size += 1

        for i in range(0, self.size):
            self.matrix[i].append(0)

        

    def __str__(self):
        if self.size == 0: return "[]"
        out = "["
        for i in range(self.size):
            out += f"\n\t{str(self.matrix[i])},"
        out += "\n]"
        return out