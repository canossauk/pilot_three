
import flet as ft
try:
    from frontend.src.styles.colors import *
except ImportError:
    from styles.colors import *

def create_login_page(on_login_success):
    username_field = ft.TextField(label="Username", width=300)
    password_field = ft.TextField(label="Password", password=True, can_reveal_password=True, width=300)
    error_text = ft.Text("", color=ft.Colors.RED, size=14)

    def login_click(e):
        user = username_field.value
        pwd = password_field.value
        
        role = None
        if user == 'admin' and pwd == '12345':
            role = 'Admin'
        elif user == 'Student' and pwd == '67890':
            role = 'Student'
        elif user == 'Tutor' and pwd == '13579':
            role = 'Tutor'

        if role:
            error_text.value = ""
            error_text.update()
            on_login_success(role)
        else:
            error_text.value = "Invalid username or password"
            error_text.update()

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Sign In", size=30, weight=ft.FontWeight.BOLD, font_family="LuxurySerif", color=COLOR_DARK),
                ft.Text("Welcome back to iLa", size=16, color=ft.Colors.GREY_700),
                ft.Container(height=20),
                username_field,
                password_field,
                error_text,
                ft.Container(height=20),
                ft.ElevatedButton("Sign In", on_click=login_click, width=300, bgcolor=COLOR_ACCENT, color=COLOR_WHITE),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
        expand=True,
        bgcolor=COLOR_BG # Ensure background matches
    )
