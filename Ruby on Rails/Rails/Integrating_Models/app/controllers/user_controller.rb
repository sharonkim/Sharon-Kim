class UserController < ApplicationController
  def index
      render json: User.all
  end

  def new
  end

  def create
      @user = User.create(name:params[:name])
      redirect_to '/users'
  end

  def show
      render json: User.find(params[:id])
  end

  def edit
      @user = User.find(params[:id])
  end

  def update
      @user = User.find(params[:id]).update(name:params[:name])
      redirect_to '/users'
  end

  def total
      @count = User.count
      render :text => "#{@count} users"
  end
end
