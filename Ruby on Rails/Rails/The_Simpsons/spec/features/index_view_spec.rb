require 'rails_helper'
feature "creating a new character" do
    scenario "successfully" do
        visit characters_new_path
        fill_in "character[first_name]", with "Robert"
        fill_in "character[last_name]", with "Terwilliger, Jr."
        fill_in "character[email]", with "Prison"
        click_button "Create Character"
        expect(page).to have_content "Robert Terwilliger, Jr. Prison"
    end

    scenario "unsuccessfully" do
        visit characters_new_path
        click_button "Create Character"
        expect(page).to have_content "First Name can\'t be blank"
        expect(page).to have_content "Last name can\'t be blank"
        expect(page).to have_content "Workplace can\'t be blank"
    end
end
