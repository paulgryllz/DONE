def first_function():
	'''
	(NoneType) -> str
	Return the string 'I can write code!'.
	
	>>> first_function()
	'I can write code!'

	Hint: this is not a trick question -- just a really easy one. If you are wondering what
	NoneType means, it indicates that there are no arguments - no types are
	being passed.
	'''
	return 'I can write code!'
	 
	 
def volume_triangular_prism(b, h, l):
	'''
	(number, number, number) -> float
	 Return the volume of a prism with a triangle base. The dimensions of the 
	 triangle are base b and height h. The prism has length l.

	>>> volume_triangular_prism(1, 2, 3)
	3.0
	>>> volume_triangular_prism(3, 4, 3.5)
	21.0
	'''
	return 0.5*b*h*l
	
def area_square(s):
	'''
	(number) -> float
	Return the area of the square with side length s. 
	
	>>> area_square(1)
	1.0
	>>> area_square(4.5)
	20.25
	'''
	return s*s
	 
def area_cube(s):
        '''
        (number) -> float
	Return the surface area (sum of the area of the faces) of a cube with
        side length s. Requirement: Use your function area_square().
        > area_cube(1)
        6.0
        > area_cube(5)
        150.0
        '''
        area_square = s*s
        # Defining area_square as area * area for the code to process it
        # and return s*s when used in a function
        return float(6*area_square)