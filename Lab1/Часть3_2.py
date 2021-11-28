import numpy as np
import networkx as nx

if __name__ == '__main__':
  
    gml1 = nx.read_gml('VK.gml')
    ctr = [0] * 7

    friends = {}
    fr_num = []

    for node in gml1.nodes:
        friends[node] = 0

    for edge in gml1.edges:
        friends[edge[0]] += 1
        friends[edge[1]] += 1

    frs = sorted(friends.items(), key=lambda x: x[1], reverse=True)

    print("Количество уникальных пользователей равно:", len(gml1.nodes))
    print("Пользователи с наибольшим количеством друзей:")

    for pair in frs:
        fr_num.append(pair[1])
    print('Медианное число друзей:', np.median(fr_num))

    print('Среднее число друзей:', np.mean(fr_num))
    for pair in frs[:15]:
        counter += 1
        print(pair[0], " ", pair[1])

    for pair in frs:
        fr_num.append(pair[1])

    print('Медианное число друзей:', np.median(fr_num))
    print('Среднее число друзей:', np.mean(fr_num))

    all_pairs = nx.all_pairs_shortest_path_length(gml1)

    for pair in all_pairs:
        for leng in pair[1].values():
            if leng >= 1 and leng <= 6:
                ctr[leng - 1] += 1
            else:
                ctr[6] += 1

    total_ln = sum(len_counter)

    for i in range(0, 6):
        print(f'Доля пар с L={i} {round(ctr[i] / total_ln, 4)}')
    print(f'Доля пар с L>6 или с отсутствующим путем {round(ctr[6] / total_ln, 4)}')