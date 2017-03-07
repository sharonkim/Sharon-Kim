
number = 25

def guess_number(guess)
    puts number
    if guess > number
        puts "Guess was too high!"

    elsif guess < number
        puts "Guess was too low!"

    elsif guess = number
        puts "You got it!"
    end

end

guess(1)
