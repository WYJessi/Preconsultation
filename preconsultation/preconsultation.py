"""Welcome to Reflex!."""

# Import all the pages.
from preconsultation.pages import *

import reflex as rx
from preconsultation import styles
from preconsultation.state import State


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=styles.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=styles.answer_style),
            text_align="left",
        ),
        margin_y="1em",
    )

# def chat() -> rx.Component:
#     qa_pairs = [
#         (
#             "What is Reflex?",
#             "A way to build web apps in pure Python!",
#         ),
#         (
#             "What can I make with it?",
#             "Anything from a simple website to a complex web app!",
#         ),
#     ]
#     return rx.box(
#         *[
#             qa(question, answer)
#             for question, answer in qa_pairs
#         ]
#     )

def chat() -> rx.Component:
    # qa_pairs = [
    #     (
    #         "What is Reflex?",
    #         "A way to build web apps in pure Python!",
    #     ),
    #     (
    #         "What can I make with it?",
    #         "Anything from a simple website to a complex web app!",
    #     ),
    # ]
    return rx.box(
            rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )

def handle_keypress(event):
    if event.key == 'Enter':
        State.answer()

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Ask a question",
            on_change=State.set_question,
            style=styles.input_style,
        ),
        # rx.input(
        #     value=State.question,
        #     placeholder="Ask a question",
        #     on_change=State.set_question,
        #     on_keypress=handle_keypress,  # handle_keypress will check for Enter and call State.answer
        #     style=styles.input_style,
        # ),
        rx.button(
            "Ask",
            on_click=State.answer,
            style=styles.button_style,
        ),
    )


def index() -> rx.Component:
    return rx.container(
        chat(),
        action_bar(),
    )


app = rx.App()
app.add_page(index)
app.compile()
# Add state and page to the app.
# Create the app and compile it.
# app = rx.App(style=styles.base_style)
# app.compile()
