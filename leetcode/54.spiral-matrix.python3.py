class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        n = len(matrix)

        if not matrix[0]:
            return []
        m = len(matrix[0])

        i, j = 0, 0
        result = []
        while n > 0 and m > 0:
            i_last, j_last = i + n - 1, j + m - 1
            # edge case
            if n == 1:
                result.extend(matrix[i][j:j_last+1])
                break
            elif m == 1:
                for r in range(i, i_last+1):
                    result.append(matrix[r][j])
                break

            result.extend(matrix[i][j:j_last])
            for r in range(i, i_last):
                result.append(matrix[r][j_last])
            for c in range(j_last, j, -1):
                result.append(matrix[i_last][c])
            for r in range(i_last, i, -1):
                result.append(matrix[r][j])

            i, j = i + 1, j + 1
            n, m = n - 2, m - 2

        return result
