class NinjaGoldController < ApplicationController
  def initialize
      super
      @action = {
          "farm" => lambda { rand(10..20) },
          "cave" => lambda { rand(5..10) },
          "house" => lambda { rand(2..5) },
          "casino" => lambda { rand(-50..50) }
      }
  end

  def index
      session[:gold] || = 0
      session[:history] || = []

      if request.post?
          unless @actions.key?(params[:activity])
              flash[:error] = "Action is not supported"
              render 'index.html.erb'
          end

        gold = @actions[params[:activity]].call if @actions.key?(params[:activity])
        session[:gold] += gold

        event = ["gain", "Earned #{gold} from the farm! (#{Time.zone.now})"]

        if gold < 0
          event = ["loss", "Entered a casino and lost #{gold * -1}...Ouch... (#{Time.zone.now})"]
        end

        session[:history].unshift(event)
      end
  end
end
