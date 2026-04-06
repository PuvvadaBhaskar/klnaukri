from django.shortcuts import render, redirect
from .models import EmployeeDetails

# HOME PAGE
def home(request):
    return render(request, 'employeapp/employehomepage.html')


# CRUD PAGE
def crud(request):
    employees = EmployeeDetails.objects.all()
    return render(request, 'employeapp/crud.html', {'employees': employees})



# INSERT DATA
def crud_insert(request):
    if request.method == "POST":
        empid = request.POST['empid']
        empname = request.POST['empname']
        emploc = request.POST['emploc']
        empphone = request.POST['empphone']
        empemail = request.POST['empemail']

        EmployeeDetails.objects.create(
            employee_id=empid,
            employee_name=empname,
            employee_location=emploc,
            empoyee_phone=empphone,   # same spelling as model
            employee_email=empemail
        )

        return redirect('crud')

    return render(request, 'employeapp/crud.html')
def read_employee(request):
    employees = EmployeeDetails.objects.all()
    selected_emp = None

    if request.method == "POST":
        read_emp = request.POST['read_empid']
        selected_emp = EmployeeDetails.objects.filter(employee_id=read_emp).first()

    context = {
        'employees': employees,
        'selected_emp': selected_emp
    }

    return render(request, 'employeapp/crud.html', context)
def update_employee(request):
    employees = EmployeeDetails.objects.all()
    update_emp = None
    update_msg = ""

    # Fetch employee
    if request.method == "POST" and "fetch" in request.POST:
        empid = request.POST.get("empid")
        update_emp = EmployeeDetails.objects.get(employee_id=empid)

    # Update employee
    if request.method == "POST" and "update" in request.POST:
        empid = request.POST.get("empid")
        emp = EmployeeDetails.objects.get(employee_id=empid)

        emp.employee_name = request.POST.get("empname")
        emp.employee_location = request.POST.get("emploc")
        emp.employee_phone = request.POST.get("empphone")
        emp.employee_email = request.POST.get("empemail")
        emp.save()

        update_msg = "Employee Updated Successfully"

    return render(request, "employeapp/crud.html", {
        "employees": employees,
        "update_emp": update_emp,
        "update_msg": update_msg
    })
def delete_employee(request):
    employees = EmployeeDetails.objects.all()
    message = None

    if request.method == "POST":
        empid = request.POST.get("employee_id")   # get from form

        emp = EmployeeDetails.objects.filter(employee_id=empid).first()

        if emp:
            emp.delete()
            message = f"Employee {empid} deleted successfully"
        else:
            message = "Employee not found"

    return render(request, "employeapp/crud.html", {
        "employees": employees,
        "delete_msg": message
    })