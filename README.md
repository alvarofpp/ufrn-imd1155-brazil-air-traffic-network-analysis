# Brazil air traffic network analysis
[![Open in Streamlit](https://img.shields.io/badge/-Streamlit-262730?style=for-the-badge&labelColor=000000&logo=Streamlit&logoColor=white)](#)

This work has as purpose to analyze under different metrics the air traffic in Brazil. Besides that, it makes it possible upload your own dataset (`.graphml`) and see all these analyses applied to him. Have fun!

Work of undergraduate course about Network Analysis (IMD1155) of Bachelor's degree in Information Technology from the Federal University of Rio Grande do Norte (UFRN), with [Ivanovitch Medeiros Dantas da Silva](https://github.com/ivanovitchm) as professor.

Group:
- [Álvaro Ferreira Pires de Paiva](https://github.com/alvarofpp)
  - Enrolment: 2016039162
  - E-mail: alvarofepipa@gmail.com
- [Marcos Vinícius Rêgo Freire](https://github.com/mvinnicius22)
  - Enrolment: 20210053533
  - E-mail: mvinnicius22@hotmail.com

You can find the dataset used in this work in [`alvarofpp/dataset-flights-brazil`](https://github.com/alvarofpp/dataset-flights-brazil).

You can find a detailed approach of these metrics above:

| Metric | Description |
| --- | --- |
| `Diameter` | [Diameter](https://colab.research.google.com/github/ivanovitchm/network_analysis/blob/main/week_06/Hubs.ipynb#scrollTo=5yquhZpJ1DaF&line=2&uniqifier=1) it is the **shortest** distance between the two most distant nodes in the network. |
| `Radius` | The [Radius](https://colab.research.google.com/github/ivanovitchm/network_analysis/blob/main/week_06/Hubs.ipynb#scrollTo=eRnXKxUU2UUw&line=1&uniqifier=1) of a network is the **minimum** eccentricity. |
| `Periphery` | The [Periphery](https://colab.research.google.com/github/ivanovitchm/network_analysis/blob/main/week_06/Hubs.ipynb#scrollTo=aaV5juQB4kCW&line=1&uniqifier=1) of a network is a set of all nodes whose eccentriciy is **equals** the diameter. |
| `Degree Centrality` | [Degree Centrality](https://colab.research.google.com/github/ivanovitchm/network_analysis/blob/main/week_06/Hubs.ipynb#scrollTo=GfPALZ3QUtlP&line=3&uniqifier=1) assigns an importance score based simply on the **number of links** held by each node. |
| `Betweenness Centrality` | [Betweenness Centrality](https://colab.research.google.com/github/ivanovitchm/network_analysis/blob/main/week_06/Hubs.ipynb#scrollTo=vqlupG50r8Yf) shows which nodes are **"bridges"** between nodes in a network. |
| `Closeness Centrality` | The [Closeness Centrality](https://colab.research.google.com/github/ivanovitchm/network_analysis/blob/main/week_06/Hubs.ipynb#scrollTo=zXVhKitENj3D) scores each node based on their **"closeness"** to all other nodes in the network. |
| `Eigenvector Centrality` | The [Eigenvector Centrality](https://colab.research.google.com/github/ivanovitchm/network_analysis/blob/main/week_06/Hubs.ipynb#scrollTo=ix_GsVjVc_d4) measures a node’s influence based on the **number of links** it has to other nodes in the network. |
| `k-core` | A [k-core](https://colab.research.google.com/github/ivanovitchm/network_analysis/blob/main/week_06/Hubs.ipynb#scrollTo=vqlupG50r8Yf) in a network is a subset of its nodes in which all nodes have at least **k** connections to each other. |
| `k-shell` | The [k-shell](https://colab.research.google.com/github/ivanovitchm/network_analysis/blob/main/week_06/Hubs.ipynb#scrollTo=PgYUzep5KqrU&line=5&uniqifier=1) of a graph G is the set of all nodes belonging to the k–core of G but not to the **(k+1)**–core. |


## Run the app

You can run the app in 3 different ways:

- Virtual environment;
- Docker container;
- Docker-compose.

### Virtual Environment

In your environment:

```shell
# Install requirements for scripts
pip install -r requirements.txt

# (optional) If you want updates the data
python3 extract.py

# Run the app
streamlit run app.py
```

### Docker

These instructions will cover usage information and for the docker container.

#### Prerequisites

In order to run this app you'll need docker installed.

- [Get Started](https://docs.docker.com/get-started/)

#### Run

Step 1:
```shell
# Build the docker image
docker build -t streamlitapp:latest .
# Or specifying a file
docker build -t streamlitapp:latest .f Dockerfile
```

Step 2:
```shell
# Run a container
docker run -p 8501:8501 streamlitapp:latest
```

### Docker-compose

If you prefer to use docker-compose to run the app with others services, this is the section.

#### Prerequisites

See the [Docker prerequisites](#) section before this section. After that, you need to install docker-compose:

- [Install Docker Compose](https://docs.docker.com/compose/install/)

After installed docker-compose, create a `.env` file (you can see [`.env.example`](.env.example) as an example).

#### Environment Variables

- `STREAMLIT_PORT` - The port the app runs on. By default, is `8501`.

#### Run

```shell
# Run the app
docker-compose up
```

## Contributing
Contributions are more than welcome. Fork, improve and make a pull request. For bugs, ideas for improvement or other, please create an [issue](https://github.com/alvarofpp/ufrn-imd1155-brazil-air-traffic-network-analysis/issues).

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
