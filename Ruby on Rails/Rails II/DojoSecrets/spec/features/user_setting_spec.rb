require 'rails_helper'
feature 'User Settings features' do
	before do
		@user = create(:user)
		log_in
	end
end

feature 'User Settings Dashboard' do
	before(:each) do
		visit '/users/#{@user.id}/edit'
	end

	scenario 'visits edit page' do
		expect(page).to have_field('email')
		expect(page).to have_field('name')
	end

	scenario 'valid information entered' do
		expect(find_field('name').value).to eq(@user.name)
		expect(find_field('email').value).to eq(@user.email)
	end

	scenario 'update information invalid' do
		fill_in 'Name', with: 'Incorrect name'
		fill_in 'Email', with: 'Invalid email format'
		click_button 'Update'

		expect(current_path).to eq('/users/#{@user.id}/edit')
		expect(page).to have_text('Email is invalid')
	end

	scenario 'valid information update' do
		fill_in 'Name', with: 'Alternate name'
		fill_in 'Email', with: 'email@email.com'
		click_button 'Update'

		expect(page).to have_text('Alternate name')
	end

	scenario 'destroys user and redirects to registration page' do
		click_button 'Delete User'

		expect(current_path).to eq('/users/new')
	end
end
