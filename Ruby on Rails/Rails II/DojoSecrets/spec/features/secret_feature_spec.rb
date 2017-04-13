require 'rails_helper'

feature 'Secret Features' do
	before do
		@user1 = create(:user)
		@user2 = create(:user, email: 'email@email.com')
		@secret2 = create(:secret, user: @user2, content: 'Enter something interesting')
		log_in
	end
end

feature 'User\'s Secret Page' do
	before do
		visit '/users/#{@user.id}'
	end

	scenario 'unable to view other user\'s page' do
		expect(page).to_not have_text(@secret2.content)
	end

	scenario 'create secret' do
		fill_in 'Content', with: 'My secret'
		click_button 'Create Secret'

		expect(current_path).to eq('/users/#{@user.id}')
		expect(page).to have_text('My secret')
	end

	scenario 'destroy secret from profile and redirect to profile page' do
		secret = create(:secret, user: @user)
		visit '/users/#{@user.id}'
		click_button 'Delete Secret'

		expect(current_path).to eq('/users/#{@user.id}')
		expect(page).to_not have_text(@secret.content)
	end
end

feature 'Secret Dashboard' do
	before do
		@secret = create(:secret, user: @user)
	end

	before(:each) do
		visit '/secrets'
	end

	scenario 'display all user\'s secrets' do
		expect(page).to have_text(@secret.content)
		expect(page).to have_text(@secret2.content)
	end

	scenario 'destroy secret from index and redirect to ' do
		click_button 'Delete Secret'

		expect(current_path).to eq('/users/#{@user.id}')
		expect(page).to_not have_text(@secret.content)
	end
end
