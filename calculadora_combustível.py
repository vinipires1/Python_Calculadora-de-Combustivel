class CalculadoraCombustivel():
  def __init__(self, km, litro):
    self.km = km,
    self.litro = litro

  def calcula_ctradicional(self, km, litro):
    soma = km / litro
    return soma

  def calcula_importado(self, km, litro):
    soma = 100 / litro
    return soma

#Inputs#
print('#### SEJA VEM VINDO ####')
a = input('Digite o tipo do carro (tradicional ou importado): ')
if a == 'tradicional':
  litro = int(input('Digite a quantidade (litros) total de combustível do carro: '))
  km = float(input('Digite a quantidade de KM percorrido:'))
else: 
  litro = int(input('Digite a quantidade (litros) total de combustível do carro: '))

#Outputs#
x = CalculadoraCombustivel(km, litro)
if a == 'tradicional':
  result_tradicional = print(f'{km} / {litro} = O seu carro está fazendo {x.calcula_ctradicional(km, litro):.1f} km/l')
else:
  result_importado = print(f'{km} / {litro} = O seu carro está fazendo {x.calcula_importado(km, litro):.1f} km/l')