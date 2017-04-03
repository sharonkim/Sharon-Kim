class Project
    attr_accessor :name, :description, :owner

    def elevator_pitch
        "#{@name}, #{@description}"
    end
end
