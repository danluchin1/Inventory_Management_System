# Inventory_Management_System

### Description
The Inventory Management System is a user-friendly application designed to help businesses efficiently manage their inventory. Built using Python for the backend, HTML and JavaScript for the frontend, and a SQLite database for data storage, the system allows users to perform essential inventory tasks such as:

* User Authentication: Secure login and registration system to ensure only authorized users can access inventory management features.
* Item Management: Add, update, and delete products in the inventory, with real-time feedback on stock levels.
* Transaction Logging: Track transactions related to inventory, including sales and purchases, for accurate stock management.
* Graphical User Interface (GUI): An intuitive interface created with Tkinter, allowing users to interact with the application seamlessly.
* Dynamic Data Display: Automatically refresh the inventory list to show real-time updates after adding or modifying items.

Overall, this application streamlines inventory control processes, improves accuracy in stock management, and enhances productivity for users managing their inventory.

### Prerequisites
Before running the application, ensure you have the following installed:

* Python 3.x
* SQLite (comes pre-installed with Python)
* Tkinter (usually included with Python installations)
* pip (Python package manager)

### Installation steps
1. Clone the repository
   * git clone https://github.com/danluchin1/Inventory_Management_System
   * cd inventory-management-system
2. Set Up the Database
   * Navigate to the database.py file and run it to set up the SQLite database and create the necessary tables: python database.py
3. Run the Application
   *Start the application by running the main.py file: python main.py
4. Access the Application
   * After running main.py, a login window will appear. Enter your credentials or register a new account to access the Inventory Management System.

### Usage
Use the application to manage your inventory by adding new items, updating existing ones, or deleting items as needed. The inventory list will automatically refresh to reflect changes.

## Reflection on Developing an Inventory Management System Using the Waterfall Model
For this project, we followed the Waterfall Software Development Life Cycle (SDLC) model to create a Python-based Inventory Management System tailored to small business needs. The sequential nature of the Waterfall model was ideal, given our well-defined requirements, as it allowed us to maintain a structured approach throughout development.

### Phase Reflections
1. **Requirements Documentation (Software Requirements Specification - SRS)**
   In the requirement analysis phase, we created a comprehensive Software Requirements Specification (SRS) document. This document outlined our system's objectives, scope, core functionalities, and specific requirements, including user authentication, inventory management, stock control, and transaction logging. Establishing a clear SRS ensured that all team members were aligned with the project’s goals, reducing misunderstandings later in the project.
2. **Design Documentation**
   During the system design phase, we produced both high-level and low-level design documentation to guide our implementation. The high-level design included an architectural overview, detailing the system’s components and their interactions. At the low level, we defined the structure of our SQLite database, which featured tables for items, transactions, and users, as well as the GUI layout using Tkinter. This documentation served as a blueprint, helping us maintain consistency and structure throughout development.
3. **Working Software**
   Our implementation phase followed the design specifications closely, resulting in a working Inventory Management System. This system met all defined requirements, allowing users to add, update, and view items, manage stock levels, and log transactions. By adhering to the Waterfall model’s structured approach, we were able to implement each feature methodically and efficiently, minimizing the need for revisions.
4. **Test Plans and Results**
   In the testing phase, we developed detailed test plans that included both unit and integration tests. We created test cases for individual modules (e.g., adding items, updating stock, user login) and then conducted integration tests to ensure that components interacted correctly. Any bugs found were logged in a bug-tracking report, which helped us efficiently resolve issues. While the Waterfall model’s approach limits testing to a specific phase, our pre-defined test plans helped ensure thorough validation of system functionality.
5. **Documentation**
   To accompany our final product, we developed structured documentation that explains the software’s functionality, architecture, and usage. This documentation includes a user guide covering installation, login, and the core features of the system, as well as a technical document outlining database design, system architecture, and module interactions. This documentation will support both users and future developers in understanding and maintaining the system.

### Reflection on the Waterfall Model’s Suitability
The Waterfall model was well-suited to this project due to the stability of our requirements and the relatively straightforward nature of an inventory management system. Its linear, phase-based approach allowed us to work systematically, with each phase setting the foundation for the next. This structure helped us remain organized and ensured that all requirements were fulfilled before moving to the next stage.

One challenge with Waterfall was its limited flexibility for incorporating changes after initial requirements were finalized. Since the model’s structure did not allow for iterative revisions, any substantial change in requirements would have required reworking several completed phases. This rigidity would be less ideal for projects with evolving requirements, where an iterative model might provide more flexibility.

In summary, developing this Inventory Management System with the Waterfall model allowed us to experience a real-world SDLC approach in a controlled, structured manner. By clearly documenting requirements, designs, test results, and final usage instructions, we created a reliable, well-documented product that met our objectives. This experience emphasized the importance of thorough planning, detailed documentation, and careful phase-based progression in achieving successful software delivery.
