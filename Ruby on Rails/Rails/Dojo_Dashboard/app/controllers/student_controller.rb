class StudentController < ApplicationController
  def index
    redirect_to '/dojos/:dojo_id'
  end

  def new
    @dojo = Dojo.find(params[:dojo_id])
    @all_dojos = Dojo.all
  end

  def create
    @student = Student.create(student_params)

    if @student.valid?
      redirect_to "/dojos"

    else
      redirect_to action: "new", dojo_id: params[:dojo_id]
    end
  end

  def show
    @student = Student.find(params[:id])
    @dojo = Dojo.find(params[:dojo_id])
    @all_students = Dojo.find(params[:dojo_id]).students.where.not(id: @student.id)
  end

  def edit
    @student = Student.find(params[:id])
    @dojo = Dojo.find(params[:dojo_id])
    @all_dojos = Dojo.all
  end

  def update
    Student.find(params[:id]).update(student_params)
    redirect_to "/dojos"
  end

  def destroy
    Student.find(params[:id]).destroy
    redirect_to "/dojos"
  end

  private
    def student_params
      params.require(:student).permit(:first_name, :last_name, :email, :dojo_id)
    end
end
