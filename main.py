from nicegui import ui
from nicegui.element import Element


@ui.page("/")
def index():
    ui.label("nicegui==3.10.0")
    ui.link("ok page", "/ok")
    ui.link("issue_keyframe_css page", "/issue_keyframe_css")
    ui.link("issue_keyframe_css_import_order_matters page",
            "/issue_keyframe_css_import_order_matters")


@ui.page("/ok")
def page_ok():
    from components.plain_style_component import PlainStyleComponent
    ui.label("ok page")
    PlainStyleComponent()
    ui.button("show `<style>", on_click=lambda: show_style(style_container))
    style_container = ui.column().classes("w-full flex flex-reverse")


@ui.page("/issue_keyframe_css")
def page_issue_keyframe_css():
    from components.keyframe_component import KeyframeComponent
    from components.plain_style_component import PlainStyleComponent
    ui.label("issue_keyframe_css")
    KeyframeComponent()
    PlainStyleComponent()
    ui.button("show `<style>", on_click=lambda: show_style(style_container))
    style_container = ui.column().classes("w-full flex flex-reverse")


@ui.page("/issue_keyframe_css_import_order_matters")
def page_issue_keyframe_css():
    from components.plain_style_component import PlainStyleComponent
    from components.keyframe_component import KeyframeComponent
    ui.label("issue_keyframe_css_import_order_matters")
    KeyframeComponent()
    PlainStyleComponent()
    ui.button("show `<style>", on_click=lambda: show_style(style_container))
    style_container = ui.column().classes("w-full flex flex-reverse")


async def show_style(container: Element):
    style: str = await ui.run_javascript(
        """
(function() {
    const style = document.querySelectorAll("style")[3]
    return style.innerText
})()
""")
    open_bracket_count = style.count("{")
    close_bracket_count = style.count("}")
    with container:
        with ui.column().classes("w-full border-1 p-2"):
            ui.code(style, language="css").classes("w-full")
            ui.markdown((
                f"Bracket count matched? **{open_bracket_count == close_bracket_count}**"
                f", {open_bracket_count=}"
                f", {close_bracket_count=}"
            )
            ).classes("font-mono")


ui.run(
    dark=True,
    show=False,
)
