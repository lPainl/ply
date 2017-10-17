import ply.lex as lex

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS' ]

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer


class Nodo():
    def __init__(self,valor,izq=None,der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

class Pila:
    def __init__(self):
        self.pila=[]        
    def apilar(self,x):
      # funcion para agregar un elemento a la pila
        self.pila.append(x)
      # print "se apilo correctmente"
    def desapilar(self):
      # funcion para eliminar un elemento de la pila
       if (self.pila != []):
      # print "se desapilo"
        return self.pila.pop()
       else: 
        return "Lista vacia"
    

def evaluar(arbol):
    try:
      if(arbol.valor == '+'):
         return (evaluar(arbol.izq) + evaluar(arbol.der))
      if(arbol.valor == '-'):
         return (evaluar(arbol.izq) - evaluar(arbol.der))
      if(arbol.valor == '*'):
         return (evaluar(arbol.izq) * evaluar(arbol.der))
      if(arbol.valor == '/'):
         return (evaluar(arbol.izq) / evaluar(arbol.der))   
      return int(arbol.valor)
    except AttributeError:
      return int(arbol)

def imprimir(arreglo):
    n = 0
   
    while (n < len(arreglo)):
      print (arreglo[n])
      n = n+1

opcion = 1
j = 0
diccionario = []
expresiones = []
archivo = open ("texto.txt","r")

for linea in archivo.readlines():   
   cadena = linea   
   lex.input(cadena)
   lista = cadena.split(" ")
   pila= Pila()
   tam = len(lista)
   i = 0
  
   while(i < tam):
      tok = lex.token()
      if (str(tok.type) != 'NUMBER'):
        if((str(tok.type) == 'PLUS') | (str(tok.type) == 'MINUS') | (str(tok.type) == 'DIVIDE') | (str(tok.type) == 'TIMES')):
           exp = [str(tok.type),lista[i]]
           expresiones.append(exp)
           der = pila.desapilar()
           izq = pila.desapilar()
           nodo = Nodo(lista[i],izq,der) 
           pila.apilar(nodo)
        elif(str(tok.type) == 'EQUALS'):
           exp = [str(tok.type),lista[i]]
           expresiones.append(exp)
           x = [lista[i -1], str(evaluar(pila.desapilar()))]
           diccionario.append(x)
           print ("el resultado de la expresion es: " + diccionario[j][0] + " = " + diccionario[j][1])
        else:
           if (str(tok.type) == 'NAME'):
               exp = ['variable',lista[i]]
               expresiones.append(exp)
               n = 0
               while (n < len(diccionario)):
                   if (diccionario[n][0] == lista[i]):
                       pila.apilar(diccionario[n][1])
                   n = n+1
           else: 
                imprimir(expresiones)
                print ("el token " + lista[i]+" no es valido")
                sys.exit()
      else:
         exp = ['numero',lista[i]]
         expresiones.append(exp)
         
         pila.apilar(lista[i])
      i = i+1
   j = j+1
   

print("proceso terminado")
imprimir(expresiones)


