require 'rails_helper'

RSpec.describe User do
    context "With valid attributes" do
        it 'should save' do
            user = User.new(
                first_name: 'Shane',
                last_name: 'Change',
                email: 'schange@codingdojo.com'
            )
            expect(user).to be_valid
        end
    end

    context "With invalid attributes" do
        it 'should not save if first_name field is blank' do
            user = User.new(
                first_name: '',
                last_name: 'Change',
                email: 'schange@codingdojo.com'
            )
            expect(user).to be_invalid
        end

        it 'should not save if last_name field is blank' do
            user = User.new(
                first_name: 'Shane',
                last_name: '',
                email: 'schange@codingdojo.com'
            )
           expect(user).to be_invalid
        end

        it 'should not save if email already exists' do
            user1 = User.create(
                first_name: 'Shane',
                last_name: 'Change',
                email: 'schang@codingdojo.com'
            )
            user2 = User.create(
                first_name: 'Sean',
                last_name: 'Chang',
                email: 'schang@codingdojo.com'
            )
            expect(user2).to be_invalid
        end

        it 'should not save if invalid email format' do
            user = User.new(
                first_name: 'Shane',
                last_name: 'Chang',
                email: 'schang@codingdojo'
            )
            expect(user).to be_invalid
        end
    end
end
