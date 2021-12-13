class Event():

    def __init__(self,text = "",myfunction = "",function_args = {},probability = 0.1):
        text_dict = {"text": text}
        self.function_args = {**text_dict,**function_args}
        self.myfunction  = myfunction 
        self.probability = probability
    
    def getFunction(self):
        return str(self.myfunction)

    def getProbabilitiy(self):
        return self.probability
    
    def getFunctionArgs(self):
        #print(self.function_args)
        return self.function_args
    
    
