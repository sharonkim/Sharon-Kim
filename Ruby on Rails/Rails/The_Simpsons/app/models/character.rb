class Character < ApplicationRecord
    validates :first_name, :last_name, :workplace, presence: true
    validates :first_name, :last_name, uniqueness: {scope: [:first_name, :last_name]}

    def full_name
        "#{first_name} #{last_name}"
    end
end
