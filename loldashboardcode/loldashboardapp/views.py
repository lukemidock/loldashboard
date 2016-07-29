
from django.shortcuts import render_to_response, render
from django.template import RequestContext


def index(request):
    return render(request, 'index.html')

def sqroot(a1, b1, c1):
	sqr = float(b1 ** 2 - 4 * a1 * c1)
	sqr = sqr ** .5
	return sqr

def numerator(B, sqr):
	top1a = float(B - B * 2 + sqr)
	top2a = float(B - B * 2 - sqr)
	return top1a, top2a

def finish(top, A):
	answer1 = top / (2 * A)
	return answer1

def check_input(usrinput):
	spliusrinput = None
	if '/' in str(usrinput):
		spliusrinput = usrinput.split('/', 1)
		num = spliusrinput[0]
		denom = spliusrinput[1]
		output = float(num) / float(denom)
		return output
	else:
		output = float(usrinput)
		return output

def quadratic_calculation(request):
	if request.method == 'POST':
		a1 = request.POST['a1']
		b1 = request.POST['b1']
		c1 = request.POST['c1']
		
		a1 = check_input(a1)
		b1 = check_input(b1)
		c1 = check_input(c1)
		sqr = sqroot(a1, b1, c1)
		top1a, top2a = numerator(b1, sqr)
		answer1 = finish(top1a, a1)
		answer2 = finish(top2a, a1)

		context_data = {
		"answer1": answer1,
		"answer2": answer2,
		}

		return render(request, 'quadratic_result.html', context_data)

