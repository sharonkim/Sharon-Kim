require 'rails_helper'

feature 'Authentication' do
	before do
		@user = create(:user)
	end
end

feature 'user sign-in' do
	scenario 'visit sign-in page' do
		visit '/sessions/new'

		expect(page).to have_field('email')
		expect(page).to have_field('password')
	end

	scenario 'successful validation logs in user' do
		log_in

		expect(current_path).to eq('/users/#{@user.id}')
		expect(page).to have_text(@user.name)
	end

	scenario 'failed validation does not login user' do
		log_in email: 'invalid email'
		log_in password: 'invalid password'

		expect(current_path).to eq('/sessions/new')
		expect(page).to have_text('Invalid Email or Password. Please try again.')
	end
end

feature 'User Logout' do
	before do
		log_in
	end

	scenario 'Log Out button displayed while user logged in' do
		expect(page).to have_button('Log Out')
	end

	scenario 'user logged out and redirected to login page' do
		click_button 'Log Out'

		expect(current_path).to eq('/sessions/new')
	end
end
