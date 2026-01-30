import flet as ft
p = ft.Page(None, "")
print("end_drawer annotations:", p.__annotations__.get('end_drawer', 'Not Found'))
# Or just try to assign it in a script
try:
    p.end_drawer = ft.Container()
    print("Success: Assigned Container to end_drawer")
except Exception as e:
    print(f"Error: {e}")
