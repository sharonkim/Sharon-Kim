class Message < ApplicationRecord
    belongs_to :post

    # Validates that fields are not left blank and/or contain  the minimum character length
    validates :author, :message, presence: true
end
