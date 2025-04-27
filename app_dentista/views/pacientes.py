import flet as ft

def HomeView(page: ft.Page):
    page.bgcolor = ft.colors.LIGHT_BLUE_50  # Fondo aún más claro para pacientes
    page.title = "DentistaApp - Pacientes"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Título principal
    titulo = ft.Text(
        "¡Hola Paciente!",
        size=28,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLUE_800
    )

    # Subtítulo
    subtitulo = ft.Text(
        "Gestiona tus citas de forma sencilla",
        size=18,
        italic=True,
        color=ft.colors.BLUE_600
    )

    # Botones principales
    boton_nueva_cita = ft.ElevatedButton(
        text="Nueva Cita",
        bgcolor=ft.colors.CYAN_400,
        color=ft.colors.WHITE,
        width=220,
        height=50,
        on_click=lambda e: page.go("/nueva-cita")
    )

    boton_mis_citas = ft.ElevatedButton(
        text="Mis Citas",
        bgcolor=ft.colors.CYAN_400,
        color=ft.colors.WHITE,
        width=220,
        height=50,
        on_click=lambda e: page.go("/mis-citas")
    )

    boton_editar_perfil = ft.ElevatedButton(
