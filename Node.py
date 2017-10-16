class Node :

    '''A base class to define Node properties.'''

    count = 0

    def __init__( self, theAnimal ) :

        self.isLeaf = True
        self.mark = None
        self.animal = theAnimal
        self.knotLeft = None
        self.knotRight = None
        Node.count += 1

    def makeKnot(self, response, pLeft, pRigt) :

        self.isLeaf = False
        self.mark = response
        self.knotLeft = pLeft
        self.knotRight = pRigt


