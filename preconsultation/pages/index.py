"""The home page of the app."""

from preconsultation import styles
from preconsultation.templates import template

import reflex as rx


# @template(route="/", title="Home", image="/github.svg")
# def index() -> rx.Component:
#     """The home page.

#     Returns:
#         The UI for the home page.
#     """
#     with open("README.md", encoding="utf-8") as readme:
#         content = readme.read()
#     return rx.markdown(content, component_map=styles.markdown_style)

def index() -> rx.Component:
    return rx.container(
        rx.box(
            "What is Reflex?",
            # The user's question is on the right.
            text_align="right",
        ),
        rx.box(
            "A way to build web apps in pure Python!",
            # The answer is on the left.
            text_align="left",
        ),
    )


