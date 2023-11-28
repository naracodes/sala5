def mostrarNumero():
  numero_valido=False;

  print("Digite um número maior que 0 e menor que 100:");
  while(numero_valido==False):
    try:
      num = int(input());
      if num < 0:
        print("o número deve ser maior que 0");
      elif num>100:
        print("o numero dever menor que 100");
      else:
        print("vodê escolheu o numero correto");
        numero_valido=True;
    except:
      print("o valor deve ser um número ")
  return();

def testarPar():
  numero_valido=False;

  print("Digite um número inteiro par, maior que 0:");
  while(numero_valido==False):
    try:
      num = int(input());
      if num < 0:
        print("o número deve ser maior que 0");
      else:
        print("vodê escolheu o numero correto");
        numero_valido=True;
    except:
      print("o valor deve ser um número ")
  return();

def testarMultiplo():
  numero_valido=False;

  print("Digite um número inteiro par, maior que zero e divisível por 3:");
  while(numero_valido==False):
    try:
      num = int(input());
      if num < 0:
        print("o número deve ser maior que 0");
      elif (num%2!=0) or (num%3!=0):
        print("você deve digitar um número par e divisível por 3")
      else:
        print("vodê escolheu o numero correto");
        numero_valido=True;
    except:
      print("o valor deve ser um número ")
  return();

mostrarNumero();
testarPar();
testarMultiplo();