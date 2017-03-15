class BankAccount
  attr_reader :account_number, :checking, :saving

  @@bank_accounts = 0

  def initialize
    @account_number = create_account
    @checking = 0
    @saving = 0
    @@bank_accounts += 1
    @interest_rate = 0.01 # not accessible to user
  end

  def deposit(account, amount)
    if account.downcase == "checking"
      @checking += amount
    else
      @saving += amount
    end
  end

  def withdrawal(account, amount)
    if account.downcase == "checking"
      if @checking - amount < 0
        raise "Insufficient Funds, you have #{@checking} in this account"
      else
        @checking -= amount
      end
    else
      if @saving - amount < 0
        raise "Insufficient Funds, you have #{@saving} in this account"
      else
        @saving -= amount
      end
    end
  end

  def total
    "Checking Balance: #{@checking}\nSaving Balance: #{@saving}\nTotal Balance: #{@checking + @saving}"
  end

  def account_information
    "Account Number: #{@account_number}\nInterest Rate: #{@interest_rate}\n#{self.total}"
  end

  private
    def create_account
      Array.new(10).map { rand(1..9) }.join
    end
end

# class BankAccount
#     attr_reader :account_number, :checking, :savings
#     @@bank_accounts = 0
#
#     def initialize
#         @account_number = create_account
#         @checking = 0
#         @savings = 0
#         @@bank_accounts += 1
#         @interest_rate = 0.01 # Not accessible by user
#     end
#
#     def deposit(account, amount)
#         if account.downcase == "checking"
#             @checking += amount
#
#         else
#             @savings += amount
#         end
#     end
#
#     def withdraw(account, amount)
#         if account.downcase == "checking"
#             if @checking - amount < 0
#                 raise "Insufficient Funds, you have #{@checking} in this account"
#
#             else
#                 @checking -= amount
#             end
#
#         else
#             if @savings - amount < 0
#                 raise "Insufficient Funds, you have #{@savings} in this account"
#
#             else
#                 @savings -= amount
#             end
#         end
#     end
#
#     def total
#         "Checking Balance: #{@checking}\nSavings Balance: #{@savings}\nTotal Balance: #{@checking + @savings}"
#     end
#
#     def account_information
#         "Account Information: #{@account_number}\mnInterest Rate: #{@interest_rate}\n#{self.total}"
#     end
#
#     private
#         def create_account
#             Array.new(10).map { rand(1..9) }.join
#         end
# end
