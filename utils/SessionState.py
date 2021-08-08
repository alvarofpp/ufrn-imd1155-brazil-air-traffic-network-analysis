import streamlit as st


class SessionState:
    DEFAULT_VALUES = {
        'graphs': {},
        'options': [],
        'graph_selected': None,
        'mode': None,
    }

    @staticmethod
    def get_keys():
        return SessionState.DEFAULT_VALUES.keys()

    @staticmethod
    def init_session():
        for key, value in SessionState.DEFAULT_VALUES.items():
            if key not in st.session_state:
                st.session_state[key] = value

    @staticmethod
    def clear_session():
        for key in SessionState.get_keys():
            if key in st.session_state:
                del st.session_state[key]

    @staticmethod
    def set_graphs_to_session(graphs):
        st.session_state['graphs'] = graphs
        st.session_state['options'] = list(graphs.keys())

    @staticmethod
    def restart_session():
        SessionState.clear_session()
        SessionState.init_session()

    @staticmethod
    def change_mode(mode_selected):
        if 'mode' not in st.session_state.keys():
            st.session_state['mode'] = mode_selected
        elif st.session_state['mode'] != mode_selected:
            SessionState.restart_session()
            st.session_state['mode'] = mode_selected

    @staticmethod
    def can_render_pages():
        return 'graphs' in st.session_state.keys() and len(st.session_state['graphs']) > 0
