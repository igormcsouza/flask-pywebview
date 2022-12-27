import webview

from project.starter import create_app


window = webview.create_window("Application", create_app())
webview.start()
