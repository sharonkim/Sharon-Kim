require 'rails_helper'

RSpec.describe Character, type: :model do
    it 'must provide first name' do
        @char = Character.new(first_name: '', last_name: 'Simpson', workplace: 'Nuclear Plant')
        expect(@char).to be_invalid()
    end

    it 'must provide last name' do
        @char = Character.new(first_name: 'Homer', last_name: '', workplace: '')
        expect(@char).to be_invalid()
    end

    it 'must be unique in table' do
        # white a character in
        @char1 = Character.create(first_name: 'Homer', last_name: 'Simpson', workplace: 'Nuclear Plant')
        # try to write the same character in again
        @char2 = Character.create(first_name: 'Homer', last_name: 'Simpson', workplace: 'Nuclear Plant')
        expect(@char2.valid?).to eq(false)
    end

    it 'must have a method called full_name that displays full name' do
        @char = Character.create(first_name: 'Homer', last_name: 'Simpson', workplace: 'Nuclear Plant')
        expect(@char.full_name).to eq('Homer Simpson')
    end
end
