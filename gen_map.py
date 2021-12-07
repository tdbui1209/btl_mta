import os
import random
import pickle
random.seed(42)


def rand_plane(n_points=1000, x_limit=1000, y_limit=1000):
    """
    Tạo một mặt phẳng với n điểm.
    :param n_points: số lượng điểm trên mặt phẳng (int)
    :param x_limit: giới hạn x của mặt phẳng (int)
    :param y_limit: giới hạn y của mặt phẳng (int)
    :return: n_points phần tử (x, y), tọa độ của n_points điểm (list)
    """
    plane = []
    while len(plane) < n_points:
        x, y = random.randint(0, x_limit), random.randint(0, y_limit)
        if (x, y) not in plane:
            plane.append((x, y))
    return plane


def euclidean_distance(x1, y1, x2, y2):
    """
    Tính khoảng cách euclid của 2 điểm.
    :param x1: tọa độ x của điểm thứ nhất (int)
    :param y1: tọa độ y của điểm thứ nhất (int)
    :param x2: tọa độ x của điểm thứ hai (int)
    :param y2: tọa độ y của điểm thứ hai (int)
    :return: khoảng cách của 2 điểm trong mặt phẳng (float)
    """
    return ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)


def rand_costs(n_points=1000):
    """
    Tạo costs cho n điểm.
    :param n_points: số lượng điểm trên mặt phẳng (int)
    :return: danh sách các costs. (list)
    """
    return [random.randint(1, 100) for _ in range(n_points)]


def rand_map(n_points=1000, max_next_node=500):
    """
    Tạo map bằng cách nối các điểm, với mỗi điểm chỉ nối tới tối đa [0, max_next_node].
    Rồi lưu vào thư mục ./data.
    :param n_points: số điểm trong mặt phẳng
    :param max_next_node: số điểm mà một điểm nối tới tối đa
    :return: 2 files map.pkl và costs.pkl
    """
    plane = rand_plane(n_points)
    costs = rand_costs(n_points)

    my_map = {}

    for i in range(len(plane)):
        if i not in my_map.keys():
            my_map[i] = {}

        x1 = plane[i][0]
        y1 = plane[i][1]

        for j in range(random.randint(0, max_next_node)):

            next_node = random.randint(0, len(plane) - 1)
            if next_node == i:
                continue

            x2 = plane[next_node][0]
            y2 = plane[next_node][1]

            distance = euclidean_distance(x1, y1, x2, y2)

            my_map[i][next_node] = {'cost': distance}

            if next_node not in my_map.keys():
                my_map[next_node] = {}
            my_map[next_node][i] = {'cost': distance}

    if not os.path.exists('./data'):
        os.mkdir('./data')

    f = open('./data/map.pkl', 'wb')
    pickle.dump(my_map, f)
    f.close()

    f = open('./data/costs.pkl', 'wb')
    pickle.dump(costs, f)
    f.close()


if __name__ == '__main__':
    rand_map(n_points=1000, max_next_node=1000)
