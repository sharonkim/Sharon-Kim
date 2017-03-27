class DojoController < ApplicationController
  def index
    @dojos = Dojo.all
    @count = Dojo.all.count
  end

  def new
    puts params[:dojo_id]
  end

  def create
    @dojo = Dojo.create(dojo_params)
    if @dojo.valid?

      redirect_to "/dojos"

    else
      flash[:error] = @dojo.errors.full_messages
      redirect_to "/dojos/new"
    end
  end

  def show
    @dojo = Dojo.find(params[:id])
    @students = Dojo.find(params[:id].students)
  end

  def edit
    @dojos = Dojo.find(params[:id])
  end

  def update
    Dojo.find(params[:id]).update(dojo_params)
    redirect_to "/dojos"
  end

  def destroy
    Dojo.find(params[:id]).destroy
    redirect_to "/dojos"
  end

  private
  def dojo_params
    param.require(:dojo).permit(:branch, :street, :city, :state, :action)
  end

end
