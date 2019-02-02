# This python file is used to train the Multiplex Network Embedding model
# Author: Hongming ZHANG, HKUST KnowComp Group

from MRWE import *
import sys

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
file_name = "data/small_example.txt"
edge_data_by_type, all_edges, all_nodes = load_network_data(file_name)
model = train_model(edge_data_by_type)


save_model(model, 'model')

test_model = load_model('model')

