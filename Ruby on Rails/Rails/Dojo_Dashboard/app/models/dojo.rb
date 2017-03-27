class Dojo < ApplicationRecord
  has_many :students
  validates :branch, :street, :city, :state, presence: true

  before_destroy :destroy_students

  private
    def destroy_students
      Student.where(dojo:self.id).destroy_all
    end
end
