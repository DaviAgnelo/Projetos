#Esta função serve para quando o programa termina de criar a
#tabela e pergunta ao usuário se ele quer continuar usando o programa
def end():
    print('Deseja criar outra Tabela?')

    an = input('y para sim e n para não: ')
    y = 'y'
    n = 'n'

    if an == y:
        programa()
    elif an == n:
        print('Obrigado por utilizar o meu programa - Davi Agnelo')
        quit()
    else:
        print('Resposta inválida')
        end()

#Essa parte vai pegar a palavra que o usuário digitou e juntar ao alfabeto
#em seguida ele vai filtrar qualquer letra repetida
def delRepeat(palavra, alfabeto):

    matriz1 = palavra+alfabeto
    matriz2 = ''

    for char in matriz1:
        if char not in matriz2:
            matriz2=matriz2+char
    
    return matriz2;
    
#Essa função separa o alfabeto de delRepeat em colunas e depois organizar essa colunas na ordem alfabética
def coluns(m):
    
    n = 1
    c1 = ''
    c2 = ''
    c3 = ''
    c4 = ''
    c5 = ''
    c6 = ''
    c7 = ''
    c8 = ''
    for char in m:
        if n == 1 or n == 9 or n == 17 or n == 25:
            n=n+1
            c1=c1+char
        elif n == 2 or n == 10 or n == 18 or n == 26:
            n=n+1
            c2=c2+char
        elif n == 3 or n == 11 or n == 19 or n == 27:
            n=n+1
            c3=c3+char
        elif n == 4 or n == 12 or n == 20 or n == 28:
            n=n+1
            c4=c4+char
        elif n == 5 or n == 13 or n == 21 or n == 29:
            n=n+1
            c5=c5+char
        elif n == 6 or n == 14 or n == 22 or n == 30:
            n=n+1
            c6=c6+char
        elif n == 7 or n == 15 or n == 23 or n == 31:
            n=n+1
            c7=c7+char
        elif n == 8 or n == 16 or n == 24 or n == 32:
            n=n+1
            c8=c8+char
        else:
            break
        
    colunas = [c1,c2,c3,c4,c5,c6,c7,c8]
        
    colunas.sort()
        
    return colunas;
    
#Essa função vai juntar a lista de colunas em uma única string
def primeiro_alf(colunas1):
    
    alf1 = ''
    
    return(alf1.join(colunas1));
    
def num_alf(alf1):
    
    n = 1
    n1 = ''
    n2 = ''
    n3 = ''
    n4 = ''
    n5 = ''
    n6 = ''
    n7 = ''
    n8 = ''
    n9 = ''
    
    for char in alf1:
        if n == 1 or n == 10 or n == 19:
            n=n+1
            n1=n1+char
        elif n == 2 or n == 11 or n == 20:
            n=n+1
            n2=n2+char
        elif n == 3 or n == 12 or n == 21:
            n=n+1
            n3=n3+char
        elif n == 4 or n == 13 or n == 22:
            n=n+1
            n4=n4+char
        elif n == 5 or n == 14 or n == 23:
            n=n+1
            n5=n5+char
        elif n == 6 or n == 15 or n == 24:
            n=n+1
            n6=n6+char
        elif n == 7 or n == 16 or n == 25:
            n=n+1
            n7=n7+char
        elif n == 8 or n == 17 or n == 26:
            n=n+1
            n8=n8+char
        elif n == 9 or n == 18 or n == 27:
            n=n+1
            n9=n9+char
        else:
            break
        
    lst = [n1,n2,n3,n4,n5,n6,n7,n8,n9]
            
    return lst;
        
def segundo_alf(alf1):
    
    n=1
    salf = ''
    
    for char in alf1:
        if n < 9:
            n=n+1
            continue
        elif n >= 9:
            n=n+1
            salf=char+salf
        else:
            break
    
    return salf;
    
def autent(nalf1, alf2):
    let1 = input('Escreva a primeira letra de autênticação: ')
    let2 = input('Escreva a segunda letra de autênticação: ')
    print('Ok, vou verificar qual a autenticação.')

    def aut1(let1,nalf1):
        aut1 = 0;
    
        for i, j in enumerate(nalf1):
            if let1 in j:
                aut1 = aut1+i+1
        return aut1;

    def aut2(let2,nalf1):
        aut2 = 0;

        for x, z in enumerate(nalf1):
            if let2 in z:
                aut2 = aut2+x+1
        return aut2;

    au1 = aut1(let1,nalf1)
    au2 = aut2(let2,nalf1)

    def daut(alf2,au1,au2):

        a = au1 + au2 - 1

        return alf2[a]

    autenticador = daut(alf2,au1,au2)

    print(autenticador, autenticador)

    return autenticador;

#Essa é a parte principal do programa, é aqui que são chamadas as outras
#funções e onde o usuário vai interagir com o programa
def programa():
    print('Tabela de Autenticação')
    palavra = input('Escreva uma palavra: ')
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    
    m = delRepeat(palavra, alfabeto)
    
    colunas1 = coluns(m)
    
    alf1 = primeiro_alf(colunas1)
    
    nalf1 = num_alf(alf1)
    
    alf2 = segundo_alf(alf1)
    
    autent(nalf1, alf2)

    def loop():
            ans = input('Deseja fazer outra autenticação?(y ou n) ')
            y = 'y'
            n = 'n'

            while 0 == 0:
                if ans == y:
                    y=''
                    autent(nalf1,alf2)
                elif ans == n:
                    n=''
                    end()
                else:
                    loop()
    
    loop()

programa()