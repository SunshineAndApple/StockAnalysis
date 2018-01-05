class Request(object):
    isAnalysis = False
    level = None

    def getVarNameFromList(self, index):
        ## a2, b2, b1, a3, b3, a4序列为查找序列
        switcher = {0:'a2', 1:'b2', 2:'b1', 3:'a3', 4:'b3', 5:'a4'}
        return switcher[index]

class Analysis(object):
    successor = None
    name = None

    def __init__(self, name):
        self.name = name

    def SetSuccessor(self, successor):
        self.successor = successor

    def HandleReuqest(self, request):
        pass

class A(Analysis):
    def HandleReuqest(self, request):
        if self.successor != None:
            print('a')
            self.successor.HandleReuqest(request)
            '''
        if request.isAnalysis == False and request.level == 'A':
            print('a')
            if self.successor != None:
                request.level = 'B'
                request.isAnalysis = False
                self.successor.HandleReuqest(request)'''

class B(Analysis):
    def HandleReuqest(self, request):
        print('b')
        '''
        if request.isAnalysis == False and request.level == 'B':
            print('b')
            if self.successor != None:
                request.level = 'B'
                request.isAnalysis = False
                #self.successor.HandleReuqest(request)'''

class Client(object):
    a = A('A')
    b = B('B')

    a.SetSuccessor(b)

    request = Request()
    request.isAnalysis = False
    request.level = 'A'
    a.HandleReuqest(request)
    print("tst")
    l = [1,0,123]


    for v in l:
        if (0 == (v | 0)):
            #print(l.index(v))
            print('index %s' % request.getVarNameFromList(l.index(v)))


if __name__ == '__main__':
    c = Client()
    l = [0, 1, 2, 3, 4, 5]
    print(max(l[4:5+1]))
