#UNFINISHED

class Player:
    def person(x,y,s):      #will create a small humanoid player
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

class Letter:          #creates 3x5 letters followed by a space from individual 1x5 slices 

    def A(x,y,s):
        s[x+1,y]=129
        s[x+3,y]=145

    def B(x,y,s):
        s[x+1,y]=130
        s[x+2,y]=131
        s[x+3,y]=145

    def C(x,y,s):
        s[x+1,y]=132
        s[x+2,y]=132
        s[x+3,y]=145

    def D(x,y,s):
        s[x+1,y]=132
        s[x+2,y]=133
        s[x+3,y]=145

    def E(x,y,s):
        s[x+1,y]=130
        s[x+2,y]=132
        s[x+3,y]=145

    def F(x,y,s):
        s[x+1,y]=129
        s[x+2,y]=134
        s[x+3,y]=145

    def G(x,y,s):
        s[x,y]=135
        s[x+1,y]=130
        s[x+3,y]=145

    def H(x,y,s):
        s[x+1,y]=136
        s[x+3,y]=145

    def I(x,y,s):
        s[x,y]=132
        s[x+2,y]=132
        s[x+3,y]=145

    def J(x,y,s):
        s[x,y]=132
        s[x+2,y]=134
        s[x+3,y]=145

    def K(x,y,s):
        s[x+1,y]=136
        s[x+2,y]=137
        s[x+3,y]=145

    def L(x,y,s):
        s[x+1,y]=138
        s[x+2,y]=138
        s[x+3,y]=145

    def M(x,y,s):
        s[x+1,y]=140
        s[x+2,y]=139
        s[x+3,y]=140
        s[x+5,y]=145

    def N(x,y,s):
        s[x,y]=139
        s[x+1,y]=136
        s[x+2,y]=139
        s[x+3,y]=145

    def O(x,y,s):
        s[x+1,y]=132
        s[x+3,y]=145

    def P(x,y,s):
        s[x+1,y]=129
        s[x+2,y]=140
        s[x+3,y]=145

    def Q(x,y,s):
        s[x,y]=141
        s[x+1,y]=142
        s[x+3,y]=145

    def R(x,y,s):
        s[x+1,y]=143
        s[x+2,y]=135
        s[x+3,y]=145

    def S(x,y,s):
        s[x,y]=135
        s[x+1,y]=130
        s[x+2,y]=143
        s[x+3,y]=145

    def T(x,y,s):
        s[x,y]=134
        s[x+2,y]=134
        s[x+3,y]=145

    def U(x,y,s):
        s[x+1,y]=138
        s[x+3,y]=145

    def V(x,y,s):
        s[x,y]=141
        s[x+1,y]=138
        s[x+2,y]=141
        s[x+3,y]=145

    def W(x,y,s):
        s[x,y]=141
        s[x+1,y]=139
        s[x+2,y]=140
        s[x+3,y]=139
        s[x+4,y]=141
        s[x+5,y]=145

    def X(x,y,s):
        s[x,y]=137
        s[x+1,y]=136
        s[x+2,y]=137
        s[x+3,y]=145

    def Y(x,y,s):
        s[x,y]=140
        s[x+1,y]=139
        s[x+2,y]=140
        s[x+3,y]=145

    def Z(x,y,s):
        s[x,y]=273
        s[x+1,y]=130
        s[x+2,y]=274
        s[x+3,y]=145

    def ONE(x,y,s):
        s[x,y]=132
        s[x+2,y]=138
        s[x+3,y]=145

    #def TWO(x,y,s):        #ran into memory errors at the end with some of these numbers
      #  s[x,y]=143
     #   s[x+1,y]=130
     #   s[x+2,y]=135
      #  s[x+3,y]=145

    def THREE(x,y,s):
        s[x,y]=130
        s[x+1,y]=130
        s[x+3,y]=145

    def FOUR(x,y,s):
        s[x,y]=140
        s[x+1,y]=136
        s[x+3,y]=145

    #def SIX(x,y,s):
       # s[x+1,y]=130
       # s[x+2,y]=139
       # s[x+3,y]=145

   # def SEVEN(x,y,s):
    #    s[x,y]=134
    #    s[x+1,y]=134
      #  s[x+3,y]=145

    def EIGHT(x,y,s):
        s[x+1,y]=130
        s[x+3,y]=145
