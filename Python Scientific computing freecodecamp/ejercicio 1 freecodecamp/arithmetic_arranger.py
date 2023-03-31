def build(s1,s2,oper,ls1,ls2,dif):
  top = []
  botton = []
  line = []
  resultado = []
  dif = " " * dif
  if(ls1 > ls2):
    top.append(f"  {s1}    ")
    botton.append(f"{oper} {dif}{s2}    ")
    line.append("-"*ls1+ "--    ")
    ll = len("-"*ls1+ "--    ") - 4 #lenght of the line
  elif(ls1 < ls2):
    top.append(f"  {dif}{s1}    ")
    botton.append(f"{oper} {s2}    ")
    line.append("-"*ls2+ "--    ")
    ll = len("-"*ls2+ "--    ") - 4#lenght of the line
  else:
    top.append(f"  {s1}    ")
    botton.append(f"{oper} {s2}    ")
    line.append("-"*ls1+ "--    ")
    ll = len("-"*ls1+ "--    ") - 4 #lenght of the line

  if oper == "+":
    suma = int(s1)+int(s2)
    lsuma = len(str(suma))
    resultado.append(" "*abs((ll-lsuma)) + str(suma) + "    ")
  else:
    resta = int(s1)-int(s2)
    lsuma = len(str(resta))
    resultado.append(" "*abs((ll-lsuma)) + str(resta) + "    ")

def draw(top, botton, line, resultado,sresults):
  for item in top:
    print(item, end="")
  print("")
  for item in botton:
    print(item, end="")
  print("")
  for item in line:
    print(item, end="")
  print("")
  if sresults:
        for item in resultado:
            print(item, end="")



def arithmetic_arranger(problems, sresults=False):
  top = []
  botton = []
  line = []
  resultado = []
  problems = list(problems) 
  if len(problems) > 5:       #error handling number 1
    return "Error: Too many problems."
  for operation in problems:
    index = 0
    oper = ""
    operation.split()
    
    if "*" in operation or "/" in operation: #error handling number 2   
     return "Error: Operator must be '+' or '-'."

    try:
     index = operation.index("+")
     oper = "+"
    except: 
     index = operation.index("-")
     oper = "-"
  # next i retrive important data for the drawing
  # s1: the first number, ls1: lenght of first number,(same for s2,ls2), 
  # dif: lenght difference between both numbers
  # then i call "build()" which makes lists for later draw with "draw()" func
    s1 = operation[:index-1]
    s2 = operation[index+2:]
    try:                #error handling number 3
     int(s1)
     int(s2)
    except:
     return "Error: Numbers must only contain digits."
    ls1 = len(s1)
    ls2 = len(s2) 
    if ls1>4 or ls2>4:  #error handling number 4
     return "Error: Numbers cannot be more than four digits."
    dif = abs(ls1 - ls2)
    dif = " " * dif
    if(ls1 > ls2):
        top.append(f"  {s1}    ")
        botton.append(f"{oper} {dif}{s2}    ")
        line.append("-"*ls1+ "--    ")
        ll = len("-"*ls1+ "--    ") - 4 #lenght of the line
    elif(ls1 < ls2):
        top.append(f"  {dif}{s1}    ")
        botton.append(f"{oper} {s2}    ")
        line.append("-"*ls2+ "--    ")
        ll = len("-"*ls2+ "--    ") - 4#lenght of the line
    else:
        top.append(f"  {s1}    ")
        botton.append(f"{oper} {s2}    ")
        line.append("-"*ls1+ "--    ")
        ll = len("-"*ls1+ "--    ") - 4 #lenght of the line

    if oper == "+":
        suma = int(s1)+int(s2)
        lsuma = len(str(suma))
        resultado.append(" "*abs((ll-lsuma)) + str(suma) + "    ")
    else:
        resta = int(s1)-int(s2)
        lsuma = len(str(resta))
        resultado.append(" "*abs((ll-lsuma)) + str(resta) + "    ")

  if sresults:
    retorno = f'{"".join(top).rstrip()}\n{"".join(botton).rstrip()}\n{"".join(line).rstrip()}\n{"".join(resultado).rstrip()}'
  else:
    retorno = f'{"".join(top).rstrip()}\n{"".join(botton).rstrip()}\n{"".join(line).rstrip()}'
  return retorno

