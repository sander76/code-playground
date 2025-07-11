class Go:
    @classmethod
    def go(cls, intance):
        return cls()


go = Go()
res = go.go(go)

print(res)
