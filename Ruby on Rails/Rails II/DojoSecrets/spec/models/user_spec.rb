require 'rails_helper'

RSpec.describe User, type: :model do
    context "with valid attributes" do
        it "should save" do
            expect(build(:user)).to be_valid
        end

        it "encrypts the password into the password digest attribute" do
            expect(build(:user)).password_digest.present?).to eq(true)
        end

        it "downcases email" do
            expect(create(:user, email: 'Email@Email.com').email).to eq('email@email.com')
        end
    end

    context "with invalid attributes will not be saved" do
        it 'does not accept blank name field' do
            expect(build(:user, name: "")).to be_invalid
        end

        it 'does not accept blank email field' do
            expect(build(:user, email: "")).to be_invalid
        end

        it 'does not accept wrong format for email' do
            emails = %w[@ user@ @email.com]
            emails.each do |email|
                expect(build(:user, email: email)).to be_invalid
            end
        end

         it 'does not accept email if already registered' do
             create(:user)
             expect(build(:user)).to be_invalid
        end

        it 'does not accept blank password field' do
            expect(build(:user, password: "")).to be_invalid
        end

        it 'does not accept incorrect password confirmation' do
            expect(build(:user, password_confirmation: 'incorrect_password')).to be_invalid
        end
    end

    context 'relationships' do
        before do
            @user = create(:user)
            @secret = create(:secret, content: 'Secret #1', user: @user)
            @like = create(:like, secrete: @secret, user: @user)
        end

        it 'has secrets' do
            expect(@user.secrets).to include(@secret)
        end

        it 'has likes' do
            expect(@user.likes).to include(@like)
        end

        it 'has secretes through likes' do
            expect(@user.secrets_liked).to include(@secret)
        end
    end
end
