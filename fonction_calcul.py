#Calcul de base 

def calcul(a, op, b) :
  #Initialisation de res vide
  res = None
  #Vérification de l'opérateur et fait le calcul adéquat
  match op :
    case ("+") :
      res = a + b
    case ("-") :
      res = a - b 
    case ("*") :
      res = a * b
    case ("/") :
      #Vérification de la divison par 0
      if b == 0 :
        res = "error"
      else :
        res = a / b 
  return res 