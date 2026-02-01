
import flet as ft
try:
    from frontend.src.styles.colors import *
except ImportError:
    from styles.colors import *

def create_login_page(on_login_success):
    username_field = ft.TextField(
        label="Username",
        width=350,
        text_size=14,
        border_color=COLOR_BURGUNDY,
        cursor_color=COLOR_BURGUNDY,
        color=COLOR_DARK
    )
    password_field = ft.TextField(
        label="Password",
        password=True,
        can_reveal_password=True,
        width=350,
        text_size=14,
        border_color=COLOR_BURGUNDY,
        cursor_color=COLOR_BURGUNDY,
        color=COLOR_DARK
    )
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

    # Background Image
    background_image_src = "/home/emagnu/edu/antigravity/xandros/pilot_three/frontend/src/assets/login_ila.jpg"

    login_form_container = ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    content=ft.Text("iLa.", size=60, weight=ft.FontWeight.BOLD, font_family="LuxurySerif", color=COLOR_BURGUNDY),
                    margin=ft.margin.only(bottom=10)
                ),
                ft.Text("International Luxury Academy", size=18, font_family="LuxurySans", color=ft.Colors.GREY_900),
                ft.Container(height=40),
                ft.Text("Log In", size=30, weight=ft.FontWeight.BOLD, font_family="LuxurySerif", color=COLOR_DARK),
                ft.Text("Access your personal dashboard", size=16, color=ft.Colors.GREY_800),
                ft.Container(height=30),
                username_field,
                ft.Container(height=10),
                password_field,
                ft.Container(height=10),
                error_text,
                ft.Container(height=30),
                ft.ElevatedButton(
                    "Log In",
                    on_click=login_click,
                    width=350,
                    height=50,
                    style=ft.ButtonStyle(
                        bgcolor=COLOR_BURGUNDY,
                        color=COLOR_WHITE,
                        shape=ft.RoundedRectangleBorder(radius=5),
                        text_style=ft.TextStyle(size=16, weight=ft.FontWeight.BOLD)
                    )
                ),
                ft.Container(height=20),
                ft.Text("Forgot your password? Contact Administration.", size=12, color=ft.Colors.GREY_700)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        padding=40,
        alignment=ft.Alignment.CENTER,
        bgcolor=ft.Colors.with_opacity(0.85, COLOR_BG), # Add some opacity to the card itself if needed, or keep opaque
        border_radius=10,
        width=450 # Restrict width for better look on large bg
    )

    return ft.Stack(
        controls=[
            ft.Image(
                src=background_image_src,
                fit=ft.BoxFit.COVER,
                expand=True,
                opacity=0.4 # Faded opacity as requested
            ),
            ft.Container(
                content=login_form_container,
                alignment=ft.Alignment.CENTER,
                expand=True
            )
        ],
        expand=True
    )
