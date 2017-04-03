require_relative 'bankaccount'


RSpec.describe BankAccount do
  before(:each) do
    @bank = BankAccount.new()
  end

  it 'has a getter method for retrieving the checking account balance' do
    expect{@bank.checking}.to_not raise_error(NoMethodError)
  end

  it 'has a getter method that retrieves the total account balance' do
    expect{@bank.total()}.not_to raise_error(NoMethodError)
  end

  it 'has a function that allows the user to withdraw cash' do
    @bank.deposit(500)
    @bank.withdraw(250)
    expect(@bank.checking).to eq(250)
  end

  it 'raises an error if a user tries to withdraw more money than they have in the account' do
    expect{@bank.withdraw(3 ** 100)}.to raise_error(InsufficentFundsError)
  end

  it 'raise an error when the user attempts to retieve the total number of bank accounts' do
    expect{@bank.count}.to raise_error(NoMethodError)
  end

  it 'raises an error when the user attempts to set the interest rate' do
    expect{@bank.interest = 3}.to raise_error(NoMethodError)
  end

end
