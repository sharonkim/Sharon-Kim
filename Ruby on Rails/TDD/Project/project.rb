class Project
    attr_accessor :name, :description, :owner, :tasks

    def initialize(name, description, owner)
        @name = name
        @description = description
        @owner = owner
        @tasks = Array.new
    end

    def elevator_pitch
        "#{@name}, #{@description}"
    end

    def tasks
      "#{@tasks}"
    end

    def add_tasks(tasks)
      @tasks << tasks
    end

    def print_tasks(tasks)
      @tasks.each do |task|
        "#{@tasks}"
    end
  end
end
