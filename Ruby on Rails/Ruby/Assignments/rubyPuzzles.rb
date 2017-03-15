# Create an array with the following values: 3,5,1,2,7,9,8,13,25,32. Print the sum of all numbers in the array. Also have the function return an array that only include numbers that are greater than 10 (e.g. when you pass the array above, it should return an array with the values of 13,25,32 - hint: use reject or find_all method).
num_arr = [3, 5, 1, 2, 7, 9, 8, 13, 25, 32]
puts num_arr.reduce(:+)
puts num_arr.reject { |num| num < 10 }

# Create an array with the following values: John, KB, Oliver, Cory, Matthew, Christopher. Shuffle the array and print the name of each person. Have the program also return an array with names that are longer than 5 characters.
person_arr = ["John", "KB", "Oliver", "Cory", "Matthew", "Christopher"]
person_arr.shuffle.each { |person| print person }
print person_arr.select { |person| person.length > 5 }

# Create an array that contains all 26 letters in the alphabet (this array must have 26 values). Shuffle the array and display the last letter of the array. Have it also display the first letter of the array. If the first letter in the array is a vowel, have it display a message.
alpha_arr = ("a".."z").to_a
puts alpha_arr.shuffle.last
puts alpha_arr.shuffle.first
new_arr = alph_arr.shuffle
puts "#{new_arr.first} is a vowel" if ["a", "e", "i", "o", "u"].include? new_arr.first


# Generate an array with 10 random numbers between 55-100 and have it be sorted (showing the smallest number in the beginning). Display all the numbers in the array. Next, display the minimum value in the array as well as the maximum value.
rand_arr = []
10.times {rand_arr << rand(55..100) }
print rand_arr.sort
print rand_arr.max
print rand_arr.min

# Create a random string that is 5 characters long (hint: (65+rand(26)).chr returns a random character)
str = ""
5.times { str << rand(65..90).chr }
puts str

# Generate an array with 10 random strings that are each 5 characters long
str_arr = []
10.times do
    str = ""
    5.times { str << rand(65..90).chr }
    str_arr << str
end
print str_arr
