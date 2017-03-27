class User < ApplicationRecord
  validates :first_name, :last_name, :favorite_language, presence: true
end
