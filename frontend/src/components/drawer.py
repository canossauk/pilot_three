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
        on_click=on_click_func,
        data=index,
        ink=True,
    )

def create_navigation_drawer(on_nav_selected, user_role="Admin") -> ft.NavigationDrawer:
    menu_items = []

    # Common Header
    controls = [
        ft.Container(
            content=ft.Text("iLa.", size=40, weight=ft.FontWeight.BOLD, color=COLOR_WHITE, font_family="LuxurySerif"),
            padding=ft.Padding.only(left=20, top=40, bottom=20),
        ),
        ft.Divider(color=ft.Colors.with_opacity(0.1, COLOR_WHITE), thickness=1),
    ]

    if user_role == "Admin":
        menu_items = [
            (ft.Icons.DASHBOARD_OUTLINED, "Dashboard"),
            (ft.Icons.FOLDER_OPEN, "Records Management"),
            (ft.Icons.PAYMENTS_OUTLINED, "Bursar/Payments"),
            (ft.Icons.DATA_USAGE, "Resource Allocation"),
        ]
    elif user_role == "Student":
        menu_items = [
            (ft.Icons.DASHBOARD_OUTLINED, "Academic Dashboard"),
            (ft.Icons.SCHEDULE_OUTLINED, "Schedule"),
            (ft.Icons.ASSIGNMENT_OUTLINED, "Assessment Tracker"),
            (ft.Icons.UPLOAD_FILE, "Submission Engine"),
            (ft.Icons.HOW_TO_REG, "Registration"),
        ]
    elif user_role == "Tutor":
        menu_items = [
            (ft.Icons.DASHBOARD_OUTLINED, "Dashboard"),
            (ft.Icons.EVENT_AVAILABLE, "Attendance Module"),
            (ft.Icons.GRADE, "Grading Suite"),
            (ft.Icons.BOOK_OUTLINED, "Curriculum Planner"),
            (ft.Icons.PERSON_SEARCH, "Student Overview"),
        ]
    else:
        # Fallback or default
        menu_items = [
            (ft.Icons.DASHBOARD_OUTLINED, "Dashboard")
        ]

    for idx, (icon, text) in enumerate(menu_items):
        # We'll use the index as the data for now, but in a real app might use a key
        controls.append(_create_drawer_item(icon, text, idx, on_nav_selected))

    return ft.NavigationDrawer(
        bgcolor=COLOR_DRAWER_BG,
        controls=controls,
        indicator_color="transparent",
    )

