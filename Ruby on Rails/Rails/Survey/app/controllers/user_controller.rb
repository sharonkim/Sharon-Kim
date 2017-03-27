class UserController < ApplicationController
  def index
      if request.post?
          session[:count] = 0 unless session.key?(:count)
          session[:count] += 1
          session[:data] = params[:data]
          flash[:success] = "Thanks for submitting this form! You have submitted this form #{session[:count]} times now."
      end
      return render 'index.html.erb'
  end

  def result
  end
end
