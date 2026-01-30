import flet as ft

def main(page: ft.Page):
    print("Page attributes:", dir(page))
    ns = ft.NavigationDrawer()
    print("NavigationDrawer attributes:", dir(ns))
    page.window_close()

ft.app(target=main)
