class CharactersController < ApplicationController
  def index
      flash[:greeting] = "Eat my shorts!"
      @characters = Character.all
  end

  def new
  end

  def edit
      @character = Character.find(params[:id])
      render layout: "two_col"
 end

  def show
      puts params[:char_id] # whatever
  end

  def create
    #   puts "We are here"
      Character.create( character_params )
      redirect_to "/"
  end

  def update
      @character = Character.find(params[:id])
      @character.update( character_params )
      redirect_to "/characters/#{params[:id]}"
  end

  private
  def character_params
      params.require(:character).permit(:fname, :lname, :workplace)
  end
end
