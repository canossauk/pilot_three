import flet as ft
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

# Color Palette
COLOR_BURGUNDY = "#5D1535"
COLOR_DARK = "#1A1A1A"
COLOR_WHITE = "#FFFFFF"
COLOR_BG = "#F5F5F7"
COLOR_SURFACE = "#FFFFFF"

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

    def handle_drawer_change(e):
        selected_index = e.control.selected_index
        set_page(selected_index)
        page.close_end_drawer()

    page.end_drawer = ft.NavigationDrawer(
        on_change=handle_drawer_change,
        selected_index=0,
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

    def open_drawer(e):
        page.end_drawer.open = True
        page.end_drawer.update()

    def create_header():
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
                    ft.IconButton(
                        icon=ft.Icons.MENU,
                        icon_color=COLOR_WHITE,
                        style=ft.ButtonStyle(
                            bgcolor={"": COLOR_BURGUNDY},
                            shape={"": ft.CircleBorder()},
                            padding=15,
                        ),
                        on_click=open_drawer
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
                create_header(),
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
