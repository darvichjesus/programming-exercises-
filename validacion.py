
def validacion(cadena):
    auxiliar=str("")
    cadena=str(cadena)
    if cadena==str(""):
        return(print("mmgvo"))
    if cadena[0]=="}" or cadena[0]==")" or cadena[0]=="]":
        return (print("Cadena invalida")) 

    for i in range (0,len(cadena)):
        if (len(auxiliar)==0 and cadena[i]==")" ) or (len (auxiliar)==0 and cadena[i]=="]") or (len (auxiliar)==0 and cadena[i]=="}"):
            return(print("Cadena vecino de darvich"))
        if cadena[i]=="(" or cadena[i]=="[" or cadena[i]=="{":
            auxiliar+=cadena[i]
        else:
            if (cadena[i]==")" and auxiliar[len(auxiliar)-1]=="(" ) or (cadena[i]=="]" and auxiliar[len(auxiliar)-1]=="[") or (cadena[i]=="}" and auxiliar[len(auxiliar)-1]=="{"):
                auxiliar=auxiliar[:-1]
            else:
                return (print("Cadena invalida"))
    if len(auxiliar)==0:
        return (print("Cadena valida"))
    else:
        return(print("cadena como el vecino invalido de darvich que se desvivio"))
        
validacion("[[[[]]]]")