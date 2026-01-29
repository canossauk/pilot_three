# 
#  Import LIBRARIES
import flet as ft
#  Import FILES

try:
    from frontend.src.styles.colors import *
except ImportError:
    from styles.colors import *

    
#  __________________________
# #




def create_header(on_click_menu) -> ft.Container:
    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Text(
                    "iLa.", 
                    size=40, 
                    weight=ft.FontWeight.BOLD, 
                    color=COLOR_DARK,
                    font_family="LuxurySerif"
                ),
                ft.VerticalDivider(width=20),
                ft.Text(
                    "International Luxury Academy",
                    size=16,
                    color=COLOR_DARK,
                    weight=ft.FontWeight.W_300
                ),
                ft.Container(expand=True),
                ft.IconButton(
                    icon=ft.Icons.MENU,
                    icon_color=COLOR_WHITE,
                    style=ft.ButtonStyle(
                        bgcolor={"": COLOR_BURGUNDY},
                        shape={"": ft.CircleBorder()},
                        padding=15,
                    ),
                    on_click=on_click_menu
                )
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
        padding=ft.padding.symmetric(horizontal=40, vertical=20),
        bgcolor=COLOR_WHITE,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
        )
    )
