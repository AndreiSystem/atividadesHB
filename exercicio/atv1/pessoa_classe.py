
class Pessoa:
    def __init__(self, nome, telefone, email, idade):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def telefone(self):
        return self.__telefone

    @property
    def email(self):
        return self.__email

    @property
    def idade(self):
        return self.__idade
