class MyManager:
    def __init__(self,value:int):
        self._val=value

    def __enter__(self):
        return self

    def __exit__(self,*args,**kwargs):
        pass

mngr=MyManager(value=10)

with mngr as mgr:
    print(mgr._val)
