import ast
n=int(input("digite a quantas variavel vai por na lista:"))
i=1
lista=[]
listacod=[]
while i<=n:
    var=input("digite a variavel:")
    try:
        var = ast.literal_eval(var)
    except (ValueError, SyntaxError):
        pass
    tipo=type(var)
    if tipo==int:
        listacod.append(f"(int: {var})")
        lista.append(var)
        print("o tipo da variavel é int")
    elif tipo==float:
        listacod.append(f"(float: {var:.2f},)")
        lista.append(var)
        print("o tipo da variavel é float")
    elif tipo==str:
        listacod.append(f"(str: '{var}')")
        lista.append(var)
        print("o tipo da variavel é string")
    elif tipo==bool:
        listacod.append(f"(bool: {var})")
        lista.append(var)
        print("o tipo da variavel é bool")
    elif tipo==list:
        lista2=[]
        for item in var:
            try:
                item = ast.literal_eval(item)
            except (ValueError, SyntaxError):
                pass
            item_type = type(item)
            if item_type == int:
                lista2.append(f"(int: {item})")
            elif item_type == float:
                lista2.append(f"(float: {item:.2f})")
            elif item_type == str:
                lista2.append(f"(str: '{item}')")
            elif item_type == bool:
                lista2.append(f"(bool: {item})")
            else:
                print("se voce pos uma lista na lista que esta na lista que to fazendo na moral espero que caia um meteora em vc obrigado kkkskssks")
        listacod.append(f"(list: {lista2})")
        lista.append(var)
        print("o tipo da variavel é lista")
    else:
        print ("se tu pos um tipo diferente nao fiz é nois")
    i+=1
print("a lista codificada é:",listacod)
print("a lista descodificada é:",lista)


