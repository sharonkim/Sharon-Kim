class SecretsController < ApplicationController
    before_action :require_login

    def index
        @secrets = Secret.all
    end

    def create
        secret = current_user.secrets.new(secret_params)

        if secret.save
            redirect_to users_show_path :id => current_user.id

        else
        end
    end

    def destroy
        if session[:user_id] == Secret.find(params[:id]).user_id
            Secret.find(params[:id]).destroy
        end
        redirect_to users_show_path :id => current_user.id
    end
end
