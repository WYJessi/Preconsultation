"""Welcome to Reflex!."""

from preconsultation import styles

# Import all the pages.
from preconsultation.pages import *

import reflex as rx

# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
# Create the app and compile it.
# app = rx.App(style=styles.base_style)
# app.compile()
