# Electronic Device Shopping Cart

This project implements a shopping cart system for an electronic device store, showcasing inheritance and object-oriented programming principles.

## Classes

### Device (Base Class)

Represents a generic electronic device with common attributes and methods.

* `__init__(self, name, price, stock, warranty_period)`: Initializes a device with name, price, stock, and warranty.
* `display_info(self)`: Returns a string with device details.
* `__str__(self)`: Returns the same string as `display_info()`.
* `apply_discount(self, discount_percentage)`: Applies a discount to the device price.
* `is_available(self, amount)`: Checks if the device has enough stock.
* `reduce_stock(self, amount)`: Reduces the device stock after purchase.

### Smartphone (Derived Class)

Represents a smartphone, inheriting from `Device`.

* `__init__(self, name, price, stock, warranty_period, screen_size, battery_life)`: Initializes a smartphone with specific attributes.
* `display_info(self)`: Overrides the base method to include smartphone-specific details.
* `__str__(self)`: Returns the same string as `display_info()`.
* `make_call(self)`: Simulates making a call.
* `install_app(self)`: Simulates installing an app.

### Laptop (Derived Class)

Represents a laptop, inheriting from `Device`.

* `__init__(self, name, price, stock, warranty_period, ram_size, processor_speed)`: Initializes a laptop with specific attributes.
* `display_info(self)`: Overrides the base method to include laptop-specific details.
* `__str__(self)`: Returns the same string as `display_info()`.
* `run_program(self)`: Simulates running a program.
* `use_keyboard(self)`: Simulates typing on the keyboard.

### Tablet (Derived Class)

Represents a tablet, inheriting from `Device`.

* `__init__(self, name, price, stock, warranty_period, screen_resolution, weight)`: Initializes a tablet with specific attributes.
* `display_info(self)`: Overrides the base method to include tablet-specific details.
* `__str__(self)`: Returns the same string as `display_info()`.
* `browse_internet(self)`: Simulates browsing the internet.
* `use_touchscreen(self)`: Simulates using the touchscreen.

### Cart

Represents a shopping cart for managing devices.

* `__init__(self)`: Initializes an empty cart.
* `add_device(self, device, amount)`: Adds a device to the cart if available.
* `remove_device(self, device, amount)`: removes a device from the cart.
* `get_total_price(self)`: Returns the total price of items in the cart.
* `print_items(self)`: Prints the items in the cart.
* `checkout(self)`: Processes the checkout, reduces stock, and prints a receipt.

## UML Class Diagram

```mermaid
classDiagram
    class Device{
        - string name
        - float price
        - int stock
        - int warranty_period
        + __init__(string name, float price, int stock, int warranty_period)
        + string display_info()
        + string __str__()
        + apply_discount(float discount_percentage)
        + bool is_available(int amount)
        + reduce_stock(int amount)
    }
    class Smartphone{
        - float screen_size
        - float battery_life
        + __init__(string name, float price, int stock, int warranty_period, float screen_size, float battery_life)
        + string display_info()
        + string __str__()
        + string make_call()
        + string install_app()
    }
    class Laptop{
        - int ram_size
        - float processor_speed
        + __init__(string name, float price, int stock, int warranty_period, int ram_size, float processor_speed)
        + string display_info()
        + string __str__()
        + string run_program()
        + string use_keyboard()
    }
    class Tablet{
        - string screen_resolution
        - float weight
        + __init__(string name, float price, int stock, int warranty_period, string screen_resolution, float weight)
        + string display_info()
        + string __str__()
        + string browse_internet()
        + string use_touchscreen()
    }
    class Cart{
        - list items
        - float total_price
        + __init__()
        + bool add_device(Device device, int amount)
        + bool remove_device(Device device, int amount)
        + float get_total_price()
        + print_items()
        + checkout()
    }
    Device <|-- Smartphone
    Device <|-- Laptop
    Device <|-- Tablet
    Cart "1" -- "*" Device : contains
