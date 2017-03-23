class HelloController < ApplicationController
  def index
      render :text => "What do you want me to say?"
  end

  def dojo
      render :text => "Hello CodingDojo!"
  end

  def say_hello
      render :text => "Saying Hello!"
  end

  def joe
      render :text => "Saying Hello Joe!"
  end

  def michael
      redirect_to action: :joe
  end

  def times
      if session[:count]
          session[:count] += 1
      else
          session[:count] = 1
      end

      render :text => "You visited this url #{session[:count]} times!"
  end

  def restart
      session.clear
      render :text => "Destroyed the session!"
  end
end
