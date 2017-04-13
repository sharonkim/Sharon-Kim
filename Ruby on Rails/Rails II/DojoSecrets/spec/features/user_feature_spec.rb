require 'rails_helper'

feature 'User features' do
	before do
		@user = create(:user)
	end
end

feature 'register user' do
	before(:each) do
		visit '/users/new'
	end

	scenario 'user visits registration page' do
		expect(page).to have_field('name')
		expect(page).to have_field('email')
		expect(page).to have_field('password')
		expect(page).to have_field('password_confirmation')
	end

	scenario 'failed validations redirects user to login page' do
		click_button 'Join'

		expect(current_path).to eq('/users/new')
		expect(page).to have_text('Information cannot be left blank')
	end

	scenario 'successful validations create user and redirects to login page' do
		fill_in 'Email', with: 'email@email.com'
		fill_in 'Name', with: 'Aphmau'
		fill_in 'Password', with: 'password'
		fill_in 'password_confirmation', with: 'password'
		click_button 'Join'

		expect(current_path).to eq('/sessions/new')
	end
end

feature 'User dashboard' do
	before do
		log_in
	end

	scenario 'displays user information' do
		expect(page).to have_text('#{@user.name}')
		expect(page).to have_link('Edit Profile')
	end
end
