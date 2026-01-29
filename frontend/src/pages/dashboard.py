import flet as ft

COLOR_BURGUNDY = "#5D1535"
COLOR_DARK = "#1A1A1A"

def create_dashboard_content() -> ft.Container:
    return ft.Container(
        expand=True,
        padding=40,
        content=ft.Column(
            controls=[
                ft.Text("Dashboard", size=40, weight=ft.FontWeight.BOLD, color=COLOR_BURGUNDY, font_family="LuxurySerif"),
                ft.Text("Welcome to the International Luxury Academy administration portal.", size=18, color=COLOR_DARK),
                ft.Divider(height=40, color="transparent"),
                ft.Row(
                    [
                        _create_stat_card("Total Students", "124", ft.Icons.PEOPLE),
                        _create_stat_card("Active Faculty", "18", ft.Icons.SCHOOL),
                        _create_stat_card("Revenue (YTD)", "$1.2M", ft.Icons.ATTACH_MONEY),
                    ],
                    spacing=20
                )
            ]
        ),
    )

def _create_stat_card(title, value, icon):
    return ft.Container(
        width=250,
        height=150,
        bgcolor="#FFFFFF",
        padding=20,
        content=ft.Column(
            [
                ft.Icon(icon, color=COLOR_BURGUNDY, size=30),
                ft.Text(value, size=30, weight=ft.FontWeight.BOLD, color=COLOR_DARK),
                ft.Text(title, size=14, color=ft.Colors.GREY_600),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )
