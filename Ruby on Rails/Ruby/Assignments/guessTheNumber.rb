def guess_number(guess)
    number = 25

    if guess == number
        puts "You got it!"

    elsif guess > number
        puts "Guess is too high!"

    else
        puts "Guess is too low!"

    end
end
}

guess_number(19)
guess_number(83)
guess_number(25)
