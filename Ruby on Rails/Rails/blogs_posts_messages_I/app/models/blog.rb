class Blog < ApplicationRecord
    has_many :posts

    # Validates fields have not been left blank
    validates :name, :description, presence: true
end
