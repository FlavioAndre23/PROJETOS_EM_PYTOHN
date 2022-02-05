import math 


import time



class carro:
    def __init__ (self, ano ,maxvel,modelo,t):
        self.ano= ano
        self.maxvel= maxvel
        self.modelo= modelo
        self.a= 0
        self.temp= t
        return

    def acel(self,maxvel, a,temp):
        self.acelera= self.maxvel/ self.temp
        print ("%f"%(self.acelera))
        
    pass



carro.acel(40,1,2)
