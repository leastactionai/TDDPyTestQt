import pytest
from PySide6 import QtCore
import basic_app


@pytest.fixture
def app(qtbot):
    test_basic_app = basic_app.BasicApp()
    qtbot.addWidget(test_basic_app)

    return test_basic_app


def test_label(app):
    assert app.text_label.text() == "Hello World!"


def test_window_title(app):
    app.windowTitle() == "PySide6 Example"


def test_label_after_click(app, qtbot):
    qtbot.mouseClick(app.button, QtCore.Qt.LeftButton)
    assert app.text_label.text() == "Changed!"
