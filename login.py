from qiskit_ibm_runtime import QiskitRuntimeService

key= 'hidden'
 
QiskitRuntimeService.save_account(
    channel="ibm_quantum",
    token=key,
    set_as_default=True,
    overwrite=True,
)
service = QiskitRuntimeService() 