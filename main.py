

import flet as ft
import openai
import time



##generate API key from openAI site

openai.api_key = ""


def main_style():
    return {}




class MainContentArea(ft.Container):
    def __init__(self):
        super().__init__(**main_style())
        self.chat = ft.ListView(
            expand = True,
            height = 200,
            spacing = 15,
            auto_scroll=True,

        )
        self.content = self.chat





def main(page: ft.Page):
    page.horizontal_alignment="center"
    page.vertical_alignment="center"
    page.theme_mode = "dark"

    main = MainContentArea()



    page.update()


if __name__=="__main__":
    ft.app(target=main)