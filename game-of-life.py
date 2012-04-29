import sys
import os
import copy

if len(sys.argv) < 3:
  sys.stderr.write("Specify input file as the first argument and output file as the second.\n")
  sys.stderr.write("Usage: python %s input-file output-file\n")
  sys.exit(1)

if not os.path.exists(sys.argv[1]):
    sys.exit('ERROR: Input file %s was not found!' % sys.argv[1])

FILE = sys.argv[1]
FILE_OUT = sys.argv[2]

def alg(data, y, x):
  #check the surrounding and the tile itself too
  whites = 0
  blacks = 0
  for i in range(-1,2): # [-1, 0, 1]
    for j in range(-1,2):
      if data[y+i][x+j] == 'w':
        whites += 1
      else:
        blacks += 1
  
  #answer
  return 'b' if blacks > whites else 'w'

def print_matrix(matrix):
  for line in matrix:
    print line

with open(FILE, 'rb') as inputfile:
  #parsing
  no_of_testcases = int(inputfile.readline())
  print "no of testcases:%i" % (no_of_testcases)
  data = []
  
  for i in range(0, no_of_testcases):
    meta = inputfile.readline().split(' ')
    size = int(meta[0])
    iterations = int(meta[1])
    
    print "size %i" % size
    matrix = []
    for j in range(0, size):
      line = inputfile.readline().strip()
      matrix.append(list(line))
    
    data.append(matrix)
    
    for ii in range(0, iterations):
      print 'Board:%i iteration:%i' % (i+1, ii+1)
      # alg
      matrix = data[i]
      newmatrix = copy.deepcopy(matrix) # deep copying!
      size = len(matrix)
      for y in range(1,size-1):
        for x in range(1,size-1):
          newmatrix[y][x] = alg(matrix, y, x)
      
      print_matrix(matrix)
      print '>>>'
      print_matrix(newmatrix)
      
      data[i] = newmatrix # replace with the processed matrix
    
  
  #output
  with open(FILE_OUT, 'wb') as outfile:
    for i in range(0, len(data)):
      outfile.write('Board %i\n' % (i+1))
      matrix = data[i]
      for j in range(0,len(matrix)):
        line = matrix[j]
        outfile.write(''.join(line) + '\n')