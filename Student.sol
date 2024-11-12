// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentAdd {
    // Structure to store student data
    struct Student {
        string name;
        uint256 rollno;
    }

    Student[] public studentarr;

    // Mapping to store student by roll number for quick lookup
    mapping(uint256 => Student) private studentsByRollNo;

    // Function to add a student
    function addStudent(string memory name, uint256 rollno) public {
        // Check if a student with the given roll number already exists
        require(studentsByRollNo[rollno].rollno == 0, "Student with this roll number already exists");

        // Create new student and push to array
        Student memory newStudent = Student(name, rollno);
        studentarr.push(newStudent);

        // Add student to the mapping for quick access by roll number
        studentsByRollNo[rollno] = newStudent;
    }

    // Function to get the total number of students
    function getStudentsLength() public view returns (uint256) {
        return studentarr.length;
    }

    // Function to display all students
    function displayAllStudents() public view returns (Student[] memory) {
        return studentarr;
    }

    // Function to get a student by roll number
    function getStudentByRollNo(uint256 rollno) public view returns (string memory name, uint256 roll) {
        require(studentsByRollNo[rollno].rollno != 0, "Student not found");
        Student memory student = studentsByRollNo[rollno];
        return (student.name, student.rollno);
    }

    // Fallback function
    fallback() external payable {}

    // Receive function to accept Ether
    receive() external payable {}
}


//install metamask
change to testnet sepolia
open sepolia faucet and paste wallet address
in remix deploy tab open environment and select connected wallets
then deploy


Structures: Structures (or structs) in Solidity allow us to create complex data types. In this problem, we'll create a Student struct to hold student information such as name and roll number.

Arrays: Arrays will be used to store multiple student records. We can use either dynamic or fixed-size arrays; in this case, a dynamic array allows us to add as many students as needed.

Fallback Function: The fallback function is a special function in Solidity that gets executed when a contract receives Ether without any data. This is useful for making the contract capable of accepting payments or handling unexpected interactions gracefully.

Key Concepts
Structs: They help in creating user-defined data types. In this program, we use a struct to represent a student entity with a name and roll number.

Dynamic Arrays: We will use a dynamic array to store student structs. This makes it possible to add new entries dynamically during runtime.

Fallback and Receive Functions: These functions allow the contract to accept Ether payments, demonstrating that contracts can handle payments alongside data operations.

Gas Costs: Every transaction on the Ethereum blockchain requires gas, which is a measure of computational work. Deploying a smart contract, calling functions, and writing to storage all consume gas. Observing gas costs helps in optimizing contracts to make them cost-efficient
