import streamlit as st
from .View import View


class IntroView(View):
    def render(self):
        st.markdown("""
        This work has as purpose to analyze the air traffic in Brazil.
        
        Work of undergraduate course about Network Analysis (IMD1155) of Bachelor's degree in Information Technology from
        the Federal University of Rio Grande do Norte (UFRN), with
        [Ivanovitch Medeiros Dantas da Silva](https://github.com/ivanovitchm) as professor.
    
        Group:
        - [Álvaro Ferreira Pires de Paiva](https://github.com/alvarofpp)
            - Matrícula: 2016039162
            - E-mail: alvarofepipa@gmail.com
        - [Marcos Vinícius Rêgo Freire](https://github.com/mvinnicius22)
            - Matrícula: 20210053533
            - E-mail: mvinnicius22@hotmail.com
        
        ----------
        """)
