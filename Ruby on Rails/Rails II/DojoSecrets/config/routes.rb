Rails.application.routes.draw do
    root 'sessions#new'
    get 'sessions/new'
    post 'sessions' => 'sessions#create'
    delete 'sessions/:id' => 'sessions#destroy'

    get 'users/new'
    get 'users' => 'users#create'
    get 'users/:id' => 'users#show', as: 'users_show'
    get 'users/:id/edit' => 'users#edit', as: 'users_edit'
    patch 'users/:id' => 'users#update'
    delete 'users/:id' => 'users#destroy'

    get 'secrets' => 'secrets#index'
    get 'secrets' => 'secrets#create'
    delete 'secrets/:id' => 'secrets#destroy'

    post 'likes' => 'likes#create'
    delete 'likes/:id' => 'likes#destroy'

resources :sessions, only: [:new, :create, :destroy]
resources :users
resources :secrets, only: [:index, :create, :destroy]
resources :likes, only: [:create, :destroy]

# For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
