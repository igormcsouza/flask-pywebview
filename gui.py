import webview

from starter import create_app


window = webview.create_window('Application', create_app())
webview.start()