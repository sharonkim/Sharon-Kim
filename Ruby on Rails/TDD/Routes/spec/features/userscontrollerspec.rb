require 'rails_helper'

Rspec.describe UsersController, type: :controller do
    it "routes/users/index to the users controller" do
        expect(:get => "/users/index").to route_to(:controller => "users", :action => "index")
    end

    it "routes/users/:id to users profile" do
        expect(:get => "/users/1").to route_to(:controller => "users", :action => "show", :id => "1")
    end
end
