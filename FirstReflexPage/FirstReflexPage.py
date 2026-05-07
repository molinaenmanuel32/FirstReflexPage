"""Mi primera página web con Reflex."""

import reflex as rx
from rxconfig import config


class State(rx.State):
    """El estado de la aplicación."""
    mensaje: str = "¡Bienvenido a mi primera página web con reflex!"

    @rx.event
    def cambiar_mensaje(self):
        self.mensaje = "¡Hiciste clic! funciona "


def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            # Título principal
            rx.heading(
                "¡Bienvenido a Emañoland!",
                size="9",
            ),
            
            rx.text(
                "Esta página fue creada con Reflex, "
                "un framework para el desarrollo web.",
                size="5",
                color="gray",
            ),
         
            rx.text(
                State.mensaje,
                size="4",
                weight="bold",
                color="violet",
            ),
           
            rx.button(
                "¡Haz clic aquí!",
                on_click=State.cambiar_mensaje,
                color_scheme="violet",
                size="3",
                radius="full",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            align="center",
        ),
    )


app = rx.App()
app.add_page(index, title="Mi Primera Web con Reflex")