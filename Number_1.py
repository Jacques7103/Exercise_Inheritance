class Z:
    def __init__(self) -> None:
        pass

class Y:
    def __init__(self) -> None:
        pass
    
class X:
    def __init__(self) -> None:
        pass
    
class B(Y, Z):
    def __init__(self) -> None:
        super().__init__()

class A(X, Y):
    def __init__(self) -> None:
        super().__init__()
        
class M(A, B, Z):
    def __init__(self) -> None:
        super().__init__()
        
if __name__ == "__main__":
    M()