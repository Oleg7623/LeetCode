from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        for i in range(9):
            rows.append(set())
        
        cols = []
        for i in range(9):
            cols.append(set())
        boxes = []
        for i in range(9):
            boxes.append(set())
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                
                if num == '.':
                    continue
                
                box_index = (r // 3) * 3 + (c // 3)
                
                # Перевіряємо наявність дублікатів у рядку, стовпці та 3x3 коробці
                if num in rows[r]:
                    return False
                if num in cols[c]:
                    return False
                if num in boxes[box_index]:
                    return False
                
                # Додаємо число до відповідних множин рядка, стовпця та 3x3 коробки
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)
        
        return True
