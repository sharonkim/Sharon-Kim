FactoryGirl.define do
  factory :user do
    last_name "Doe"
    admin false

    trait :male do
        first_name "John"
        full_name {"#{first_name} #{last_name}"}
        email "john@doe.com"
        age {rand(21..60)}
    end

    trait :female do
        first_name "Jane"
        full_name {"#{first_name} #{last_name}"}
        email "jane@doe.com"
        age {rand(21..60)}
    end

    trait :admin do
        admin true
    end
  end
end
