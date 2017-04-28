class TeamsController < ApplicationController
    def index
        render :json => Team.all
    end

    def get_teams
        render json: Team.all
    end
end
