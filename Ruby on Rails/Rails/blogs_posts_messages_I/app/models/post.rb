class Post < ApplicationRecord
    belongs_to :blog

    has_many :messages

    # Validates fields are not blank and/or contain the minimum character length
    validates :content, presence: true
    validates :title, length: { minimum: 7 }
end
