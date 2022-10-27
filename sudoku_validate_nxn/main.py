# https://www.codewars.com/kata/540afbe2dc9f615d5e000425/train/python
# Validate Sudoku with size `NxN`

import math

class Sudoku(object):
    def __init__(self, data):
        self.data = data
        self.valid_nums = self.valid_nums()
        pass
    
    def valid_nums(self):
        return [num for num in range(1,len(self.data)+1)]
    
    def is_valid(self):
        #print(self.data)
        if not self.isSquare() or not self.rows_are_valid():
            return False
        if not self.boxes_are_valid():
            return False
        return True
    
    def isSquare (self): return all (len (row) == len (self.data) for row in self.data)
    
    def rows_are_valid(self):
        for row in self.data:
            if set(row) != set(self.valid_nums):
                return False
        return True

    def boxes_are_valid(self):
        boxes = self.extract_boxes()
        print(f"BOX: {boxes}")

        for box in boxes:
            if not self.box_is_valid(box):
                return False
        return True

    def extract_boxes(self):
        boxes = []
        row_len = len(self.data)
        n = int(math.sqrt(row_len)) # Take the sqrt to find the box size

        for i in range(0, row_len, n): # Go to first Index of every Row
            for j in range(0, row_len, n): # Go to first Index of every Spalte
                box = []
                #print(f"I: {i}, J: {j}")
                for x in range(i, i +n):
                    for y in range(j, j+n):
                        box.append(self.data[x][y])
                boxes.append(box)
        return boxes


            
    def box_is_valid(self, box):
        print(f"BOX IN BOX IS VALID: {box}")
        print(f"SET: {set(box)}, set valid Nums: {set(self.valid_nums)}")
        return set(box) == set(self.valid_nums)


goodSudoku1 = Sudoku([
  [7,8,4, 1,5,9, 3,2,6],
  [5,3,9, 6,7,2, 8,4,1],
  [6,1,2, 4,3,8, 7,5,9],

  [9,2,8, 7,1,5, 4,6,3],
  [3,5,7, 8,4,6, 1,9,2],
  [4,6,1, 9,2,3, 5,8,7],
  
  [8,7,6, 3,9,4, 2,1,5],
  [2,4,3, 5,6,1, 9,7,8],
  [1,9,5, 2,8,7, 6,3,4]
])

goodSudoku2 = Sudoku([
  [1,4, 2,3],
  [3,2, 4,1],

  [4,1, 3,2],
  [2,3, 1,4]
])

# Invalid Sudoku
badSudoku1 = Sudoku([
  [0,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9]
])

badSudoku2 = Sudoku([
  [1,2,3,4,5],
  [1,2,3,4],
  [1,2,3,4],  
  [1]
])

# test.it('should be valid')
# test.assert_equals(goodSudoku1.is_valid(), True, 'Testing valid 9x9')
# test.assert_equals(goodSudoku2.is_valid(), True, 'Testing valid 4x4')

# test.it ('should be invalid')
# test.assert_equals(badSudoku1.is_valid(), False, 'Values in wrong order')
# test.assert_equals(badSudoku2.is_valid(), False, '4x5 (invalid dimension)')

goodSudoku1.is_valid()