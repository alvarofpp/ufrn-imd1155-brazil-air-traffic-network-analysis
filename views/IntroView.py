from .View import View


class IntroView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def render(self):
        self.render_component.markdown("""
        This work has as purpose to analyze under different metrics the air traffic in Brazil. Besides that, it makes it
        possible upload your own dataset (`.graphml`) and see all these analyses applied to him. Have fun!
        
        Work of undergraduate course about Network Analysis (IMD1155) of Bachelor's degree in Information Technology
        from the Federal University of Rio Grande do Norte (UFRN), with
        [Ivanovitch Medeiros Dantas da Silva](https://github.com/ivanovitchm) as professor.

        Group: [Álvaro Ferreira Pires de Paiva](https://github.com/alvarofpp) and
        [Marcos Vinícius Rêgo Freire](https://github.com/mvinnicius22).
        
        [![Github](https://img.shields.io/badge/-Github-181717?style=for-the-badge&logo=Github&logoColor=white)](https://github.com/alvarofpp/ufrn-imd1155-brazil-air-traffic-network-analysis)

        ----------
        """)
