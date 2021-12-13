from django.shortcuts import render, redirect

# Create your views here.
from .models import Member
from django.views import generic
from django.shortcuts import get_object_or_404

def index(request):
    """View function for home page of site."""

    # Generate countsof the main objects
    num_members = Member.objects.all().count()
    
    # Generate main objects
    all_members = Member.objects.all()
    
    # Admin members (status = 'a')
    admin_members = Member.objects.filter(role__exact='a')


    context = {
        'num_members': num_members,
        'admin_members': admin_members,
        'all_members': all_members,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class MemberDetailView(generic.DetailView):
    model = Member
    
    
def edit_member(request, pk):
    """View function for editing member details."""
    member = get_object_or_404(Member, pk=pk)

    # If this is a POST request then process the data in request
    if request.method == 'POST':
        # If delete button has been clicked
        if 'delete_member' in request.POST:
            member.delete()
            return redirect('/')
        # If save button has been clicked
        elif 'save_member' in request.POST:
            # Populate fields with data from the request
            member.first_name = request.POST['first_name']
            member.last_name = request.POST['last_name']
            member.email_address = request.POST['email_address']
            member.phone_number = request.POST['phone_number']
            member.role = request.POST['role']
            member.save()

            return redirect('/')

    return render(request, 'catalog/member_detail.html', {'member': member})
    
def add_member(request):
    """View function for add a new member."""
    # If this is a POST request then process the data in request
    if request.method == 'POST':
        # Create a new Member object with the data
        new_member = Member(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email_address=request.POST['email_address'],
            phone_number=request.POST['phone_number'],
            role=request.POST['role'],
            )
        new_member.save()
        return redirect('/')

    return render(request, 'catalog/member_add.html')