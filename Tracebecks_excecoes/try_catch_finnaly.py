try:
    # Código que pode gerar exceções
    resultado = 10 / 0  # Exemplo de código que gera uma exceção de divisão por zero
except ZeroDivisionError:
    # Código a ser executado se uma exceção específica (ZeroDivisionError) ocorrer
    print("Erro: Divisão por zero.")
except Exception as e:
    # Código a ser executado se ocorrer qualquer outra exceção
    print(f"Ocorreu uma exceção: {e}")
finally:
    # Código a ser executado independentemente de exceções
    print("Fim do bloco try-except-finally.")


try:
    num1 = int(input(' primeiro numero'))
    num2 = int(input(' segundo numero'))

except Exception as e: 
    print(f'Erro inesperado {e}')

finally:
    soma = num1+num2

    print(soma)


    
