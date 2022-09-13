class Elogio:
  listaElogio = []
  
  def __init__(self):
    self.listaElogio = []
  
  def adicionar(self, value):
    self.listaElogio.append(value)
 
  def mostrarListaElogio(self):
    for i in range(len(self.listaElogio)):
        print(f'{i + 1} - {self.listaElogio[i]}')
    print('{}FIM DA LISTA{}'.format('\033[1;34m', '\033[m'))
  
  def excluirItemListaElogio(self, position):
    del(self.listaElogio[position - 1])

  def apagarListaElogio(self):
    self.listaElogio.clear()