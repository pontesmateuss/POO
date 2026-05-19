def tentativa():
        try:
            print(10 / 0)

        except ZeroDivisionError:
            print("Não é possível dividir por zero")

        else:
            print("Tudo ocorreu corretamente")

        finally:
            print("Fim do programa")

tentativa()
