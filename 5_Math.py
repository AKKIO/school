# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9

@author: YnwrdCreso
"""

"""
Funciones definidas por usuario

Valor Absoluto

        --
        | X >= 0  X
    |X| <
        | X < =  -X
        --
ejemplo.
    Abs_(-5)
"""


def Abs_(x):
    if x < 0:
        x = -x
    return x


"""
Formula general

    ax² + bx + c = 0
                   _______
            -b +-√b² - 4ac
    x1,2 = ----------------
                2a

    ejemplo:
        FormulaGeneral(1, 2, 1)

"""


def FormulaGeneral(a, b, c):
    temp = b ** 2 - 4 * a * c
    if temp >= 0:
        x1 = (-b + temp ** 0.5) / (2 * a)
        x2 = (-b - temp ** 0.5) / (2 * a)
        print("x1 = ", x1)
        print("x2 = ", x2)
    else:
        real = -b / (2 * a)
        imag = Abs_(temp) ** 0.5 / (2 * a)
        print("x1 = ", real, " + ", imag, "i")
        print("x2 = ", real, " - ", imag, "i")


def Maximo3(a, b, c):
    if a > b:
        if a > c:
            print(a, "Es el valor máximo")
        else:
            print(c, "Es el valor máximo")
    else:
        if b > c:
            print(b, "Es el valor máximo")
        else:
            print(c, "Es el valor máximo")


def Clima(temp):
    if temp <= 10:
        print("Se siente Frío")
    elif temp > 10 and temp <= 25:
        print("Se siente agradable")
    else:
        print("Se siente calor")


"""
Uso del FOR y RANGE
Función Factorial

           n
        _______
         |   |
    n! = |     |     r
         |   |
         r = 1
"""


def Factorial(n):
    n = int(n)
    ans = 1
    if n >= 0:
        for r in range(1, n+1):
            ans *= r
    else:
        print("No se puede realizar el factorial de números negativos")
        ans = 0
    return ans


"""
Uso del FOR y RANGE
Función Exponencial

                  x²    x³
    eˣ = 1 + x + --- + --- + ...
                  2!    3!
    Ejemplo:
        Exponencial(x, n)
        Exponencial(1, 100)
"""


def Exponencial(x, n):
    ans = 1.0
    for i in range(1, n+1):
        ans += x ** i / Factorial(i)
    print("el exp(%f) = %f" % (x, ans))
    return(ans)


"""
WHILE
Programa que obtiene el cociente y residuo de la división,
mediante restas

"""


def CocienteResiduo(dividendo, divisor):
    cociente = 0
    residuo = dividendo
    while residuo >= divisor:
        residuo -= divisor
        cociente += 1
    print("Cociente = %d, Residuo %f" % (cociente, residuo))


"""
While
Obtener la media, varianza y desviación estandar, un conjunto
de elementos, al teclear cero se detiene la captura de elementos

Ejemplo
    Estadistica()

"""


def Estadistica():
    sumax = 0.0
    sumax2 = 0.0
    n = 0
    print("Estimación de la media y varianza")
    print("Teclee cero para terminar")
    x = float(input("Valor de x: "))
    minv = x
    maxv = x
    while x != 0.0:
        n += 1
        sumax += x
        sumax2 += x ** 2
        if minv > x:
            minv = x
        elif maxv < x:
            maxv = x
        x = float(input("Valor de x: "))
    media = sumax / n
    varianza = (n * sumax2 - sumax ** 2) / (n * (n - 1))
    dstd = varianza ** 0.5
    print("\tsuma x = %f \tsuma x² = %f" % (sumax, sumax2))
    print("\tn = %d \tmedia = %f" % (n, media))
    print("\tVarianza = %f \tDesviación Std = %f" % (varianza, dstd))
    print("\tRango es: [%f, %f ]" % (minv, maxv))


"""
Arreglos y For
Evaluación de un polinomio en un arreglo
si f(x) = a0 + a1 x + a2 x² + a3 x³ ...
evaluar para un valor de x

ejemplo:
    pol = [5, 8, 2, 3]
    PolEval(pol, x)
"""


def PolEval(pol, x):
    n = len(pol)	 # (len) obtener el tamaño de una lista o arreglo
    ans = 0
    for i in range(n):
        ans += pol[i] * x ** i
    return ans


"""
USO DEL FOR Y LISTAs o arreglos
Función que imprime un polinomio
de la forma f(x) = a0 + a1 x + a2 x² + a3 x³ + ...

ejemplo:
    pol = [5, 8, 2, 3]
    PolPrint(pol)
"""


def PolPrint(pol):
    n = len(pol)	 # tamaño del arreglo
    if n <= 0:
        print("No es un polinomio")
    else:
        if pol[0] != 0 or n == 1:
            print("f(x) = %5.3f" % (pol[0]), end='')
            # (end = '')evita el salto de línea
        else:
            print("f(x) = ", end='')
        for i in range(1, n):
            if i == 1:
                if pol[i] >= 0:
                    print(" + %5.3f X" % (pol[i]), end='')
                else:
                    print(" - %5.3f X" % (-pol[i]), end='')
            else:
                if pol[i] >= 0:
                    print(" + %5.3f X^%d" % (pol[i], i), end='')
                else:
                    print(" - %5.3f X^%d" % (-pol[i], i), end='')
    print()


"""
append uso de la funcion
e inicialización de una lista o arreglo vacio []
Derivada de un polinomio
Ejemplo:
    pol = [5, 8, 2, 3]
    polDeriv(pol)
"""


def PolDeriv(pol):
    n = len(pol)	 # tamaño del polinomio
    pold = []		 # polinomio derivado
    if n <= 1:
        pold.append(0)		# agregando elementos al poliniomio derivado
    else:
        for i in range(n-1):
            pold.append((i+1) * pol[i+1])
    PolPrint(pold)
    return pold


def PolDivSin(apol, xr):
    n = len(apol)
    bpol = []
    if n <= 1:
        print("No es posible realizr la división sintetia")
        bpol.append(0)
    else:
        for i in range(n-1):
            bpol.append(0)
        bpol[-1] = apol[-1]  # asignando la última posición a cada array
        n -= 1
        for i in range(n-2, -1, -1):
            bpol[i] = apol[i+1]+xr*bpol[i+1]
        residuo = apol[0]+xr*bpol[0]
        PolPrint(bpol)
        print("El residuo es : ", residuo)
    return bpol


"""
Número de renglones de una matriz

    ejemplo :
        a = [[1,2,3],[4,5,6]]
        MtxRen(a)
"""


def MtxRen(a):
    return len(a)


"""
Número de columnas de una matriz

    ejemplo :
        a = [[1,2,3],[4,5,6]]
        MtxRen(a)
"""


def MtxCol(a):
    return len(a[0])


"""
Impresión de una matriz
    ejemplo :
    a = [[1, 2, 3], [4, 5, 6]]
    MtxPrint(a)

"""


def MtxPrint(a):
    print()
    Ren = MtxRen(a)
    col = MtxCol(a)
    for r in range(Ren):
        for c in range(col):
            print("\t%5.2f" % (a[r][c]), end='')
        print()


"""
Función que realiza la copia de una matriz lista
"""


def MtxCopy(a):
    mtx = []
    for f in a:
        mtx.append(f[:])
    return mtx


"""
Función matricial que genera una matriz de ceros
"""


def MtxZeros(ren, col):
    mtx = []
    for r in range(ren):
        aux = [0]*col
        mtx.append(aux)
    return mtx


def MtxVal(ren, col, n):
    mtx = []
    for r in range(ren):
        aux = [n]*col
        mtx.append(aux)
    return mtx


"""
Función matriz identidad
"""


def MtxIdentidad(n):
    mtx = MtxZeros(n, n)
    for i in range(n):
        mtx[i][i] = 1
    return mtx


"""
m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[1,2,3],[4,5,6],[7,8,9]]
"""
# Suma de Matrices


def MtxSuma(mtx1, mtx2):
    Col = MtxCol(mtx1)
    Ren = MtxRen(mtx1)
    mtxr = MtxZeros(Ren, Col)

    for r in range(Ren):
        for c in range(Col):
            mtxr[c][r] = mtx1[c][r]+mtx2[c][r]
    return mtxr


# Resta de matrices


def MtxResta(mtx1, mtx2):
    Col = MtxCol(mtx1)
    Ren = MtxRen(mtx1)
    mtxr = MtxZeros(Ren, Col)

    for r in range(Ren):
        for c in range(Col):
            mtxr[c][r] = mtx1[c][r]-mtx2[c][r]
    return mtxr

# multiplicación de Matrices


def MtxMult(mtx1, mtx2):
    Col = MtxCol(mtx1)
    Ren = MtxRen(mtx1)
    mtxr = MtxZeros(Ren, Col)

    for r in range(Ren):
        for m in range(Col):
            for c in range(Ren):
                mtxr[r][m] += mtx1[r][c]*mtx2[c][m]
    return mtxr

# Multiplicación directa


def MtxDirMult(mtx1, mtx2):
    Col = MtxCol(mtx1)
    Ren = MtxRen(mtx1)
    mtxr = MtxZeros(Ren, Col)

    for r in range(Ren):
        for c in range(Col):
            mtxr[c][r] = mtx1[c][r]*mtx2[c][r]
    return mtxr


"""
Operaciones Suma y Resta
    opt 1 para suma
    opt 0 para resta

    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8, 9], [1, 2, 3]]
    C = MtxOpt(A, B, opt)
"""


def MtxOpt(A, B, opt):
    aren = MtxRen(A)
    acol = MtxCol(A)
    bren = MtxRen(B)
    bcol = MtxCol(B)

    if (aren != bren or acol != bcol):
        print("No es posible realizar la suma matricial")
        mtx = MtxZeros(1, 1)
    else:
        mtx = MtxZeros(aren, acol)
        for r in range(aren):
            for c in range(acol):
                if (opt == 1):
                    mtx[r][c] = A[r][c] + B[r][c]
                else:
                    mtx[r][c] = A[r][c] - B[r][c]
    return mtx


"""
Operaciones Suma
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8, 9], [1, 2, 3]]
    C = MtxSuma(A, B)
"""


def MtxSumaC(A, B):
    return MtxOpt(A, B, 1)


"""
Operaciones Resta
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8, 9], [1, 2, 3]]
    C = MtxResta(A, B)
"""


def MtxRestaC(A, B):
    return MtxOpt(A, B, 0)


"""
Operaciones Multiplicación

    A = [[1, 1, 1], [1, 1, 1]]
    B = [[1, 1], [1, 1], [1, 1]]
    C = MtxMult(A, B)
"""


def MtxMultC(A, B):
    aren = MtxRen(A)
    acol = MtxCol(A)
    bren = MtxRen(B)
    bcol = MtxCol(B)
    if (acol != bren):
        print("No se puede realizar la multiplicación matricial")
        mtx = MtxZeros(1, 1)
    else:
        mtx = MtxZeros(aren, bcol)
        for r in range(aren):
            for c in range(bcol):
                for k in range(bren):
                    mtx[r][c] = mtx[r][c] + A[r][k] * B[k][c]
                    print(r, c, k)
    return mtx


"""
Recursividad
Es una fucnión que se manda a llamar a si misma
y debe contar con un caso base

"""


def FactorialRecursivo(n):
    factor = 1
    if n < 0:
        print("Math Error")
    elif n == 0 or n == 1:
        factor = 1  # caso base
        print("Ingreso al caso base")
    else:
        factor = n * FactorialRecursivo(n-1)
        print("Obteniendo el factorial de ", n-1)
    return factor


"""
Cofactor

    A = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    MtxPrint(MtxCofactor(A,2,2))
"""


def MtxCofactor(A, ren, col):
    aren = MtxRen(A)
    acol = MtxCol(A)
    if aren != acol or aren == 1 or acol == 1 or ren >= aren or col >= acol:
        print("No es posible obtener el cofactor")
        mtx = MtxZeros(1, 1)
    else:
        mtx = MtxZeros(aren-1, acol-1)
        rmtx = 0
        for r in range(aren):
            cmtx = 0
            for c in range(acol):
                if r != ren and c != col:
                    mtx[rmtx][cmtx] = A[r][c]
                    cmtx += 1
            if r != ren:
                rmtx += 1
    return mtx
