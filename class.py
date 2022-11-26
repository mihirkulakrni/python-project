class MyRouters(object):
    "This is class that describes the charactersitics of a router"
    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios
    def print_router(self, manuf_date):
        print("The router name is:",self.routername)
        print("The router model is:",self.model)
        print("The serialno is:",self.serialno)
        print("The IOS Version is:",self.ios)
        print("The model and date combained :",self.model + manuf_date)
        
        
