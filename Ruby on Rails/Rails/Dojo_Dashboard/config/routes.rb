Rails.application.routes.draw do
    root "dojos#index"
    resources :dojos do
        resources :students
    end
    get 'dojos/new' => 'dojos#new'
    get 'dojos/:id' => 'dojojs#show'
    get 'dojos/:id/edit' => 'dojos#edit'
    post 'dojos' => 'dojo#create'
    patch 'dojos/:id' => 'dojo#update'
    delete 'dojos/:id' => 'dojos#destroy'
end
