Rails.application.routes.draw do
    root "players#index"
    get "players" => "players#get_players"
    post "players" => "players#create"
    get "teams" => "teams#get_teams"

    # root "static_pages#index"
    # get 'static_pages/index'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
