def solve_quad(a, b, c):
    solns = []
    discrim = b**2 - 4*a*c
    solns.append( (-b + np.sqrt(discrim + 0j)) / (2*a) )
    solns.append( (-b - np.sqrt(discrim + 0j)) / (2*a) )
    return solns

a = float(raw_input("What is a? "))
b = float(raw_input("What is b? "))
c = float(raw_input("What is c? "))
solutions = solve_quad(a, b, c)
if solutions[0] == solutions[1]:
    print "Uh oh, there's only one root."
    print 'x1 = {0}\nx2 = {1}'.format(*solutions)
else:
    print "Here are your solutions:"
    print 'x1 = {0}\nx2 = {1}'.format(*solutions)
