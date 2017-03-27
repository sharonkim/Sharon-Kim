require_relative 'project'

RSpec.describe Project do
  before(:each) do
    # updated this block to create two projects
    @project1 = Project.new('Project 1', 'description 1', 'owner 1')
    @project2 = Project.new('Project 2', 'description 2', 'owner 2')
  end

  it 'has a getter and setter for name attribute' do
    @project1.name = "Changed Name"
    expect(@project1.name).to eq("Changed Name")
    @project2.name = "Changed Name"
    expect(@project2.name).to eq("Changed Name")
  end

  it 'has a method elevator_pitch to explain name and description' do
    expect(@project1.elevator_pitch).to eq("Project 1, description 1")
    expect(@project2.elevator_pitch).to eq("Project 2, description 2")
  end

  it 'has a getter and setter for owner attribute' do
    @project1.owner = "Sharon Kim"
    expect(@project1.owner).to eq("Sharon Kim")
  end

  it 'has a method add_tasks that pushes a task to the task attribute' do
    @project1.add_tasks("Must...Sleep...")
    expect(@project1.add_tasks).to eq("Must...Sleep...")
  end

  it 'has a method print_tasks that prints each task in the tasks attribute' do
    @project1.print_tasks("Sweat. Code. Sleep(not really).")
    @project1.print_tasks("Repeat...")
    expect(@project1.print_tasks).to eq(["Sweat. Code. Sleep(not really).", "Repeat..."])
  end
end
