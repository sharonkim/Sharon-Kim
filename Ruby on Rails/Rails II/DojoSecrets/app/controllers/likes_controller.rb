class LikesController < ApplicationController
    def create
        Like.create(params[:id], user: current_user)
        redirect_to '/secrets'
    end

    def destroy
        @like = Like.find(params[:id])

        if current_user == @like.user
            @like.destroy
        end
        redirect_to '/secrets'
    end
end
