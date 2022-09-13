class Reclamacao:
  listaReclamacao = []

  def __int__(self):
     self.listaReclamacao = []

  def adicionar(self, value):
    self.listaReclamacao.append(value)
    
  def mostrarListaReclamacao (self):
    for i in range(len(self.listaReclamacao)):
        print(f'{i + 1} - {self.listReclamacao[i]}')
    print('{}FIM DA LISTA{}'.format('\033[1;34m', '\033[m'))


  def excluirItemListaReclamacao(self, position):
    del(self.listaReclamacao[position - 1])

  def apagarListaReclamacao(self):
    self.listaReclamacao.clear()