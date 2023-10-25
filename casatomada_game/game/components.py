from reactpy import component, html


# variable debe estar pegado al variable="texto" (en el archivo index)
@component
def hello_world(variable):
    return html.h1(f"Hello, {variable}")