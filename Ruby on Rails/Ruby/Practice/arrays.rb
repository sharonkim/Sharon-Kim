x = [1, 2, 3, 4, 5, 6]

puts x.at(2) # => 3
puts x.fetch(2) # => 3
puts x.delete(1) # => 1
puts x.reverse # => 6 5 4 3 2 1
puts x.length # => 6
puts x.sort # => 1 2 3 4 5 6
puts x.slice(1) # => 2
puts x.shuffle # => 4 1 5 2 3 6
puts x.join # => 123456
puts x.insert(3, "this is the middle") # => 1 2 3 this is the middle 4 5 6

a = %w{turtles unicorns rainbows}
    puts a.values_at(1, 2).join(' and ') # => unicorns and rainbows


# Replace negative values with 0
array = [1, 2, -9, 6, -6, 7]

array.each_with_index { |val, x| array[index] = 0 if val < 0 } # => [1, 2, 0, 6, 0, 7]
array.each_with_index { |val, x| array[index] = 0 if val < 0 }.each { |x| puts x } # => [1, 2, 0, 6, 0, 7]
array.map! { |val| val < 0 ? 0 : val } # => [1, 2, 0, 6, 0, 7]
