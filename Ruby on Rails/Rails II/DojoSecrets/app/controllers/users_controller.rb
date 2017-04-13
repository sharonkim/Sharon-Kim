class UsersController < ApplicationController
    before_action :require_login, except: [:new, :create]
    before_action :check_user, except: [:new, :create]

    def new
    end

    def create
        user = User.new( user_params )

        if user.save
            redirect_to sessions_new_path

        else
            flash[:errors] = user.errors_full_messages
            redirect_to users_new_path
        end
    end

    def update
    end

    def show
        @user = User.find(params[:id])
    end

    def edit
    end

    def destroy
    end

    private
    def user_params
        params.require(:user).permit(:name, :email, :password, :password_confirmation)
    end

    def check_user
        user_id = params[:id].to_i

        if user_id != session[:user_id])
        redirect_to users_show_path(session[:user_id])
    end
end
