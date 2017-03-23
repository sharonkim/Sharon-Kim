class TimesController < ApplicationController
  def main
      render :long => '%B %d, %Y'
      render
  end
end
