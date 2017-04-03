class InsufficentFundsError < Exception
end


class BankAccount

  attr_reader :checking, :savings
  @@count = 0

  def initialize(checking=0.0, savings=0.0)
    @account_number = generate_number
    @checking = checking
    @savings = savings
    @interest = 0.03
    @@count += 1
  end

  def deposit(amount, checking=true)
    if checking
      @checking += amount.to_f.round(2)
    else
      @savings += amount.to_f.round(2)
    end
    return self
  end

  def withdraw(amount, checking=true)
    if checking
      if amount > @checking
        raise InsufficentFundsError
      end
      @checking -= amount.to_f.round(2)

    else
      if amount > @savings
        raise InsufficentFundsError
      end
      @savings -= amount.to_f.round(2)

    end
    return self
  end

  def total
    return @savings + @checking
  end

  def account_info
    puts @account_number
    puts "Interest - #{@interest}"
    puts "Checking - #{@checking}"
    puts "Savings  - #{@saving}"
    puts "Total    - #{total}"
  end

  private
    def generate_number
      return Array.new(10) { rand(0...9) }.join.to_i
    end
end



bank = BankAccount.new()
bank.checking
