#!/bin/python3
import sys
def O00OOOO00O00O0O00 (OOOOOOOOOOO0O0O00 ,O0O0OOOOOO0OOOO00 ):
    O000O0O00O0O00O0O ={}
    def OOOOO00O0OOOOO0O0 (OO0OOOO00O00O0O0O ,O0OOO0OO0O0OO0O00 ):
        O000O0000OOO000O0 =(OO0OOOO00O00O0O0O ,O0OOO0OO0O0OO0O00 )
        if O000O0000OOO000O0 in O000O0O00O0O00O0O :
            return O000O0O00O0O00O0O [O000O0000OOO000O0 ]
        if OO0OOOO00O00O0O0O >=len (OOOOOOOOOOO0O0O00 )or O0OOO0OO0O0OO0O00 <0 :
            return 0
        elif O0OOO0OO0O0OO0O00 ==0 :
            return 1
        else :
            O0O0OO00O00OOOOOO =0
            O0O0OO00O00OOOOOO +=OOOOO00O0OOOOO0O0 (OO0OOOO00O00O0O0O +1 ,O0OOO0OO0O0OO0O00 )
            O0O0OO00O00OOOOOO +=OOOOO00O0OOOOO0O0 (OO0OOOO00O00O0O0O ,O0OOO0OO0O0OO0O00 -OOOOOOOOOOO0O0O00 [OO0OOOO00O00O0O0O ])
            O000O0O00O0O00O0O [O000O0000OOO000O0 ]=O0O0OO00O00OOOOOO
            return O0O0OO00O00OOOOOO
    return OOOOO00O0OOOOO0O0 (0 ,O0O0OOOOOO0OOOO00 )
n ,m =input ().strip ().split (' ')
n ,m =[int (n ),int (m )]
OO0OOOO00O00O0O00 =[int (OO0O0000000OOOO0O )for OO0O0000000OOOO0O in input ().strip ().split (' ')]
print (O00OOOO00O00O0O00 (OO0OOOO00O00O0O00 ,n ))
