class User < ApplicationRecord
    EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i

    has_many :ownders
    has_many :messages
    has_many :posts
    # All blogs belonging to a specific User
    has_many :blogs, through: :ownders
    # All blogs with posts by a specific User
    has_many :blog_posts, through: :posts, source: :blog_posts

    validates :email, uniqueness: { case_sensitive:false }, format: {with: EMAIL_REGEX}
    valideates :first_name, :last_name, :email, presence: true
end
