tem_alta_renda = True
tem_bom_credito = False
tem_historico_criminal = False

if tem_alta_renda and not tem_historico_criminal:
    print("Elegível para empréstimo!")