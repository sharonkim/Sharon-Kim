i = 0
num = 5

for i in 0..5
    puts "Value of local variable is #{i}"
end

for i in 0..5
    puts "Value of local variable is #{i}"
    break if i == 2
end

for i in 0..5
    next if i == 2
    puts "Value of local variable is #{i}"
end
