# Funções - Fibonacci

O script principal de vocês deve estar no arquivo `main.py`.

## 📝 Instruções

Escreva uma função que recebe um número inteiro `n` como parâmetro e retorna o `n`-ésimo número da sequência de Fibonacci.

O identificador da função deve ser `fibonacci`.

Caso a função receba um número `n < 0` a função deve lançar um erro do tipo `ValueError`.
Para isso basta fazer a instrução `raize ValueError("n tem que ser maior do que zero")`.

## 📌 Exemplos

```python
fibonacci(0) # 0
fibonacci(1) # 1
fibonacci(2) # 1
fibonacci(3) # 2
fibonacci(4) # 3
fibonacci(5) # 5
fibonacci(6) # 8
fibonacci(7) # 13
fibonacci(8) # 21
```

## 🧪 Testes

Para testar o programa você pode executar o seguinte commando no terminal:

```bash
python -m unittest
```

Caso você esteja usando o [VSCode](https://code.visualstudio.com/), você pode abrir a paleta de comandos `CTRL+SHIFT+P` e digitar `Run All Tests`.
