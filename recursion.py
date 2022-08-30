def sum_positive_numbers(n):
  count = 0
  for num in range (1, n+1):
    print(num)
    count += num
  if n <= 1:
   return 0
  return count

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5))

def isPower (x, y):
     
    # The only power of 1
    # is 1 itself
    if (x == 1):
        return (y == 1)
         
    # Repeatedly compute
    # power of x
    pow = 1
    while (pow < y):
        pow = pow * x
 
    # Check if power of x
    # becomes y
    return (pow == y)

    def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return __

  # Recursive case: keep dividing number by base.
  return is_power_of(__, ___)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False