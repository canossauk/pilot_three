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



try:
    from frontend.src.styles.colors import *
except ImportError:
    from styles.colors import *

def create_dashboard_content(user_role="Admin") -> ft.Container:
    if user_role == "Student":
        return _create_student_dashboard()
    elif user_role == "Tutor":
        return _create_tutor_dashboard()
    else:
        return _create_admin_dashboard()

def _create_admin_dashboard():
    return ft.Container(
        expand=True,
        padding=40,
        content=ft.Column(
            controls=[
                ft.Text("Administrator Dashboard", size=40, weight=ft.FontWeight.BOLD, color=COLOR_BURGUNDY, font_family="LuxurySerif"),
                ft.Text("Overview of school performance and metrics.", size=18, color=COLOR_DARK),
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

def _create_student_dashboard():
    return ft.Container(
        expand=True,
        padding=40,
        content=ft.Column(
            controls=[
                ft.Text("Student Portal", size=40, weight=ft.FontWeight.BOLD, color=COLOR_BURGUNDY, font_family="LuxurySerif"),
                ft.Text("Welcome back, Student. Here is your academic overview.", size=18, color=COLOR_DARK),
                ft.Divider(height=40, color="transparent"),
                ft.Row(
                    [
                        _create_stat_card("GPA", "3.8", ft.Icons.GRADE),
                        _create_stat_card("Attendance", "95%", ft.Icons.ACCESS_TIME),
                        _create_stat_card("Assignments Due", "3", ft.Icons.ASSIGNMENT_LATE),
                    ],
                    spacing=20
                ),
                ft.Divider(height=20, color="transparent"),
                ft.Text("Upcoming Classes", size=24, weight=ft.FontWeight.BOLD, color=COLOR_DARK),
                ft.Card(
                    content=ft.Container(
                        padding=20,
                        content=ft.Column([
                            ft.ListTile(leading=ft.Icon(ft.Icons.CLASS_), title=ft.Text("Advanced Mathematics"), subtitle=ft.Text("10:00 AM - Room 301")),
                            ft.ListTile(leading=ft.Icon(ft.Icons.CLASS_), title=ft.Text("History of Art"), subtitle=ft.Text("1:00 PM - Room 204")),
                        ])
                    )
                )
            ]
        ),
    )

def _create_tutor_dashboard():
    return ft.Container(
        expand=True,
        padding=40,
        content=ft.Column(
            controls=[
                ft.Text("Tutor Dashboard", size=40, weight=ft.FontWeight.BOLD, color=COLOR_BURGUNDY, font_family="LuxurySerif"),
                ft.Text("Manage your classes and student performance.", size=18, color=COLOR_DARK),
                ft.Divider(height=40, color="transparent"),
                ft.Row(
                    [
                        _create_stat_card("Classes Today", "4", ft.Icons.CLASS_),
                        _create_stat_card("Pending Grades", "12", ft.Icons.ASSIGNMENT_IND),
                        _create_stat_card("Student Alerts", "2", ft.Icons.WARNING_AMBER),
                    ],
                    spacing=20
                ),
                 ft.Divider(height=20, color="transparent"),
                ft.Text("Today's Schedule", size=24, weight=ft.FontWeight.BOLD, color=COLOR_DARK),
                ft.Card(
                    content=ft.Container(
                        padding=20,
                        content=ft.Column([
                            ft.ListTile(leading=ft.Icon(ft.Icons.SCHEDULE), title=ft.Text("Intro to Physics"), subtitle=ft.Text("09:00 AM - 10:30 AM")),
                            ft.ListTile(leading=ft.Icon(ft.Icons.SCHEDULE), title=ft.Text("Chemistry Lab"), subtitle=ft.Text("11:00 AM - 12:30 PM")),
                        ])
                    )
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
