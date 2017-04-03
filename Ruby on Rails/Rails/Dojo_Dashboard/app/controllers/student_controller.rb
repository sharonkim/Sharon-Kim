class StudentController < ApplicationController
    def new
        @dojos = Dojo.all
        @dojo = Dojo.find(params[:dojo_id])
    end

    def create
        @student = Student.new(student_params)

        if @student.save
            redirect_to "dojos/#{student.dojo_id}", notice: "You have successfully created a student!"

        else
            flash[:errors] = @student.errors.full_messages
            redirect_to :back
        end
    end

    def show
        @student = Student.with_dojo(params[:id])
        @cohort = Student.cohort(@student)
    end

    def edit
        @dojos = Dojo.all
        @student = Student.cohort(@student)
    end

    def update
        Student.find(params[:id])

        if @student.update(student_params)
            redirect_to dojo_student_path(@student.dojo_id, @student_id), notice: "You have successfully updated a student!"

        else
            flash[:errors] = @student.errors.full_messages
            redirect_to :back
        end
    end

    def destroy
        Student.find(params[:id]).destroy
        redirect_to :root
    end

    private
    def student_params
        params.require(:student).permit(:first_name, :last_name, :email, :dojo_id)
    end
end
