def truthTable(expressao,inputs=2):
    expressao = expressao.lower()
  
    expressao = expressao.replace("and","&")
    expressao = expressao.replace("xor","^")
    expressao = expressao.replace("or","|")
    expressao = expressao.replace("not","~")
    valores_v = []


    if inputs==2:
        for a in range(1,-1,-1):
            for b in range(1,-1,-1):
                x = eval(expressao)
                if(x == -1): x = 1
                if(x == -2): x = 0
                valores_v.append(x)
        
    elif inputs==3:
        for a in range(1,-1,-1):
            for b in range(1,-1,-1):
                for c in range(1,-1,-1):
                    x = eval(expressao)
                    if(x == -1): x = 1
                    if(x == -2): x = 0
                    valores_v.append(x)
    
    elif inputs==4:    
        for a in range(1,-1,-1):
            for b in range(1,-1,-1):
                for c in range(1,-1,-1):
                    for d in range(1,-1,-1):
                        x = eval(expressao)
                        if(x == -1): x = 1
                        if(x == -2): x = 0
                        valores_v.append(x)
    return valores_v

expressao1 = "A AND (B OR C)"
expressao2 = "(A AND B) OR (A AND C)"
E1 = truthTable(expressao1,3)
E2 = truthTable(expressao2,3)

print(E1)
print(E2)

if(E1 == E2):
    print("IGUAL")
else:
    print("DIFERENTE")

