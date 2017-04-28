require 'open-uri'

players = [
    [first_name: "Michael", last_name: "Jordan"],
    [first_name: "Kobe", last_name: "Bryant"],
    [first_name: "Kevin", last_name: "Garnett"],
    [first_name: "LeBron", last_name: "James"],
    [first_name: "Stephen", last_name: "Curry"],
    [first_name: "Jordan", last_name: "Clarkson"],
    [first_name: "Derek", last_name: "Fisher"],
    [first_name: "Jimmy", last_name: "Butler"],
]

teams = [
    [name: "Boston Celtics"],
    [name: "Brooklyn Nets"],
    [name: "New York Knicks"],
    [name: "Philadelphia 76ers"],
    [name: "Toronto Rapters"],
    [name: "Chicago Bulls"],
    [name: "Cleveland Cavaliers"],
    [name: "Detroit Pistons"],
    [name: "Indiana Pacers"],
    [name: "Milwaukee Bucks"],
    [name: "Atlanta Hawks"],
    [name: "Charlotte Hornets"],
    [name: "Miami Heat"],
    [name: "Orlando Magic"],
    [name: "Washington Wizards"],
    [name: "Denver Nuggets"],
    [name: "Minnesota Timberwolves"],
    [name: "Oklahoma City Thunder"],
    [name: "Portland Trail Blazers"],
    [name: "Utah Jazz"],
    [name: "Golden State Warriors"],
    [name: "Los Angeles Clippers"],
    [name: "Los Angeles Lakers"],
    [name: "Phoenix Suns"],
    [name: "Sacramento Kings"],
    [name: "Dallas Mavericks"],
    [name: "Houston Rockets"],
    [name: "Memphis Grizzlies"],
    [name: "New Orleans Pelicans"],
    [name: "San Antonio Spurs"],
]

players.each do |player|
    player = Player.create!(:first_name => first_name, :last_name => last_name)
end

teams.each do |team|
    team = Team.create!(:name => name)
end

# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)
