def verificar_ano_bissexto(ano):
  """
  Verifica se um ano é bissexto.

  Args:
    ano: O ano a ser verificado (número inteiro).

  Returns:
    True se o ano for bissexto, False caso contrário.
  """
  if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    return True
  else:
    return False

# --- Exemplo de uso ---
ano_teste = int(input("Digite um ano para verificar se é bissexto: "))

if verificar_ano_bissexto(ano_teste):
  print(f"O ano {ano_teste} é bissexto.")
else:
  print(f"O ano {ano_teste} não é bissexto.")# Escreva o seu código aqui :-)
