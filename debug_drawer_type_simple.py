import flet as ft
print("Page end_drawer annotation:", ft.Page.__annotations__.get('end_drawer', 'Not Found'))
try:
    # Just check if property setter logic explicitly forbids it by reading source or docs?
    # Actually, let's just create a dummy object that behaves like a Page? No, strictly annotations.
    pass
except:
    pass
