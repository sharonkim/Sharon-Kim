class Post < ApplicationRecord
    has_many :messages
    belongs_to :blog
    # Validates fields are not blank and/or contain the minimum character length
    validates :content, presence: true
    validates :title, length: { minimum: 7 }
end
