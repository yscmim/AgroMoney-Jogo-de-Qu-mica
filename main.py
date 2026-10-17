import flet as ft


def main(page: ft.Page):
    page.title = "AgroMoney"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F3F7EF"
    page.padding = 24
    page.window_width = 430
    page.window_height = 720
    page.window_min_width = 320
    page.window_min_height = 580
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    jogador = {"nome": "", "saude": 10, "contaminacao": 0, "moedas": 20}

    nome = ft.TextField(
        label="Nome do jogador",
        hint_text="Digite o nome",
        prefix_icon=ft.Icons.PERSON,
        border_radius=12,
        filled=True,
        bgcolor="white",
        on_change=lambda e: jogador.update(nome=e.control.value),
    )

    def valor_texto(chave):
        return ft.Text(
            str(jogador[chave]),
            size=30,
            weight=ft.FontWeight.BOLD,
            color="#203B2B",
            width=72,
            text_align=ft.TextAlign.CENTER,
        )

    valores = {
        "saude": valor_texto("saude"),
        "contaminacao": valor_texto("contaminacao"),
        "moedas": valor_texto("moedas"),
    }

    def alterar(chave, delta):
        jogador[chave] = max(0, jogador[chave] + delta)
        valores[chave].value = str(jogador[chave])
        page.update()

    def painel(titulo, chave, emoji, descricao):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(emoji, size=28),
                        width=52,
                        height=52,
                        alignment=ft.alignment.center,
                        bgcolor="#EAF2E4",
                        border_radius=14,
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(titulo, size=17, weight=ft.FontWeight.BOLD, color="#203B2B"),
                            ft.Text(descricao, size=12, color="#718071"),
                        ],
                        spacing=2,
                        expand=True,
                    ),
                    ft.IconButton(
                        icon=ft.Icons.REMOVE_CIRCLE_OUTLINE,
                        icon_color="#477254",
                        icon_size=28,
                        tooltip=f"Diminuir {titulo.lower()}",
                        on_click=lambda e: alterar(chave, -1),
                    ),
                    valores[chave],
                    ft.IconButton(
                        icon=ft.Icons.ADD_CIRCLE,
                        icon_color="#2F7D46",
                        icon_size=30,
                        tooltip=f"Aumentar {titulo.lower()}",
                        on_click=lambda e: alterar(chave, 1),
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=4,
            ),
            padding=14,
            bgcolor="white",
            border_radius=18,
            border=ft.border.all(1, "#E2EADF"),
        )

    def zerar_valores(e):
        jogador["saude"] = 10
        jogador["contaminacao"] = 0
        jogador["moedas"] = 20
        for chave in valores:
            valores[chave].value = str(jogador[chave])
        page.update()

    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("🌱 AgroMoney", size=30, weight=ft.FontWeight.BOLD, color="#245C35"),
                    ft.Text("Controle do jogador", size=15, color="#718071"),
                ],
                spacing=4,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=ft.padding.only(bottom=16, top=8),
        ),
        nome,
        ft.Container(height=4),
        painel("Saúde", "saude", "❤️", "Nível de saúde"),
        painel("Contaminação", "contaminacao", "☣️", "Nível de contaminação"),
        painel("Moedas", "moedas", "🪙", "Moedas disponíveis"),
        ft.Container(height=8),
        ft.OutlinedButton(
            "Restaurar valores iniciais",
            icon=ft.Icons.RESTART_ALT,
            on_click=zerar_valores,
            style=ft.ButtonStyle(
                color="#477254",
                side=ft.BorderSide(1, "#B8CDB8"),
                shape=ft.RoundedRectangleBorder(radius=12),
                padding=14,
            ),
        ),
        ft.Text(
            "Os valores começam em Saúde 10, Contaminação 0 e Moedas 20. "
            "Você pode alterar esses valores no código.",
            size=11,
            color="#718071",
            text_align=ft.TextAlign.CENTER,
        ),
    )


ft.app(target=main)
