import streamlit as st
from .Component import Component


class GraphSelectComponent(Component):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def render(self):
        if not self._check():
            return

        if len(st.session_state['options']) > 1:
            option = self.render_component.selectbox('Select the graph',
                                                     options=st.session_state['options'])
        else:
            option = st.session_state['options'][0]

        st.session_state['graph_selected'] = st.session_state['graphs'][option]

    def _check(self):
        if 'graphs' not in st.session_state.keys() or 'options' not in st.session_state.keys():
            return False

        return len(st.session_state['graphs']) > 0 and len(st.session_state['options']) > 0
