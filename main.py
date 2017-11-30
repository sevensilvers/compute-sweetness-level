import sys

def get_sweetness_level(bar_length, student_count, student_lists):
  n, s = [int(bar_length), int(student_count)]
  right_to_left = dict()
  left_to_right = dict()
  sweetness_list = []
  for student_bars in student_lists:
    l, r = [int(student_bars[0]), int(student_bars[1])]
    sweetness = (r * (r + 1) / 2) - (l * (l - 1) / 2)
    new_left, new_right = l, r
    if l > 0 and l - 1 in right_to_left:
            new_left = right_to_left[l - 1]
            right_to_left.pop(l - 1)
    if r < n - 1 and (r + 1) in left_to_right:
            new_right = left_to_right[r + 1]
            left_to_right.pop(r + 1)
    if new_left > 0:
        sweetness += new_left - 1
        new_left -= 1
    if new_right < n - 1:
        sweetness += new_right + 1
        new_right += 1
    if new_right + 1 in left_to_right:
        new_right = left_to_right.pop(new_right + 1)
    if new_left - 1 in right_to_left:
        new_left = right_to_left.pop(new_left - 1)
    right_to_left[new_right] = new_left
    left_to_right[new_left] = new_right
    sweetness_list.append(sweetness)
  return sweetness_list

print get_sweetness_level(10, 3, [[2,4],[6,7],[9,9]])
