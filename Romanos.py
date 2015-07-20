# -*- coding: ISO-8859-1 -*-
#-------------------------------------------------------------------------------
# @name:        Romanos.py
# @purpose:     Transformar numeros em Algarismos romanos
#
# @author:      saozinha12@gmail.com
#
# @created:     19/07/2015
# @copyright:   Conceicao Lourenco
# @licence:     GPL
#-------------------------------------------------------------------------------


rom  = {1 : "I", 2 : "II", 3: "III", 4 : "IV", 5 : "V", 6 : "VI", 7 : "VII", 8 : "VIII", 9 : "IX",
        10 : "X", 11 : "XI", 12 : "XII", 13 : "XIII", 50 : "L", 100:"C", 112:"CXII", 500:"D", 1000:"M"}
    
saida = "erro"

def integerAchaDecimal(dec):
    algarismo = ""
    i = 1
    # 10
    if int(dec) == 1:
            algarismo = rom[10]
    else:
            # 20 a 30
        if int(dec) <= 3:
            while (i <= int(dec)) :
                algarismo += rom[10]
                i = i + 1
        else:
                # 40 pra cima
            if int(dec) == 4 : 
                    algarismo = rom[40]
            else:
                    # 50 
                if int(dec) == 5 : 
                        algarismo = rom[50]
                else:
                    # acima de 50
                    if int(dec) <= 8 :
                        algarismo = rom[50]
                        i = 5
                        while (i < int(dec)) :
                            algarismo += rom[10]
                            i = i + 1  
                        
                    else:
                        if int(dec) == 9 : 
                            algarismo = rom[10] + rom[100]
                            #saida = rom[10]+ rom[100] + rom[un]
  
    #print ("Resultado Dezena - Algarismo >> ", algarismo)
    return algarismo 

def integerAchaCentena(dec):
    algarismo = ""
    i = 1
    # se for 1 = 100 
    if int(dec) == 1:
            algarismo = rom[100]
    else:
        # acima de 100 ate 300
        if int(dec) <= 3:
            while (i <= int(dec)) :
                algarismo += rom[100]
                i = i + 1
        else:
            if int(dec) == 4:
                algarismo = rom[100]  + rom[500]  
            else:
                # 500 
                if int(dec) == 5 : 
                        algarismo = rom[500]
                else:
                    # acima de 50
                    if int(dec) <= 8 :
                        algarismo = rom[500]
                        i = 5
                        while (i < int(dec)) :
                            algarismo += rom[100]
                            i = i + 1                     
                    else:
                        if int(dec) == 9 : 
                            algarismo = rom[100] + rom[1000]

    return algarismo
  
def integerAchaMilhar(dec):
    algarismo = ""
    i = 1
    # se for 1 = 1000
    if int(dec) == 1:
            algarismo = rom[1000]
    else:
        # acima de 1000 ate 3000
        if int(dec) <= 3:
            while (i <= int(dec)) :
                algarismo += rom[1000]
                i = i + 1
        else:
            if int(dec) == 4:
                algarismo = rom[1000]  + rom[5000]
            else:
                # 500
                if int(dec) == 5 :
                        algarismo = rom[5000]
                else:
                    # acima de 50
                    if int(dec) <= 8 :
                        algarismo = rom[5000]
                        i = 5
                        while (i < int(dec)) :
                            algarismo += rom[1000]
                            i = i + 1
                    else:
                        if int(dec) == 9 :
                            algarismo = rom[1000] + rom[10000]

    return algarismo

def  integerToRoman(num):
    saida = "erro";
    numRet = str(num) 
    conp = list(numRet)
   
    # se tem 2 na lista -  decimal
    if len(list(numRet)) == 2 :
        un = int(conp[1])
        algarismo = str(integerAchaDecimal(conp[0]))
        print (algarismo)
        saida = algarismo + rom[un] 

    # se tem 3 na lista - e centena
    if len(list(numRet)) == 3:
        #centena
        saida = integerAchaCentena(conp[0])
        # dezena
        if conp[1] != "0":
            saida += str(integerAchaDecimal(conp[1]))
        # unidade
        if conp[2] != "0":
            saida += rom[int(conp[2])]

    # se tem 4 na lista - e milhar
    if len(list(numRet)) == 4:
        #milhar
        saida = integerAchaMilhar(conp[0])
        #centena
        if conp[1] != "0":
            saida += integerAchaCentena(conp[1])
        # dezena
        if conp[2] != "0":
            saida += str(integerAchaDecimal(conp[2]))
        # unidade
        if conp[3] != "0":
            saida += rom[int(conp[3])]

    #print (saida)
    return saida

print(integerToRoman(2015))