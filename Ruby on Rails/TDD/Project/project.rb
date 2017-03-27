class Project
    attr_accessor :name, :description, :owner, :tasks

    def initialize(name, description, owner)
        @name = name
        @description = description
        @owner = owner
        @tasks = String.new()
    end

    def elevator_pitch
        "#{@name}, #{@description}"
    end

    def tasks
      "#{@tasks}"
    end

    def add_task(tasks)
      @tasks << tasks
    end

    def print_tasks
      @tasks.each do
        "#{@tasks}"
    end
  end
end
