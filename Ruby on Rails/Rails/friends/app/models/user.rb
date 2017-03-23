class User < ApplicationRecord
    has_many :friendships, :foreign_key => "user_id", :class_name => 'Friendships'
    has_many :friends, :through => :friendships
end
