class UsersController < ApplicationController
    def new
    end

    def create
        user = User.new( user_params )

        if user.save
            session[:user_id] = @user.id
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
