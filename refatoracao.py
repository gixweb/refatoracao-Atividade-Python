"""
A lógica envolve:
• Verificar se o usuário está ativo
• Aplicar diferentes cálculos com base na categoria do usuário
• Considerar valores e pontos acumulados
• Aplicar ajustes finais dependendo do resultado

por exemplo:
• Cálculo de bônus
• Comissão
• Pontuação
• Benefícios de clientes

a = usuario
b = valorConta
c = valorAcumulado
d = categoria
e = valorReserva
r = resultado
"""

usuario = True
valorConta = 100
valorAcumulado = 50
valorReserva = 70
categoria = "cliente Comum"
resultado = 0

def resultadoContaComum (valorConta, valorAcumulado):
    if valorConta > 50:
        resultado = valorConta * valorAcumulado
    else:
        resultado = valorConta + valorAcumulado
    return resultado

def resultadoContaLuxo (valorReserva, valorConta, valorAcumulado):
    if valorReserva > 100:
        resultado = valorConta * (valorAcumulado + 0.1)
    else:
        resultado = valorConta * valorAcumulado
    return resultado

def resultadoContaPremium(valorReserva, valorConta, valorAcumulado):
    if valorConta > 100 & valorReserva > 50:
        resultado = (valorConta * valorAcumulado) - 20
    else:
        resultado = valorConta
    return resultado

def resultadoCalculo(resultado):
    if resultado > 500:
        resultado = resultado - 30
    return resultado

def procedimento (categoria, resultado, resultadoContaComum, resultadoContaLuxo, resultadoContaPremium):
    match categoria:
        case "cliente Comum":
            resultado = resultadoContaComum(valorConta, valorAcumulado)
            return resultado
        case "cliente Luxo":
            resultado = resultadoContaLuxo(valorReserva, valorConta, valorAcumulado)
            return resultado
        case "cliente Premium":
            resultado = resultadoContaPremium(valorReserva, valorConta, valorAcumulado)
            return resultado
        case " ":
            return "cliente não encontrado"
    
if usuario == True:
    if valorConta > 500:
        resultado = valorConta - 30
    else:
        resultadoConta = procedimento(categoria, resultado, resultadoContaComum, resultadoContaLuxo, resultadoContaPremium)
        resultado = resultadoCalculo(resultadoConta)

print(resultado)
print(usuario)
print(categoria)