# 
#  Import LIBRARIES
import flet as ft
#  Import FILES

try:
    from frontend.src.client import SchoolClient
except ImportError:
    from client import SchoolClient

# Imports for pages
# Assuming simple layout for now, importing generators
try:
    from frontend.src.pages.dashboard import create_dashboard_content
    from frontend.src.pages.students import create_students_view
except ImportError:
    from pages.dashboard import create_dashboard_content
    from pages.students import create_students_view
# We can import others as needed or use placeholders for now


#  __________________________
# #



# Color Palette
try:
    from frontend.src.styles.colors import *
except ImportError:
    from styles.colors import *

async def main(page: ft.Page):
    page.title = "iLa - International Luxury Academy"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.bgcolor = COLOR_BG
    
    page.fonts = {
        "LuxurySerif": "Playfair Display",
        "LuxurySans": "Lato",
    }
    
    client = SchoolClient()

    # Main Content Area
    content_area = ft.Container(expand=True)

    def set_page(index):
        content_area.content = None
        if index == 0: # Dashboard
            content_area.content = create_dashboard_content()
        elif index == 2: # Students
            content_area.content = create_students_view(page, client)
        else:
            # Placeholder for others
            content_area.content = ft.Container(
                alignment=ft.alignment.center,
                content=ft.Column(
                    [
                        ft.Icon(ft.Icons.CONSTRUCTION, size=50, color=ft.Colors.GREY_400),
                        ft.Text("This module is under development.", color=ft.Colors.GREY_600)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        page.update()

    # --- Drawer ---
    try:
        from frontend.src.components.drawer import create_navigation_drawer
    except ImportError:
        from components.drawer import create_navigation_drawer

    def handle_drawer_change(e):
        selected_index = e.control.selected_index
        set_page(selected_index)
        # Close the drawer
        page.end_drawer.open = False
        page.update()

    page.end_drawer = create_navigation_drawer(handle_drawer_change)

    def open_drawer(e):
        page.end_drawer.open = True
        page.update()

    # --- Header ---
    try:
        from frontend.src.components.header import create_header
    except ImportError:
        from components.header import create_header

    # Layout Assembly
    hero_section = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Administration", size=60, font_family="LuxurySerif", color=COLOR_DARK),
                ft.Text("Select a module from the menu to begin.", size=18, color=ft.Colors.GREY_700),
            ]
        ),
        padding=ft.padding.only(left=80, top=60, bottom=40),
    )

    page.add(
        ft.Column(
            [
                create_header(open_drawer),
                hero_section,
                content_area
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )
    )

    # Initialize with Dashboard
    set_page(0)

if __name__ == "__main__":
    ft.app(target=main)
