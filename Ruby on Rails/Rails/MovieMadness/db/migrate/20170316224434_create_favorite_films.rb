class CreateFavoriteFilms < ActiveRecord::Migration[5.0]
  def change
    create_table :favorite_films do |t|
      t.references :user, foreign_key: true
      t.references :film, foreign_key: true

      t.timestamps
    end
  end
end
