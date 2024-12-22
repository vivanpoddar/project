from qiskit_nature.units import DistanceUnit
from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_algorithms import NumPyMinimumEigensolver
from qiskit_nature.second_q.algorithms import GroundStateEigensolver
from qiskit_nature.second_q.mappers import JordanWignerMapper
import time

start_time = time.time()

driver = PySCFDriver(
    #atom="H 0 0 0; H 0 0 0.735",
    #atom="O 0 0 0; H 0.757 0.586 0; H -0.757 0.586 0",
    atom="C 0 0 0; H 0.629 0.629 0.629; H -0.629 -0.629 0.629; H -0.629 0.629 -0.629; H 0.629 -0.629 -0.629",
    #atom="C 0 0 0; C 1.54 0 0; H 0.629 0.629 0.629; H -0.629 -0.629 0.629; H -0.629 0.629 -0.629; H 2.169 0.629 0.629; H 0.911 -0.629 0.629; H 0.911 0.629 -0.629"
    #atom="C 0 0 0; C 1.54 0 0; C 3.08 0 0; H 0.629 0.629 0.629; H -0.629 -0.629 0.629; H -0.629 0.629 -0.629; H 2.169 0.629 0.629; H 0.911 -0.629 0.629; H 0.911 0.629 -0.629; H 3.709 0.629 0.629; H 2.451 -0.629 0.629; H 2.451 0.629 -0.629"
    #atom="C 0 0 0; C 1.54 0 0; C 3.08 0 0; C 4.62 0 0; H 0.629 0.629 0.629; H -0.629 -0.629 0.629; H -0.629 0.629 -0.629; H 2.169 0.629 0.629; H 0.911 -0.629 0.629; H 0.911 0.629 -0.629; H 3.709 0.629 0.629; H 2.451 -0.629 0.629; H 2.451 0.629 -0.629; H 5.249 0.629 0.629; H 3.541 -0.629 0.629; H 3.541 0.629 -0.629"
    #atom="C 0 0 0; C 1.54 0 0; C 3.08 0 0; C 4.62 0 0; C 6.16 0 0; H 0.629 0.629 0.629; H -0.629 -0.629 0.629; H -0.629 0.629 -0.629; H 2.169 0.629 0.629; H 0.911 -0.629 0.629; H 0.911 0.629 -0.629; H 3.709 0.629 0.629; H 2.451 -0.629 0.629; H 2.451 0.629 -0.629; H 5.249 0.629 0.629; H 3.541 -0.629 0.629; H 3.541 0.629 -0.629; H 6.789 0.629 0.629; H 5.081 -0.629 0.629; H 5.081 0.629 -0.629"
    #atom="C 0 0 0; C 1.54 0 0; C 3.08 0 0; C 4.62 0 0; C 6.16 0 0; C 7.7 0 0; H 0.629 0.629 0.629; H -0.629 -0.629 0.629; H -0.629 0.629 -0.629; H 2.169 0.629 0.629; H 0.911 -0.629 0.629; H 0.911 0.629 -0.629; H 3.709 0.629 0.629; H 2.451 -0.629 0.629; H 2.451 0.629 -0.629; H 5.249 0.629 0.629; H 3.541 -0.629 0.629; H 3.541 0.629 -0.629; H 6.789 0.629 0.629; H 5.081 -0.629 0.629; H 5.081 0.629 -0.629; H 8.329 0.629 0.629; H 6.621 -0.629 0.629; H 6.621 0.629 -0.629"
    basis="sto3g",
    charge=0,
    spin=0,
    unit=DistanceUnit.ANGSTROM,
)

problem = driver.run()
print(problem)

solver = GroundStateEigensolver(
    JordanWignerMapper(),
    NumPyMinimumEigensolver(),
)

result = solver.solve(problem)
print(result)

end_time = time.time()
elapsed_time = end_time - start_time
print("Total wall time:", elapsed_time*1000, "ms")