from models import Loja, Motoboy, Pedido


LOJAS = [
    Loja(nome="Loja 1", comissao_por_entrega=0.05),
    Loja(nome="Loja 2", comissao_por_entrega=0.05),
    Loja(nome="Loja 3", comissao_por_entrega=0.15),
]

PEDIDOS = [
    Pedido("Pedido 1", valor=50, loja=LOJAS[0]),
    Pedido("Pedido 2", valor=50, loja=LOJAS[0]),
    Pedido("Pedido 3", valor=50, loja=LOJAS[0]),
    Pedido("Pedido 4", valor=50, loja=LOJAS[1]),
    Pedido("Pedido 5", valor=50, loja=LOJAS[1]),
    Pedido("Pedido 6", valor=50, loja=LOJAS[1]),
    Pedido("Pedido 7", valor=50, loja=LOJAS[1]),
    Pedido("Pedido 8", valor=50, loja=LOJAS[2]),
    Pedido("Pedido 9", valor=50, loja=LOJAS[2]),
    Pedido("Pedido 10", valor=100, loja=LOJAS[2]),
]


MOTOBOYS = [
    Motoboy(nome="Moto 1", valor_fixo=2, exclusividade=None),
    Motoboy(nome="Moto 2", valor_fixo=2, exclusividade=None),
    Motoboy(nome="Moto 3", valor_fixo=2, exclusividade=None),
    Motoboy(nome="Moto 4", valor_fixo=2, exclusividade=[LOJAS[0]]),
    Motoboy(nome="Moto 5", valor_fixo=3, exclusividade=None),
]


def atribuir_pedidos(motoboys: list):
    # Iterar sobre os pedidos e atribuir aos motoboys
    for pedido in PEDIDOS:
        motoboy_disponivel = None

        for motoboy in motoboys:
            if motoboy.exclusividade and pedido.loja in motoboy.exclusividade:
                motoboy_disponivel = motoboy
                break
            elif not motoboy_disponivel or len(motoboy.pedidos) < len(
                motoboy_disponivel.pedidos
            ):
                motoboy_disponivel = motoboy

        if motoboy_disponivel:
            motoboy_disponivel.pedidos.append(pedido)


atribuir_pedidos(MOTOBOYS)
# Para rodar passando um motoboy:
# atribuir_pedidos([MOTOBOYS[0]])
# Calcular ganhos e exibir resultados
for motoboy in MOTOBOYS:
    total_pedidos = len(motoboy.pedidos)
    total_ganho = motoboy.calcular_comissao()

    if total_pedidos > 0:
        print(f"Motoboy: {motoboy.nome}")
        print(f"Total de pedidos: {total_pedidos}")
        print(f"Ganhos totais: R$ {total_ganho:.2f}")
        print("Lojas:")
        for pedido in motoboy.pedidos:
            print(f"{pedido.nome} - {pedido.loja}")
        print("=" * 30)
