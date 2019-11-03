def countdown(n):
	if n <= 0:
		print('Racket is vertrokken!')
	else:
		print(n)
		countdown(n-1)

countdown(10);
