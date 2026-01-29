import flet as ft
try:
    from frontend.src.client import SchoolClient
except ImportError:
    from client import SchoolClient

# Color Palette (re-defined or imported if we had a shared constants file)
COLOR_BURGUNDY = "#5D1535"
COLOR_DARK = "#1A1A1A"
COLOR_WHITE = "#FFFFFF"

def create_students_view(page: ft.Page, client: SchoolClient):
    # State
    students = []

    # Student Data Table
    students_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("NAME", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("EMAIL", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("MAJOR", weight=ft.FontWeight.BOLD)),
        ],
        rows=[],
        heading_row_color=ft.Colors.with_opacity(0.05, COLOR_BURGUNDY),
        data_row_color={ft.ControlState.HOVERED: ft.Colors.with_opacity(0.02, COLOR_BURGUNDY)},
        border=ft.border.all(0, ft.Colors.TRANSPARENT),
        width=1000, 
    )
    
    async def refresh_students():
        nonlocal students
        students = await client.get_students()
        students_table.rows.clear()
        for s in students:
            students_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(s["id"]))),
                        ft.DataCell(ft.Text(s["name"], weight=ft.FontWeight.W_500)),
                        ft.DataCell(ft.Text(s["email"])),
                        ft.DataCell(ft.Text(s["major"] or "N/A")),
                    ]
                )
            )
        page.update()

    # Add Student Logic
    name_field = ft.TextField(label="Full Name", border=ft.InputBorder.UNDERLINE, color=COLOR_DARK)
    email_field = ft.TextField(label="Email Address", border=ft.InputBorder.UNDERLINE, color=COLOR_DARK)
    major_field = ft.TextField(label="Major/Focus", border=ft.InputBorder.UNDERLINE, color=COLOR_DARK)
    
    async def add_student_click(e):
        if not name_field.value or not email_field.value:
            page.snack_bar = ft.SnackBar(ft.Text("Name and Email are required"))
            page.snack_bar.open = True
            page.update()
            return
            
        result = await client.add_student(name_field.value, email_field.value, major_field.value)
        if result:
            page.snack_bar = ft.SnackBar(ft.Text(f"Student {result['name']} added!"), bgcolor=COLOR_BURGUNDY)
            page.snack_bar.open = True
            name_field.value = ""
            email_field.value = ""
            major_field.value = ""
            await refresh_students()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Failed to add student"), bgcolor=ft.Colors.RED_900)
            page.snack_bar.open = True
        page.update()

    add_student_card = ft.Card(
        elevation=0,
        content=ft.Container(
            padding=30,
            content=ft.Column(
                [
                    ft.Text("Enroll New Talent", size=24, color=COLOR_BURGUNDY, font_family="LuxurySerif"),
                    ft.Divider(height=20, color="transparent"),
                    name_field,
                    email_field,
                    major_field,
                    ft.Divider(height=30, color="transparent"),
                    ft.ElevatedButton(
                        "ADMIT STUDENT",
                        style=ft.ButtonStyle(
                            bgcolor={"": COLOR_BURGUNDY},
                            color={"": COLOR_WHITE},
                            shape=ft.RoundedRectangleBorder(radius=0),
                            padding=20,
                        ),
                        on_click=add_student_click,
                        width=200
                    )
                ],
                spacing=10
            )
        )
    )

    # Content Layout
    content = ft.Row(
        controls=[
            ft.Container(content=add_student_card, width=400, alignment=ft.Alignment.TOP_CENTER),
            ft.VerticalDivider(width=40, color="transparent"),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Current Roster", size=20, weight=ft.FontWeight.BOLD, color=COLOR_BURGUNDY),
                        students_table
                    ]
                ),
                expand=True,
                bgcolor=COLOR_WHITE,
                padding=30,
                border_radius=0, 
            )
        ],
        vertical_alignment=ft.CrossAxisAlignment.START,
        alignment=ft.MainAxisAlignment.CENTER,
    )
    
    # We trigger the initial load
    # Note: Since this function returns the control, we can't await inside it easily without creating a task.
    # We'll attach the data loading to the `did_mount` of the control if possible, or just fire and forget.
    # Flet controls don't strictly have did_mount exposed in the python API easily unless subclassing UserControl.
    # For now, we'll return the content and instructions to load.
    
    # A cleaner way is to wrap this in a UserControl, but to keep it simple with functions:
    # We will trigger the refresh task.
    import asyncio
    asyncio.create_task(refresh_students())
    
    return content
