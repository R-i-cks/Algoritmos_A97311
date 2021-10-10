

import random
def primeiroj():
    fosf=21
    j= float(input("Introduza 1 ou 2 conforme pretenda jogar em primeiro ou segundo, respetivamente: "))
    if j!= 1 and j!=2:
        print("Jogador inválido")   
    else:               
        while (fosf!= 1):   
                a=jogada1(j,fosf)
                fosf=a
        
    
#--------------------------------------------------------------------------------------------------
def jogada1(j,fosf):
    A=[1,2,3,4]  
    if j==1 and fosf==1:
          print("O jogador perde")
          return        
    elif j==1 and fosf!=1: # jogador primeiro
        j1=float(input("Introduza um valor entre 1 e 4: "))
        vrf=A.count(j1)
        if vrf!=0:     # Verifica se a jogada é possível
            fosf=(fosf-j1)
            print(fosf) 
            if (fosf<=5):
                j2=(fosf-1)
                fosf=(fosf-j2)  #O computador joga e retira o mesmo número de fósforos
                print(fosf)
                print("O computador vence!!!")
                return fosf
            else:
                j2=(5-j1)
                fosf=fosf-j2
                print(fosf)
                return fosf            
        else:
            print("Valor inválido")
            return
   
    elif j==2: 
                j1= random.choice(A)
                fosf=(fosf-j1)
                print(fosf)
                j2=float(input("Introduza um valor entre 1 e 4: "))
                vrf2=A.count(j2)
                if vrf2!=0: 
                    fosf=fosf-j2
                    print(fosf)
                    if (j1+j2)==5:
                        if fosf==1:
                            print("O jogador vence")
                            return fosf
                        else:
                            return fosf
                    elif (j1+j2)<5: 
                        j3=j1
                        j4=j2
                        j1=(5-(j3+j4))
                        fosf=fosf-j1
                        print(fosf)
                        j=1
                        return fosf
                    else:
                        return fosf
                else:
                    print("Jogada Inválida!!")
                    
primeiroj()

    
        
        
    
        
        
    


    
        