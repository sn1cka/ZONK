class ScoresCalculator:

    def calculate_points(self, x):
        count_of = [0, 0, 0, 0, 0, 0]
        for item in x:
            if item - 1 >= 0:
                count_of[item - 1] += 1

        result = 0
        pair_count = 0

        for item in count_of:  # Проверки на пары, если  3, то 750 очков
            if item == 2:
                pair_count += 1
        if pair_count == 3:
            result += 750
            return result

        if count_of == [1, 1, 1, 1, 1, 1]:  # Все разные, то 1500 очков
            result += 1500
            return result

        if count_of[4] < 3:  # 50 очков за 5 (если меньше 3)
            result += count_of[4] * 50
        if count_of[0] < 3:  # 100 очков за каждую 1 (если меньше 3)
            result += 100 * count_of[0]

        for i in range(0,
                       6):  # Три одиннаковых кости номинал*100 + столько же за каждую последующую кость того же номинала
            if i == 0:
                multiple_coefficient = 1000
            else:
                multiple_coefficient = 100 * (i + 1)
            if count_of[i] >= 3:
                result += multiple_coefficient + (count_of[i] - 3) * multiple_coefficient

        return result
