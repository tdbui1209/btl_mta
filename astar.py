import collections
from modules import showResultWithAttr, aweSomeSort, showStep


def AStar(start, target, my_map, costs):
    print('Các bước:')
    costs[start] = 0

    q = collections.deque()  # khởi tạo queue
    q.append(start)  # enqueue

    previous = []  # khởi tạo previous kiểu dictionary
    for point in my_map.keys():
        if point == start:
            previous.append((point, {'from': start, 'total_cost': costs[point]}))  # Đưa start vào điểm đã đi qua
        else:
            previous.append((point, {'from': None, 'total_cost': costs[point]}))
    previous = dict(previous)

    counter = 0
    while 1:
        counter += 1
        showStep(counter, q, previous)  # Show các bước thực hiện thuật toán
        curPoint = q.popleft()  # enqueue (Đây cũng là phần tử nhỏ nhất vì đã sắp xếp queue tăng dần)

        if curPoint == target:
            showResultWithAttr(previous, start, target)
            break

        curCityTotalCost = previous[curPoint]['total_cost'] - costs[curPoint]  # Chi phí để đi từ start đến curPoint

        if curPoint != target:
            for point in my_map[curPoint].keys():  # Các điểm có thể đi đến được từ curPoint
                pointTotalCost = previous[point]['total_cost']  # Chi phí được tính ở bước trước đó
                totalCost = my_map[curPoint][point]['distance'] + curCityTotalCost + costs[
                    point]  # Chi phí để đi từ start -> curPoint -> target

                # Nếu chưa đi qua điểm này hoặc chi phi đi từ start -> curPoint -> target tốt hơn chi phí trước đó
                if previous[point]['from'] is None or totalCost < pointTotalCost:
                    if q.count(point) != 0:  # Nếu đã có point này trong hàng đợi thì xóa nó đi
                        q.remove(point)
                    q.append(point)  # Thêm vào hàng đợi
                    previous[point]['from'] = curPoint  # Lưu lại dấu vết
                    previous[point]['total_cost'] = totalCost  # Cập nhật lại chi phí mới

        if len(q) == 0:
            print('Fail!')
            return False  # Không thể đi đến goal từ start
        q = collections.deque(aweSomeSort(q, previous))  # Sắp xếp lại hàng đợi tăng dần theo total_cost
