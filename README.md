[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/PqHvR8Ro)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10997485&assignment_repo_type=AssignmentRepo)
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
