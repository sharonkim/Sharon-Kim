class CreateCharacters < ActiveRecord::Migration[5.0]
  def change
    create_table :characters do |t|
      t.string :fname
      t.string :lname
      t.string :workplace

      t.timestamps
    end
  end
end
