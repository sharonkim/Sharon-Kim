class EventsController < ApplicationController
    before_action :require_login, only: [:edit, :update, :destroy]

    def index
        user = User.find(current_user.id)
        @local_events = Event.where(state: user.state)
        @other_events = Event.where.not(state: user.state)
    end

    def show
        event = Event.find(params[:id])
        user = event.users
        comments = event.comments
    end

    def create
        event = Event.create(event_params)

        if event.valid?
			event.save
        else
           flash[:errors] = event.errors.full_messages
       end
	   redirect_to events_index_path
    end

    def destroy
        event = Event.find(params[:id])
        event.destroy if event.user == current_user
        redirect_to events_index_path
    end

    def edit
        event = Event.find(params[:id])
        event.destroy if event.user == current_user
        redirect_to events_index_path
    end

    def update
        event = Event.find(params[:id])
        if event.update(event_params)
            redirect_to "/events/#{ @event.id }"
        else
            flash[:errors] = event.errors.full_messages
            redirect_to events_index_path
		end
    end

    private
        def event_params
            params.require(:event).permit(:name, :date, :location, :state).merge(user: current_user)
        end

        def require_login
            user_id = params[:id].to_i

            if user_id != session[:user_id]
                redirect_to root_path
			end
        end
end
