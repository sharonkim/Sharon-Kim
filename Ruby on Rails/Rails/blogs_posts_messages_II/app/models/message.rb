class Message < ApplicationRecord
  belongs_to :user
  belongs_to :post

  validates :author, :meassage:, presence: true
end
