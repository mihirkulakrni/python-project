class MyNewRouter(MyRouters):
    def __init__(self , routername, model, serialno, ios, portsno):
        MyRouters.__init__(self,routername,model,serialno,ios)
        self.portsno = portsno

    def print_new_router(self,string):
        print(string + self.model)



        
    
