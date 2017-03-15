require_relative "human"

class Samurai < Human
    @@count = 0

    class << self
        attr_accessor :count

        def initialize
            super
            @health = 200
            self.count += 1
            self
        end

        def death_blow(obj) # If used on another object, the attacked object's health will be decreased to 0
            if obj.class.ancestors.include?(Human)
                obj.health = 0
                true
            else
                false
        end

        def meditate
            @health = 200
            self
        end

        def how_many
            if self.class.count > 1
                puts "There are #{self.class.count} samurai"

            else
                self.class.count = 1
                puts "There is 1 samurai"
        end
    end
end
