from typing import Tuple

import streamlit as st
import numpy as np
import plotly.express as px

from algorithms.array_random_shuffle.simulate import simulate, distribution, average_cosine_similarity, euclidian_distance
from algorithms.array_random_shuffle.shuffle import wrong_sequential_swap_shuffle, fisher_yates_shuffle, wrong_random_pairs_shuffle

st.set_page_config(layout="wide")


def heatmap(data: np.ndarray, labels: Tuple[str, str]):
    chart = px.imshow(data, labels={'x': labels[1], 'y': labels[0]})
    st.plotly_chart(chart, use_container_width=True)


SHUFFLE_ALGORITHMS = {
    'no shuffling': lambda x: x,
    'random': lambda x: np.random.randint(0, len(x), size=len(x)),
    'Wrong Sequential Scan Algo': wrong_sequential_swap_shuffle,
    'Wrong Random Pairs Swap Algo': wrong_random_pairs_shuffle,
    'Fisher-Yates Shuffle': fisher_yates_shuffle,
}

shuffle_algo = st.sidebar.selectbox(label="Shuffle Algorithm", options=SHUFFLE_ALGORITHMS.keys())
array_size = st.sidebar.number_input("Array Size", min_value=2, value=50)
num_simulations = st.sidebar.number_input("Simulations number", min_value=2, value=100)
n_jobs = st.sidebar.number_input("Number of simulation jobs", min_value=1, value=4)


simulation_results = simulate(
    algorithm=SHUFFLE_ALGORITHMS[shuffle_algo],
    array_size=array_size,
    num_of_runs=num_simulations,
    n_jobs=n_jobs
)

actual_distr, target_distr = distribution(simulation_results)
cosine_sim = average_cosine_similarity(actual_distr, target_distr)
l2_dist = euclidian_distance(actual_distr, target_distr)

st.subheader("Simulation results:")
heatmap(simulation_results.T, labels=('values', 'simulations'))

st.subheader("Simulated Distribution:")
heatmap(actual_distr, labels=('result position', 'initial position'))

st.subheader("Cosine similarity with uniform distribution:")
st.write(round(cosine_sim, 3))

st.subheader("Euclidean distance with uniform distribution:")
st.write(round(l2_dist, 3))
