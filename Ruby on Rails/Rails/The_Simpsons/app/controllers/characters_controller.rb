class CharactersController < ApplicationController
    before_action :logged_in, only: [:create, :show]
    before_action :logged_in, except: [:index, :new]

    def index
      flash[:greeting] = "Eat my shorts!"
      @characters = Character.all
    end

    def new
      render layout: 'two col'
    end

    def edit
      @character = Character.find(params[:id])
      render layout: 'two_col'
    end

    def show
      puts params[:char_id] # whatever
    end

    def create
      char = Character.create( character_params )
      if char.valid?
          redirect_to '/'

      else
          flash[:errors] = char.errors.full_messages
          redirect_to '/characters/new'
      end
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
