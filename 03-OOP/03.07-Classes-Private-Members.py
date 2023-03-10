class Demo:
    def __secret(self):
        print("No one can know")

    def public(self):
        print("Everyone can know")

    def get_secret(self, pwd):
        if pwd == "12345":
            self.__secret()
        else:
            print("Forbidden")


demo = Demo()
demo.public()
demo.get_secret("54321")
demo.get_secret("12345")
print(dir(demo))
demo._Demo__secret()
