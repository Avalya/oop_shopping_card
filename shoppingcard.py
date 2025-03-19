class Device:
   
    def __init__(self, name, price, stock, warranty_period):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty_period = warranty_period

    def display_info(self):
       
        print(f"Name: {self.name}, Price: ${self.price}, Stock: {self.stock}, Warranty: {self.warranty_period} months")

    def __str__(self):
        return f"{self.name} - ${self.price}, Stock: {self.stock}, Warranty: {self.warranty_period} months"

    def apply_discount(self, discount_percentage):
        self.price *= (1 - discount_percentage / 100)

    def is_available(self, amount):
        return self.stock >= amount

    def reduce_stock(self, amount):
        if self.is_available(amount):
            self.stock -= amount
            return True
        else:
            return False

class Smartphone(Device):
    def __init__(self, name, price, stock, warranty_period, screen_size, battery_life):
        super().__init__(name, price, stock, warranty_period)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def display_info(self):
        super().display_info()
        print(f"Screen Size: {self.screen_size} inches, Battery Life: {self.battery_life} hours")

    def __str__(self):
        return f"{super().__str__()} - Screen Size: {self.screen_size} inches, Battery Life: {self.battery_life} hours"

    def make_call(self):
        print(f"{self.name}: Making a call.")

    def install_app(self):
        print(f"{self.name}: Installing an app.")

class Laptop(Device):
    def __init__(self, name, price, stock, warranty_period, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty_period)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def display_info(self):
        super().display_info()
        print(f"RAM: {self.ram_size} GB, Processor: {self.processor_speed} GHz")

    def __str__(self):
        return f"{super().__str__()} - RAM: {self.ram_size} GB, Processor: {self.processor_speed} GHz"

    def run_program(self):
        print(f"{self.name}: Running a program.")

    def use_keyboard(self):
        print(f"{self.name}: Using the keyboard.")

class Tablet(Device):
    def __init__(self, name, price, stock, warranty_period, screen_resolution, weight):
        super().__init__(name, price, stock, warranty_period)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def display_info(self):
        super().display_info()
        print(f"Screen Resolution: {self.screen_resolution}, Weight: {self.weight} grams")

    def __str__(self):
        return f"{super().__str__()} - Screen Resolution: {self.screen_resolution}, Weight: {self.weight} grams"

    def browse_internet(self):
        print(f"{self.name}: Browsing the internet.")

    def use_touchscreen(self):
        print(f"{self.name}: Using the touchscreen.")

class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount
            device.reduce_stock(amount)
            print(f"{amount} x {device.name} added to cart.")
        else:
            print(f"Insufficient stock for {device.name}.")

    def remove_device(self, device, amount):
        for item in self.items:
            if item[0] == device:
                if amount >= item[1]:
                    self.total_price -= device.price * item[1]
                    self.items.remove(item)
                    print(f"All {item[1]} x {device.name} removed from cart.")
                else:
                    self.total_price -= device.price * amount
                    item = (device, item[1] - amount)
                    print(f"{amount} x {device.name} removed from cart.")

                return
        print(f"{device.name} not found in cart.")

    def get_total_price(self):
        return self.total_price

    def print_items(self):
        if not self.items:
            print("Cart is empty.")
            return

        print("--- Cart Items ---")
        for device, amount in self.items:
            print(f"{amount} x {device.name} - ${device.price * amount}")
        print(f"Total: ${self.total_price}")

    def checkout(self):
        if not self.items:
            print("Cart is empty. Nothing to checkout.")
            return

        print("--- Checkout ---")
        self.print_items()
        print("Thank you for your purchase!")
        self.items = []
        self.total_price = 0

def main():
    devices = [
        Smartphone("iPhone 15", 999, 10, 12, 6.1, 20),
        Smartphone("Samsung Galaxy S23", 899, 15, 12, 6.6, 22),
        Laptop("MacBook Pro", 1999, 5, 24, 16, 3.2),
        Laptop("Dell XPS 13", 1499, 8, 24, 8, 2.8),
        Tablet("iPad Air", 599, 20, 12, "2360x1640", 461),
        Tablet("Samsung Tab S8", 649, 12, 12, "2560x1600", 503),
        Smartphone("Google Pixel 7", 799, 7, 12, 6.3, 21),
        Laptop("HP Spectre x360", 1699, 6, 24, 16, 3.0),
        Tablet("Amazon Fire HD 10", 149, 30, 12, "1920x1200", 465),
        Smartphone("OnePlus 11", 699, 18, 12, 6.7, 23),
        Laptop("Lenovo ThinkPad X1", 1799, 4, 36, 16, 2.7),
        Tablet("Microsoft Surface Go 3", 399, 15, 12, "1920x1280", 544),
        Smartphone("Xiaomi 13", 749, 11, 12, 6.36, 19),
        Laptop("ASUS ROG Zephyrus", 1899, 3, 24, 16, 3.3),
        Tablet("Lenovo Tab P11", 249, 25, 12, "2000x1200", 490),
        Smartphone("Vivo X90", 649, 14, 12, 6.78, 20),
        Laptop("Acer Swift 5", 1299, 6, 24, 8, 2.4),
        Tablet("Huawei MatePad", 349, 22, 12, "2000x1200"),
    ]