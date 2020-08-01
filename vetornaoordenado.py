# -*- coding: utf-8 -*-
"""VetorNaoOrdenado.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t591ZjSQOffK6MzzxbGVgkpjd6ZYnnuI
"""

import numpy as np

class VetorNaoOrdenado:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = np.empty(self.capacidade, dtype=int)
  
  #O(n)
  def imprime(self):
    if self.ultima_posicao == -1:
      print('O Vetor esta vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, '-', self.valores[i])    
        
  #O(1) - O(2)
  def insere(self, valor):
      if self.ultima_posicao == self.capacidade - 1:
        print('Capacidade máxima atingida')
      else: 
        self.ultima_posicao += 1
        self.valores[self.ultima_posicao] = valor
  
  # O(n)
  def pesquisar(self, valor):
    for i in range(self.ultima_posicao + 1):
      if valor == self.valores[i]:
        return i
    return -1
  
  #O(n)
  def excluir(self, valor):
    posicao = self.pesquisar(valor)
    if posicao == -1:
      return -1
    else:
      for i in range(posicao, self.ultima_posicao):
        self.valores[i] = self.valores[i + 1]

    self.ultima_posicao -= 1

vetor = VetorNaoOrdenado(5)


vetor.insere(2)
vetor.insere(3)
vetor.insere(5)
vetor.insere(4)
vetor.insere(9)

# Erro de capacidade
vetor.insere(7)

vetor.imprime()

vetor.pesquisar(5)

# Valor que não existe
vetor.pesquisar(8)

vetor.excluir(5)
vetor.imprime()

# Valor não encontrado para exclusão
vetor.excluir(10)

vetor.insere(5)
vetor.imprime()

