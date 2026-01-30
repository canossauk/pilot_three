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
        padding=40,
        content=ft.Column(
            controls=[
                ft.Text("Financial Overview", size=40, weight=ft.FontWeight.BOLD, color="#5D1535", font_family="LuxurySerif"),
                ft.Text("Select an option from the navigation menu.", size=18, color="#1A1A1A"),
            ]
        ),
    )
