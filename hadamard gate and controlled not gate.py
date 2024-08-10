from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer

# Create a quantum circuit with two qubits
qc = QuantumCircuit(2)

# Apply the Hadamard gate to the first qubit
qc.h(0)

# Apply the CNOT gate with qubit 0 as control and qubit 1 as target
qc.cx(0, 1)

# Draw the circuit
qc.draw('mpl')
