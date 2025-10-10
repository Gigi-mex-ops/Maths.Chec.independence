n1 = int(input()) # No cambies esta línea
n2 = int(input()) # No cambies esta línea
op = input() # No cambies esta línea
result = 0

if op == '+':
    result = n1 + n2
elif op == '-':
    result = n1 - n2
elif op == '*':
    result = n1 * n2 
elif op  == '/':
    result = n1 / n2 

# No cambies la línea de abajo
print(f"result = {result}")

#es una practca que ayuda a memorzar onde va cada operador si ponemos la condicion if