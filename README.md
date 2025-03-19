# Electronic Device Shopping Cart

This project implements a shopping cart system for electronic devices, demonstrating the use of inheritance in Object-Oriented Programming (OOP).

## Project Structure
## Classes

### `Device`

Base class for all electronic devices.

**Attributes:**

* `name` (str): The name of the device.
* `price` (float): The price of the device.
* `stock` (int): The number of units available.
* `warranty_period` (int): The warranty period in months.

**Methods:**

* `__init__(self, name, price, stock, warranty_period)`: Initializes a new Device object.
* `display_info(self)`: Displays basic device information.
* `__str__(self)`: Returns a string representation of the device.
* `apply_discount(self, discount_percentage)`: Applies a discount to the device price.
* `is_available(self, amount)`: Checks if the device is available in the given quantity.
* `reduce_stock(self, amount)`: Reduces the stock of the device.

### `Smartphone`, `Laptop`, `Tablet`

Subclasses of `Device` with additional attributes and methods specific to each device type.

### `Cart`

Represents a shopping cart.

**Attributes:**

* `items` (list): A list of tuples, where each tuple contains a device and the amount being purchased.
* `total_price` (float): The total price of all devices in the cart.

**Methods:**

* `__init__(self)`: Initializes an empty Cart object.
* `add_device(self, device, amount)`: Adds a device to the cart.
* `remove_device(self, device, amount)`: Removes a device from the cart.
* `get_total_price(self)`: Returns the total price of the cart.
* `print_items(self)`: Prints the items in the cart.
* `checkout(self)`: Processes the checkout.

## How to Run

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd electronic-device-shopping-cart
    ```
2.  **Run the Application:**
    ```bash
    python src/shoppingcard_py.py
    ```
3.  **Run Tests:**
    ```bash
    python -m unittest tests/test_electronic_store.py
    ```

## Sample Runs

Include sample runs (input and output) here. You can either use text examples or screenshots.

## UML Class Diagram

Include a UML class diagram here (e.g., as an image file).
