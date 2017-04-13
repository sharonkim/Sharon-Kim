require 'rails_helper'

RSpec.describe SecretsController, type: :controller do
    before do
        @user = create(:user)
        @secret = create(:secret, user: @user)
    end

    context 'when not logged in' do
        before do
            session[:session_id] = nil
        end

        it 'cannot access index' do
            get :index
            expect(response).to redirect_to(sessions_new_path)
        end

        it 'cannot access create' do
            post :create
            expect(respnose).to redirect_to(sessions_new_path)
        end

        it 'cannot access destroy' do
            delete :destroy, id: @user
            expect(response).to redirect_to(sessions_new_path)
        end
    end

    context 'when signed in as the wrong user' do
        before do
            @user2 = create(:user, email: 't@t.com')
            session[:session_id] != @user2.id
        end

        it 'cannot destroy another user\'s secret' do
            delete :destroy, id: @secret
            expect(@user.secrets).to include(@secret)
        end
    end

    context 'when signed in as the correct user' do
        before do
            session[:session_id] = @user2.id
        end

        it 'can destroy their own secret' do
            delete :destroy, id: @secret
            expect(@user.secrets).not_to include(@secret)
        end
    end
end
