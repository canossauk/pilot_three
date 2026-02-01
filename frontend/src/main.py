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
    from frontend.src.pages.faculty import create_faculty_content
    from frontend.src.pages.staff import create_staff_content
    from frontend.src.pages.finance import create_finance_content
    from frontend.src.pages.crm import create_crm_content
except ImportError:
    from pages.dashboard import create_dashboard_content
    from pages.students import create_students_view
    from pages.faculty import create_faculty_content
    from pages.staff import create_staff_content
    from pages.finance import create_finance_content
    from pages.crm import create_crm_content
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

    # --- Login & Navigation Logic ---
    current_user_role = None

    try:
        from frontend.src.pages.login import create_login_page
    except ImportError:
        from pages.login import create_login_page

    # --- Drawer ---
    try:
        from frontend.src.components.drawer import create_navigation_drawer
    except ImportError:
        from components.drawer import create_navigation_drawer

    drawer_open = False

    async def on_nav_selected(e):
        nonlocal drawer_open
        index = e.control.data
        set_page(index)
        # Close the drawer
        await page.close_end_drawer()
        drawer_open = False
        page.update()

    def handle_drawer_dismiss(e):
        nonlocal drawer_open
        drawer_open = False

    async def open_drawer(e):
        nonlocal drawer_open
        if drawer_open:
            await page.close_end_drawer()
            drawer_open = False
        else:
            await page.show_end_drawer()
            drawer_open = True
        page.update()

    # --- Header ---
    try:
        from frontend.src.components.header import create_header
    except ImportError:
        from components.header import create_header

    # Layout Assembly for Authenticated View
    def create_layout():
        hero_section = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(f"{current_user_role} Portal", size=60, font_family="LuxurySerif", color=COLOR_DARK),
                    ft.Text("Select a module from the menu to begin.", size=18, color=ft.Colors.GREY_700),
                ]
            ),
            padding=ft.Padding.only(left=80, top=60, bottom=40),
        )

        return ft.Column(
            [
                create_header(open_drawer),
                hero_section,
                content_area
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )

    def set_page(index):
        content_area.content = None
        
        # Mapping based on Role and Index
        # This is a basic mapping, for a real app we might want a configuration dict
        
        target_content = None

        if current_user_role == "Admin":
            if index == 0: target_content = create_dashboard_content() # Dashboard
            elif index == 1: target_content = None # Records Management
            elif index == 2: target_content = create_finance_content() # Bursar/Payments (Mapping to Finance for now)
            elif index == 3: target_content = None # Resource Allocation

        elif current_user_role == "Student":
            if index == 0: target_content = create_dashboard_content() # Academic Dashboard
            elif index == 1: target_content = None # Schedule
            elif index == 2: target_content = None # Assessment Tracker
            elif index == 3: target_content = None # Submission Engine
            elif index == 4: target_content = None # Registration

        elif current_user_role == "Tutor":
            if index == 0: target_content = create_dashboard_content() # Dashboard
            elif index == 1: target_content = None # Attendance Module
            elif index == 2: target_content = None # Grading Suite
            elif index == 3: target_content = None # Curriculum Planner
            elif index == 4: target_content = create_students_view(page, client) # Student Overview (Mapping to Students)

        if target_content:
            content_area.content = target_content
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

    def on_login_success(role):
        nonlocal current_user_role
        current_user_role = role
        
        # Re-initialize drawer with new role
        page.end_drawer = create_navigation_drawer(on_nav_selected, user_role=role)
        page.end_drawer.on_dismiss = handle_drawer_dismiss
        
        # Switch to main layout
        page.clean()
        page.add(create_layout())
        
        # Load default page (Dashboard)
        set_page(0)

    # Initial State: Login Page
    page.add(create_login_page(on_login_success))

if __name__ == "__main__":
    ft.run(main)
    
