import streamlit as st


class RenderMixin:
    def __init__(self, render_component=None):
        self.render_component = render_component if render_component is not None else st
