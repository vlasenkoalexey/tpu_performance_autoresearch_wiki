_SPLASH_MESH = None

class A:
    def __call__(self):
        print("Mesh:", _SPLASH_MESH)

a = A()
a()
