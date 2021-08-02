import streamlit as st
from .View import View


class IntroView(View):
    def render(self, graph=None):
        st.sidebar.markdown("""
        This work has as purpose to analyze the air traffic in Brazil.
        
        Work of undergraduate course about Network Analysis (IMD1155) of Bachelor's degree in Information Technology from
        the Federal University of Rio Grande do Norte (UFRN), with
        [Ivanovitch Medeiros Dantas da Silva](https://github.com/ivanovitchm) as professor.
    
        Group: [Álvaro Ferreira Pires de Paiva](https://github.com/alvarofpp) and [Marcos Vinícius Rêgo Freire](https://github.com/mvinnicius22).
        
        ----------
        """)
