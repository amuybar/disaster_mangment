from django.shortcuts import render, redirect
from .models import DisasterReport
from .forms import DisasterReportForm

def report_disaster(request):
    if request.method == 'POST':
        form = DisasterReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DisasterReportForm()
    return render(request, 'report_disaster.html', {'form': form})
