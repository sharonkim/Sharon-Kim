class AddColumnToFilm < ActiveRecord::Migration[5.0]
  def change
    add_column :films, :director, :string
  end
end
