class PlayersController < ApplicationController
  def index
  end

  def get_players
      render json: Player.all
  end

  def create
      player = Player.create(first_name: params[:player]['first_name'], last_name: params[:player][:last_name])
      redirect_to "/players"
  end
end
