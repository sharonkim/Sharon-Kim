y = {first_name:  "Coding", last_name:  "Dojo"}
y.delete :last_name
puts y # => {:first_name:"Coding"}


if y.empty?
    puts "There is no key-value pair"
else
    puts "Key-value pair exists"
end # => Key-value pair exists


if y.has_key? :first_name
    puts "Y has a key called :first_name"
else
    puts "There is no :first_name key"
end # => Y has a key called :first_name


if y.has_value? "Coding"
    puts "Y has a value called 'Coding'"
else
    puts "No 'Coding', only 'Dojo'"
end # => Y has a value called 'Coding'
