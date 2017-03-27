Rails.application.routes.draw do
  get '/ninja_gold/index' => "ninja_gold#index"

  post '/ninja_gold/index' => "ninja_gold#index"

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
