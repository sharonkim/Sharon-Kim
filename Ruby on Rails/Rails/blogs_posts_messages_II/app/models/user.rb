class User < ApplicationRecord
    EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i

    has_many :owners
    has_many :messages
    has_many :posts
    # All blogs belonging to a specific User
    has_many :blogs, through: :owners
    # All blogs with posts by a specific User
    has_many :blog_posts, through: :posts, source: :blog_posts
    has_many :comments, as: :commentable

    validates :first_name, :last_name, :email, presence: true
    validates :email, uniqueness: { case_sensitive:false }, format: {with: EMAIL_REGEX}
end
