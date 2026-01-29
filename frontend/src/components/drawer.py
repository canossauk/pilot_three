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



def create_navigation_drawer(on_change_func) -> ft.NavigationDrawer:
    return ft.NavigationDrawer(
        on_change=on_change_func,
        selected_index=0,
        bgcolor=COLOR_WHITE,
        controls=[
            ft.Container(
                content=ft.Text("iLa.", size=30, weight=ft.FontWeight.BOLD, color=COLOR_BURGUNDY, font_family="LuxurySerif"),
                padding=ft.padding.only(left=20, top=20, bottom=20),
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.DASHBOARD_OUTLINED, 
                selected_icon=ft.Icons.DASHBOARD, 
                label="Dashboard"
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.SCHOOL_OUTLINED, 
                selected_icon=ft.Icons.SCHOOL, 
                label="Faculty"
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.PEOPLE_OUTLINE, 
                selected_icon=ft.Icons.PEOPLE, 
                label="Students"
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.ASSIGNMENT_IND_OUTLINED,
                selected_icon=ft.Icons.ASSIGNMENT_IND, 
                label="Staff"
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.ATTACH_MONEY_OUTLINED, 
                selected_icon=ft.Icons.ATTACH_MONEY, 
                label="Finance"
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.CONTACTS_OUTLINED, 
                selected_icon=ft.Icons.CONTACTS, 
                label="CRM"
            ),
        ],
        indicator_color=ft.Colors.with_opacity(0.1, COLOR_BURGUNDY),
    )
