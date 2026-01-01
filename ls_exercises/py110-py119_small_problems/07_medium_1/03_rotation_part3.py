'''
Take the number 735291 and rotate it by one digit to the left, getting 352917. Next, keep the first digit fixed in place and rotate the remaining digits to get 329175. Keep the first two digits fixed in place and rotate again to get 321759. Keep the first three digits fixed in place and rotate again to get 321597. Finally, keep the first four digits fixed in place and rotate the final two digits to get 321579. The resulting number is called the maximum rotation of the original number.

Write a function that takes an integer as an argument and returns the maximum rotation of that integer. You can (and probably should) use the rotate_rightmost_digits function from the previous exercise.

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True
'''
# part a:
# Take the number 735291 and rotate it by one digit to the left, getting 352917.

# part b:
# keep the first digit fixed in place and rotate the remaining digits to get 329175.

# part c:
# Keep the first two digits fixed in place and rotate again to get 321759.

# part d:
# Keep the first three digits fixed in place and rotate again to get 321597.

# part e:
# keep the first four digits fixed in place and rotate the final two digits to get 321579.

# ==========
# My Solution
# ==========

def rotate_rightmost_digits(number, rotations):
    digits = str(number)
    return int(digits[:-rotations] + digits[-rotations:][1:] + digits[-rotations])

# used the following function to show the process step-by-step
def max_rotation(number):
    digits = str(number)
    part_a = digits[:0] + digits[1:] + digits[0]
    print(part_a)
    part_b = part_a[:1] + part_a[2:] + part_a[1]
    print(part_b)
    part_c = part_b[:2] + part_b[3:] + part_b[2]
    print(part_c)
    part_d = part_c[:3] + part_c[4:] + part_c[3]
    print(part_d)
    part_e = part_d[:4] + part_d[5:] + part_d[4]
    print(part_e)
    return int(part_e)

def max_rotation(number):
    digits = str(number)
    for n in range(len(digits)-1):
        digits = digits[:n] + digits[n+1:] + digits[n:n+1]
    return int(digits)

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True

# ==========
# LS Solution
# ==========

def rotate_rightmost_digits(number, count):
    number_str = str(number)
    first_part = number_str[:-count]
    second_part = number_str[-count:]
    result_str = first_part + rotate_string(second_part)

    return int(result_str)

def max_rotation(number):
    number_digits = len(str(number))
    for count in range(number_digits, 1, -1):
        number = rotate_rightmost_digits(number, count)

    return number