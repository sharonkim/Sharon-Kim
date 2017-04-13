class User < ApplicationRecord
    has_secure_password

    has_many :secrets
    has_many :likes, dependent: :destroy
    has_many :secrets_liked, through: :likes, source: :secret

    validates :name, :email, presence: true
    validates :email, :format => { :with => /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i }, :uniqueness => { :case_sensitive => false }

    before_save :downcase_email

    private
        def downcase_email
            self.email.downcase!
        end
end
