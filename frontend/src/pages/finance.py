#
#  Import LIBRARIES
import flet as ft
#  Import FILES
#  __________________________________
#

def create_finance_content() -> ft.Container:
    """
    Creates and returns the main dashboard content area.
    """
    return ft.Container(
        expand=True,
        padding=20,
        bgcolor=ft.Colors.BLUE_ACCENT_700,
        content=ft.Column(
            controls=[
                ft.Text(value="Welcome to the Finance Page", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                ft.Text(value="Select an option from the navigation menu.", theme_style=ft.TextThemeStyle.BODY_LARGE),
            ]
        ),
    )
