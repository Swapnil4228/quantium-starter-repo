import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


def test_header_present(dash_duo):
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert header.text == "Soul Foods Pink Morsel Sales Dashboard"


def test_graph_present(dash_duo):
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-graph")
    assert graph is not None


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)

    picker = dash_duo.find_element("#region-selector")
    assert picker is not None