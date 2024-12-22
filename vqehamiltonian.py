from qiskit_nature.units import DistanceUnit
from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.second_q.mappers import JordanWignerMapper
from qiskit.quantum_info import SparsePauliOp

driver = PySCFDriver(
    atom="H 0 0 0; H 0 0 0.735",
    basis="6-31g",
    charge=0,
    spin=0,
    unit=DistanceUnit.ANGSTROM,
)

problem = driver.run()
print(problem)

hamiltonian = problem.hamiltonian.second_q_op()

mapper = JordanWignerMapper()
qubit_hamiltonian = mapper.map(hamiltonian)

sparse_pauli_op = SparsePauliOp(qubit_hamiltonian)
