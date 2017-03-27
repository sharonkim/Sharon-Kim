class TimesController < ApplicationController
  def main
      @time = Time.new.strftime("%b %d, %Y %I:%M %p")
  end
end
