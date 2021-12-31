from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

portfolio = [

	{
		'Coin' : 'Ethereum',
		'Balance' : 1.2,
	},

	{
		'Coin' : 'Solana',
		'Balance' : 13,
	}

]

@login_required
def home(request):
	context = {
		'portfolio' : portfolio
	}
	return render(request, 'crypto/home.html', context) # Can pass info in context