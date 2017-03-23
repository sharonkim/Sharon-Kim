class Friendship < ApplicationRecord
  belongs_to :user, :foreigh_key => "user_id", class_name => "Users"
  belongs_to :freind, :foreigh_key => "friend_id", :clases_name
end => "friend_id", :class_name => "User"
S
