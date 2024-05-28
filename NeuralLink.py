import numpy as np
import matplotlib.pyplot as plt

class Neuron:
    def __init__(self, n_inputs, bias=0., weights=None):
        self.b = bias
        self.ws = np.random.rand(n_inputs) if weights is None else np.array(weights)

    def _f(self, x):
        return max(x * .1, x)

    def __call__(self, xs):
        return self._f(np.dot(xs, self.ws) + self.b)

class NeuralNetwork:
    def __init__(self, structure):
        self.layers = [[Neuron(structure[i-1]) for _ in range(structure[i])] for i in range(1, len(structure))]

    def visualize(self):
        layer_sizes = [len(self.layers[0][0].ws)] + [len(layer) for layer in self.layers]
        v_spacing = 1 / float(max(layer_sizes))
        h_spacing = 1 / float(len(layer_sizes) - 1)
        colors = ['red', 'blue', 'blue', 'green']

        fig, ax = plt.subplots(figsize=(12, 8))
        ax.axis('off')

        for i, layer_size in enumerate(layer_sizes):
            layer_top = (1 - v_spacing * (layer_size - 1)) / 2
            for j in range(layer_size):
                x = i * h_spacing
                y = layer_top + j * v_spacing
                circle = plt.Circle((x, y), v_spacing / 6, color=colors[i], ec='k', zorder=4)
                ax.add_artist(circle)
                ax.annotate(f'Layer {i+1}', xy=(x, y), ha='center', va='center', fontsize=9, zorder=5)

        for i, (layer_size_a, layer_size_b) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:])):
            layer_top_a = (1 - v_spacing * (layer_size_a - 1)) / 2
            layer_top_b = (1 - v_spacing * (layer_size_b - 1)) / 2
            for j in range(layer_size_a):
                for k in range(layer_size_b):
                    line = plt.Line2D([i * h_spacing, (i + 1) * h_spacing],
                                      [layer_top_a + j * v_spacing, layer_top_b + k * v_spacing], c='k', zorder=3)
                    ax.add_artist(line)

        plt.show()

structure = [3, 4, 4, 1]
network = NeuralNetwork(structure)

network.visualize()
