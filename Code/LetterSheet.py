

class Player:
    def person(x,y,s):
        s[x,y]=5
        s[x+1,y]=0
        s[x+2,y]=5

        s[x,y+2]=5
        s[x+1,y+2]=0
        s[x+2,y+2]=5
        s[x,y+3]=0
        s[x+1,y+3]=0
        s[x+2,y+3]=0
        s[x,y+4]=0
        s[x+1,y+4]=5
        s[x+2,y+4]=0

class Letter:

    def A(x,y,s):
        s[x+1,y]=1
        s[x+3,y]=24

    def B(x,y,s):
        s[x,y]=0
        s[x+1,y]=2
        s[x+2,y]=3
        s[x+3,y]=105

    def C(x,y,s):
        s[x,y]=6
        s[x+1,y]=4
        s[x+2,y]=4
        s[x+3,y]=105

    def D(x,y,s):
        s[x,y]=0
        s[x+1,y]=7
        s[x+2,y]=11
        s[x+3,y]=105

    def E(x,y,s):
        s[x,y]=0
        s[x+1,y]=4
        s[x+2,y]=7
        s[x+3,y]=105


    def F(x,y,s):
        s[x,y]=0
        s[x+1,y]=1
        s[x+2,y]=17
        s[x+3,y]=105

    def G(x,y,s):
        s[x,y]=18
        s[x+1,y]=4
        s[x+2,y]=0
        s[x+3,y]=105

    def H(x,y,s):
        s[x,y]=0
        s[x+1,y]=22
        s[x+2,y]=0
        s[x+3,y]=105

    def I(x,y,s):
        s[x,y]=7
        s[x+1,y]=0
        s[x+2,y]=7
        s[x+3,y]=105

    def J(x,y,s):
        s[x,y]=7
        s[x+1,y]=0
        s[x+2,y]=17
        s[x+3,y]=105

    def K(x,y,s):
        s[x,y]=0
        s[x+1,y]=22
        s[x+2,y]=32
        s[x+3,y]=105


    def L(x,y,s):
        s[x,y]=0
        s[x+1,y]=34
        s[x+2,y]=34
        s[x+3,y]=105

    def M(x,y,s):
        s[x,y]=0
        s[x+1,y]=47
        s[x+2,y]=39
        s[x+3,y]=47
        s[x+4,y]=39
        s[x+5,y]=105

    def N(x,y,s):
        s[x,y]=39
        s[x+1,y]=22
        s[x+2,y]=39
        s[x+3,y]=105

    def O(x,y,s):
        s[x,y]=0
        s[x+1,y]=7
        s[x+2,y]=0
        s[x+3,y]=105

    def P(x,y,s):
        s[x,y]=0
        s[x+1,y]=1
        s[x+2,y]=47
        s[x+3,y]=105

    def Q(x,y,s):
        s[x,y]=48
        s[x+1,y]=49
        s[x+2,y]=0
        s[x+3,y]=105

    def R(x,y,s):
        s[x,y]=0
        s[x+1,y]=52
        s[x+2,y]=18
        s[x+3,y]=105

    def S(x,y,s):
        s[x,y]=18
        s[x+1,y]=4
        s[x+2,y]=56
        s[x+3,y]=105

    def T(x,y,s):
        s[x,y]=57
        s[x+1,y]=58
        s[x+2,y]=59
        s[x+3,y]=105

    def U(x,y,s):
        s[x,y]=0
        s[x+1,y]=34
        s[x+2,y]=0
        s[x+3,y]=105

    def V(x,y,s):
        s[x,y]=48
        s[x+1,y]=34
        s[x+2,y]=48
        s[x+3,y]=105

    def W(x,y,s):
        s[x,y]=48
        s[x+1,y]=39
        s[x+2,y]=11
        s[x+3,y]=39
        s[x+4,y]=48
        s[x+5,y]=105

    def X(x,y,s):
        s[x,y]=32
        s[x+1,y]=22
        s[x+2,y]=32
        s[x+3,y]=105

    def Y(x,y,s):
        s[x,y]=47
        s[x+1,y]=39
        s[x+2,y]=47
        s[x+3,y]=105

    def Z(x,y,s):
        s[x,y]=75
        s[x+1,y]=4
        s[x+2,y]=77
        s[x+3,y]=105