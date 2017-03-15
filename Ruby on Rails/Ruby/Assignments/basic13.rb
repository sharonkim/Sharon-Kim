# Print 1-255
1.upto(255) { |i| print i, ", " }

# Print odd numbers between 1-255
(1..255).each { |i| print i, ", " if i.odd? }

# Print Sum
(1..255).each { |i| puts "New number: #{i}  Sum: #{ i * ( i + 1 ) / 2 }" }

# Iterating through an array
arr.each { |i| print i, ", "}

# Find Max
print arr.max

# Get Average
total.to_f / len

# Array with Odd Numbers
y = []
(1..255).each { |i| y << i if i.odd? }

# Greater than Y
y = rand(5..10)
puts "y = #{y}"
puts arr.count { |elem| elem > y }

# Square the values
x = []
puts x.map! { |elem| elem * elem }

# Elimainate Negative Numbers
x = []
puts x.each_index { |index| x[index] = 0 if x[index] < 0 }

Max, Min, and Average
x = []
{ max: x.max, min: x.min, average: x.reduce(:+) / x.length.to_f }

# Shifting the Values in the Array
x = []
x.rotate!(1)[x.length - 1] = 0

# Number to String
x = []
print x.each_index { |index| x[index] = "Dojo" if x[index] < 0 }
