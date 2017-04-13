require 'rails_helper'

feature 'Like Features' do
	before do
		@user = create(:user)
		@secret = create(:secret, user: @user)
		log_in
	end
end

feature 'Secret does not earn a like' do
	before(:each) do
		visit '/secrets'
	end

	scenario 'update like count' do
		expect(page).to have_text(@secret.content)
		expect(page).to have_text('0 likes')
	end

	scenario 'like button displayed for unliked secret' do
		expect(page).to have_button('Like')
	end

	scenario 'like count updated and button removed when user likes secret' do
		click_button 'Like'

		expect(page).to_not have_button('Like')
		expect(page).to have_text('1 likes')
	end
end

feature 'Secret Liked' do
	before do
		@like = create(:like, user: @user, secret: @secret)
	end

	before(:each) do
		visit '/secrets'
	end

	scenario 'unlike button visible' do
		expect(page).to have_button('Unlike')
	end

	scenario 'like count updated when secret unliked' do
		click_button 'Unlike'

		expect(page).to_not have_button('Unlike')
		expect(page).to have_text('0 likes')
	end
end
