import random

def contem(v, e):
    n = len(v)

    for i in range(n):
        v[i] == e
        return True
    return False

def somar(v):
    s = 0
    n = len(v)

    for i in range(n):
        s += v[i]
    return s

def media(v):
    s = somar(v)
    n = len(v)

    media = s / n
    return media

def maior(v):
    m = v[0]
    n = len(v)

    for i in range(n):
        if v[i] > m:
            m = v[i]
    return m

def menor(v):
    m = v[0]
    n = len(v)
    for i in range(n):
        if v[i] < m:
            m = v[i]
    return m

def ordenado(v):
  x = v[0]
  n = len(v)
  for i in range(n):
    if v[i] > x:
      return True
  return False

def gerar_ord(n):

    vetor = [0] * n
    inferior = -n * 10
    delta = 20
    for i in range(n):
        superior = inferior + delta
        vetor[i] = random.randint(inferior, superior)
        inferior = superior
    return vetor


def gerar(n):

    vetor = [0] * n
    for i in range(n):
        vetor[i] = random.randint(-n * 10, n * 10)
    return vetor
