class User < ApplicationRecord
	validates :first_name, :last_name, :email, :age, presence: true
	validates_length_of :first_name, :last_name, minimum: 2
	validates_numericality_of :age, greater_than: 10, less_than: 150
end
