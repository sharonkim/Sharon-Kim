Rails.application.routes.draw do
  get 'student/index'

  get 'student/new'

  get 'student/create'

  get 'student/show'

  get 'student/edit'

  get 'student/update'

  get 'student/destroy'

  get 'dojos' => 'dojos#index'

  get 'dojos/new' => 'dojos#new'

  post 'dojos' => 'dojo#create'

  get 'dojos/:id' => 'dojojs#show'

  get 'dojos/edit' => 'dojos#edit'

  patch 'dojos/:id' => 'dojo#update'

  delete 'dojos/:id' => 'dojos#destroy'

  get 'dojos/:dojo_id/students' => 'student#index'

  get 'dojos/:dojo_id/students/new' => 'student#new'

  post 'dojos/:dojo_id/students' => 'student#create'

  get 'dojos/:dojo_id/students/:id' => 'student#show'

  get 'dojos/:dojo_id/students/:id/edit' => 'student#edit'

  patch 'dojos/:dojo_id/students/:id' => 'student#update'

  delete 'dojos/:dojo_id/students/:id' => 'student#destroy'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
