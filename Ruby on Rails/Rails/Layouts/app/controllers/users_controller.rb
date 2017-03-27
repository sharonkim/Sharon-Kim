class UsersController < ApplicationController
  def index
    render layout: "two_col"
  end

  def create
    puts params
    redirect_to '/'
  end

  private
  def protect_params
    params.require(:user).permit(:first_name, :last_name, :favorite_language)
  end
end
