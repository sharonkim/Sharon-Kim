class Project
  attr_accessor :name, :description, :owner, :tasks


  def initialize(name, description, owner)
      @name = name
      @description = description
      @owner = owner
      @tasks = Array.new()
  end

  def elevator_pitch
      "#{@name}, #{@description}"
  end

  def add_task(task)
    @tasks << task
  end

  def print_tasks
    @tasks.each  do |t|
      puts t
    end
  end
end
