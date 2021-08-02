import streamlit as st
from .Component import Component


class SelectComponent(Component):
    def __init__(self, values=None):
        super().__init__()
        self.values = values

    def format(self, option: int):
        return self.values[option]

    def render(self, label: str):
        return st.sidebar.selectbox(label, options=list(self.values.keys()), format_func=self.format)
