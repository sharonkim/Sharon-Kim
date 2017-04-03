class Post < ApplicationRecord
    belongs_to :user
    belongs_to :blog

    has_many :messages
    has_many :comments, as: :commentable

    validates :content, :title, presence: true
end
