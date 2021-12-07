import pickle


def myMap():
    """
    Load map.
    :return: map và cost
    """
    f = open('./data/map.pkl', 'rb')
    my_map = pickle.load(f)
    f.close()

    f = open('./data/costs.pkl', 'rb')
    costs = pickle.load(f)
    f.close()
    return my_map, costs
