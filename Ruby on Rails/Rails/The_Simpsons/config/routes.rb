Rails.application.routes.draw do
    root 'characters#index'

    get 'characters/index'

    get 'characters/new'

    get 'characters/edit'

    get 'characters/whatever' => 'characters#new'

    get 'characters/:id' => 'characters#edit'

    post 'characters' => 'characters#create'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
