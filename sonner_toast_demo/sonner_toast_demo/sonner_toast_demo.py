"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from rxconfig import config

import reflex as rx

from reflex_sonner_toast import toast, toaster

filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    def so_something(self):
        pass


def index() -> rx.Component:
    return rx.center(
        toaster(expand=True),
        rx.vstack(
            rx.button("Toast Message", on_click=toast.error('This is a message toast', position="top-center")),
            rx.button("Toast Message Dark Theme", on_click=toast.error('This is a message toast with dark theme', position="top-center", theme="dark")),
            rx.button("Toast Error", on_click=toast.error('An error occurred', position="top-center", style={"background": "red"})),
            rx.button("Toast success", on_click=toast.success('This message was a success', position="bottom-left", style={
                "background": "green"
            })),
            rx.button("Toast Message + close", on_click=toast.error('This is a message toast', position="top-center", close_button=True, invert=True)),
            align="center",
            spacing="7",
        ),
        height="100vh",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index, on_load=toast.messaage("The page has loaded!"))
# app.add_page(index, on_load=rx.console_log("Hey there page has loaded"))