class Person
    attr_accessor :first_name
    def initialize names
        @first_name = name
    end
end

a = Person.new "Michael"

puts a.first_name

a.first_name = 'Charlie'

puts a.first_name


# a = {first_name: "Michael", last_name: "Choi"}
# b = {first_name: "John", last_name: "Doe"}
# c = {first_name: "Jane", last_name: "Doe"}
# d = {first_name: "James", last_name: "Smith"}
# e = {first_name: "Jennifer", last_name: "Smith"}
# names = [a, b, c, d, e]
#
# puts "You have #{names.length} names in the 'names' array"
#
# def names.each
#     for i in 0...self.length
#         yield self[i]
#     end
# end
#
# names.each { |i| puts "The first name #{i[:first_name]} is #{i[:last_name].length) characters long" }
# names.each { |i| puts "Last name: #{i[:last_name]}" }


# DECLARATIVE
# names.each { |i| puts "The name is #{i[:first_name]} #{i[:last_name]}" }
#

# names.each do |i|
#     puts "The name is #{i[:first_name]} #{i[:last_name]}"

#
# # IMPERATIVE
# for i in 0...names.length
#     puts "The name is #{names[i][:first_name]} #{names[i][:last_name]}"
# end


# puts "The name is '#{a[:first_name]} #{a[:last_name]}'"
# puts "The name is '#{b[:first_name]} #{b[:last_name]}'"
# puts "The name is '#{c[:first_name]} #{c[:last_name]}'"
# puts "The name is '#{d[:first_name]} #{d[:last_name]}'"
# puts "The name is '#{e[:first_name]} #{e[:last_name]}'"
