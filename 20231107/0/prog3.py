class A: pass
class B: pass
'''
class C(A): pass
class D(B, A): pass
'''
'''
class E(A, C): pass
'''
'''
class C(B): pass
class D(B, A): pass

class E(B, C): pass

class C(A, B): pass
class D(A, B): pass
class E(C, D): pass
'''
