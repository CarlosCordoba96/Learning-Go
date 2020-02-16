class Dados:
    def __init__(self,tiradas,ptosAsuperar):
        self._tiradas=tiradas
        self._ptosAsuperar=ptosAsuperar

    def iniciar(self):
        lista=[]
        self.backTracking(0,lista,0)

    def suma(self,lista):
        suma=0
        for i in lista:
            suma+=i
        return suma

    def backTracking(self,etapa,lista,suma):
        if etapa==self._tiradas:
            if suma>self._ptosAsuperar:
                print(lista)
                print(self.suma(lista))
        else:
            for i in range(1,7):
                suma+=i
                lista.insert(etapa,i)
                self.backTracking(etapa+1,lista,suma)
                lista.pop(etapa)
                suma-=i

d= Dados(20,100)
d.iniciar()
