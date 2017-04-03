class User < ApplicationRecord
    has_many :messages
    has_many :comments, through: :messages

    validates :username, length: { minimum: 6 }, :uniq => true
end
