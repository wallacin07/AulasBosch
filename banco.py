class Conta:
    def __init__(self, saldo: int,conta:int,agencia: int,banco: str):
        self._saldo = saldo
        self._conta = conta
        self._agencia = agencia
        self._banco = banco

    def verSaldo(self):
        return self._saldo
    
    def fecharConta(self):
        print("Conta fechada")
    
    def fazerSaque(self):
        money = int(input("Digite a quantidade que deseja retirar"))
        try:
            if money > self._saldo:
                raise ValueError
            self._saldo - money
            print("Saque realizado com sucesso")
            return 
        except ValueError:
            print('Valor incorreto, tente novamente outro valor')

    def fazerDeposito(self):
        money = int(input("Digite a quantidade que deseja depositar"))
        try:
            if money < 0:
                raise ValueError
            print("Depósito realizado com sucesso")
            return self._saldo + money
        except ValueError:
            print('Valor menor que zero, por favor insira um valor valido')

conta1 = Conta(0,2596,40002,'Itau')
while True:
    menu = int(input("Voce quer acessar qual opção?\n1 - ver saldo"))