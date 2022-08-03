from django.shortcuts import render,redirect
from . models import *
# Create your views here.

def index(request):
	return render(request,'index.html')

def contact(request):
	if request.method=="POST":
		Contact.objects.create(
			name=request.POST['fname'],
			email=request.POST['email'],
			subject=request.POST['subject'],
			message=request.POST['message'],
		)
		msg="contact Saved sucessfuly"
		contacts=Contact.objects.all().order_by("-id")[:5]
		return render(request,'contact.html',{'msg':msg,'contacts':contacts})
	else:
	    contacts=Contact.objects.all().order_by("-id")[:5]
	return render(request,'contact.html',{'contacts':contacts})

def about(request):
	return render(request,'about.html')

def doctors(request):
	doctors=Doctor_Profile.objects.all()
	return render(request,'doctors.html',{'doctors':doctors})

def doctor_details(request,pk):
	doctor=Doctor_Profile.objects.get(pk=pk)
	return render(request,'doctor_details.html',{'doctor':doctor})

def sign_up(request):
	if request.method=="POST":
		try:
			User.objects.get(email=request.POST['email'])
			msg="Email is already register"
			return render(request,'sign_up.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						password=request.POST['password'],
						address=request.POST['address'],
					)
				msg="sign up  sucessfuly"
				return render(request,'login.html',{'msg':msg})
			else:
				msg="password & confrim password does not matched"
				return render(request,'sign_up.html',{'msg':msg})
	else:
		return render(request,'sign_up.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(
				email=request.POST['email'],
				password=request.POST['password']
			)
			if user.usertype=="patient":
				request.session['email']=user.email
				request.session['fname']=user.fname
				appointment=Appointment.objects.filter(patient=user,status="pending")
				request.session['appointment_count']=len(appointment)
				return render(request,'index.html')
			else:
				request.session['email']=user.email
				request.session['fname']=user.fname
				# request.session['doctor_picture']=user.doctor_picture
				return render(request,'doctor_index.html')
		except Exception as e:
			print("=================================",e)
			msg="Email & password is incorrect"
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		return render(request,'login.html')
	except:
		return render(request,'login.html')

def change_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		if request.POST['opassword']==user.password:
			if request.POST['npassword']==request.POST['cnpassword']:
				user.password=request.POST['npassword']
				user.save()
				return redirect('logout')
			else:
				msg="new password & confrim new password does not matched"
				return render(request,'change_password.html',{'msg':msg})
		else:
			msg="old password does not matched"
			return render(request,'change_password.html',{'msg':msg})
	else:
		return render(request,'change_password.html')

def doctor_profile(request):
	doctor_profile=Doctor_Profile()
	doctor=User.objects.get(email=request.session['email'])
	try:
		doctor_profile=Doctor_Profile.objects.get(doctor=doctor)
	except:
		pass
	if request.method=="POST":
		if doctor_profile.doctor_speciality:
			doctor_profile.doctor=doctor
			doctor_profile.doctor_degree=request.POST['doctor_degree']
			doctor_profile.doctor_speciality=request.POST['doctor_speciality']
			doctor_profile.doctor_start_time=request.POST['doctor_start_time']
			doctor_profile.doctor_end_time=request.POST['doctor_end_time']
			doctor_profile.doctor_fees=request.POST['doctor_fees']
			try:
				doctor_profile.doctor_picture=request.FILES['doctor_picture']
			except:
				pass
			doctor_profile.save()
			msg="doctor profile updated sucessfuly"
			return render(request,'doctor_profile.html',{'doctor_profile':doctor_profile,'msg':msg})
		else:
			doctor_profile=Doctor_Profile.objects.create(
					doctor=doctor,
					doctor_degree=request.POST['doctor_degree'],
					doctor_speciality=request.POST['doctor_speciality'],
					doctor_start_time=request.POST['doctor_start_time'],
					doctor_end_time=request.POST['doctor_end_time'],
					doctor_fees=request.POST['doctor_fees'],
					doctor_picture=request.FILES['doctor_picture'],
				)
			doctor_profile.save()
			msg="doctor profile created sucessfuly"
			return render(request,'doctor_profile.html',{'doctor_profile':doctor_profile,'msg':msg})
	else:
		return render(request,'doctor_profile.html',{'doctor_profile':doctor_profile})

def book_appointment(request,pk):
	doctor=Doctor_Profile.objects.get(pk=pk)
	patient=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		Appointment.objects.create(
				doctor=doctor,
				patient=patient,
				date=request.POST['date'],
				time=request.POST['time'],
				health_issue=request.POST['Health_issue']
			)
		msg="Appointment book sucessfuly"
		appointment1=Appointment.objects.filter(patient=patient,status="pending")
		request.session['appointment_count']=len(appointment1)
		appointment=Appointment.objects.filter(patient=patient)
		patient1=User.objects.all()

		print(patient1)
		return render(request,'myappointment.html',{'msg':msg,'appointment':appointment})
	else:
		return render(request,'book_appointment.html',{'doctor':doctor,'patient':patient})

def myappointment(request):
	patient=User.objects.get(email=request.session['email'])
	appointment=Appointment.objects.filter(patient=patient)
	appointment1=Appointment.objects.filter(patient=patient,status="pending")
	request.session['appointment_count']=len(appointment1)
	return render(request,'myappointment.html',{'appointment':appointment})

def patient_cencel_appoinment(request,pk):
	appointment=Appointment.objects.get(pk=pk)
	if request.method=="POST":
		CencelAppointment.objects.create(
				appointment=appointment,
				reason=request.POST['reason']
			)
		appointment.status="cencelled by patient"
		appointment.save()
		return redirect("myappointment")
	else:
		return render(request,'patient_cencel_appoinment.html',{'appointment':appointment})

def doctor_index(request):
	return render(request,'doctor_index.html')

def health_profile(request):
	health_profile=HealthProfile()
	patient=User.objects.get(email=request.session['email'])
	try:
		health_profile=HealthProfile.objects.get(patient=patient)
	except:
		pass
	if request.method=="POST":
		diabetes=request.POST['diabetes']
		if diabetes=="yes":
			flag1=True
		else:
			flag1=False
		blood_pressure=request.POST['blood_pressure']
		if blood_pressure =="yes":
			flag2=True
		else:
			flag2=False

		health_profile=HealthProfile.objects.create(
				patient=patient,
				blood_group=request.POST['blood_group'],
				weight=request.POST['weight'],
				diabetes=flag1,
				blood_pressure=flag2
			)
		msg="HealthProfile Updated Sucessfuly"
		return render(request,'health_profile.html',{'msg':msg,'health_profile':health_profile})
	else:
		return render(request,'health_profile.html',{'health_profile':health_profile})

def doctor_appointment(request):
	doctor=User.objects.get(email=request.session['email'])
	doctor_profile=Doctor_Profile.objects.get(doctor=doctor)
	doctor_appointment=Appointment.objects.filter(doctor=doctor_profile)
	return render(request,'doctor_appointment.html',{'doctor_appointment':doctor_appointment})

def doctor_approve_appointment(request,pk):
	appointment=Appointment.objects.get(pk=pk)
	appointment.status="approve"
	appointment.save()
	return redirect('doctor_appointment')

def doctor_complete_appointment(request,pk):
	appointment=Appointment.objects.get(pk=pk)
	if request.method=="POST":
		appointment.prescription=request.POST['prescription']
		appointment.status="completed"
		appointment.save()
		return redirect('doctor_appointment')
	else:
		return render(request,'doctor_complete_appointment.html',{'appointment':appointment})
	# appointment.status="completed"
	
	

def doctor_cencel_appoinment(request,pk):
	appointment=Appointment.objects.get(pk=pk)
	appointment.status="cancelled by doctor"
	appointment.save()
	return redirect('doctor_appointment')


