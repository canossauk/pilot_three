import flet as ft
try:
    from frontend.src.styles.colors import *
except ImportError:
    from styles.colors import *

def _create_drawer_item(icon, text, index, on_click_func):
    return ft.Container(
        content=ft.Row(
            [
                ft.Icon(icon, color=COLOR_WHITE, size=28),
                ft.Text(text, color=COLOR_WHITE, size=20, weight=ft.FontWeight.W_500), # Bigger font
            ],
            spacing=20,
        ),
        padding=ft.Padding.symmetric(horizontal=20, vertical=15),
        on_click=lambda e: on_click_func(index),
        ink=True,
    )

def create_navigation_drawer(on_nav_selected) -> ft.NavigationDrawer:
    return ft.NavigationDrawer(
        bgcolor=COLOR_DRAWER_BG,
        controls=[
            ft.Container(
                content=ft.Text("iLa.", size=40, weight=ft.FontWeight.BOLD, color=COLOR_WHITE, font_family="LuxurySerif"),
                padding=ft.Padding.only(left=20, top=40, bottom=20),
            ),
            # Divider or spacer if needed
            ft.Divider(color=ft.Colors.with_opacity(0.1, COLOR_WHITE), thickness=1),
            
            _create_drawer_item(ft.Icons.DASHBOARD_OUTLINED, "Dashboard", 0, on_nav_selected),
            _create_drawer_item(ft.Icons.SCHOOL_OUTLINED, "Faculty", 1, on_nav_selected),
            _create_drawer_item(ft.Icons.PEOPLE_OUTLINE, "Students", 2, on_nav_selected),
            _create_drawer_item(ft.Icons.ASSIGNMENT_IND_OUTLINED, "Staff", 3, on_nav_selected),
            _create_drawer_item(ft.Icons.ATTACH_MONEY_OUTLINED, "Finance", 4, on_nav_selected),
            _create_drawer_item(ft.Icons.CONTACTS_OUTLINED, "CRM", 5, on_nav_selected),
        ],
        indicator_color="transparent", # Disable standard indicator as we use custom items
    )
