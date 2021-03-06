class Customer:
    name: str
    address: str
    email: str
    auto_incremented_id: int = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.auto_incremented_id
        Customer.auto_incremented_id += 1

    @staticmethod
    def get_next_id():
        return Customer.auto_incremented_id

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; " \
               f"Address: {self.address}; " \
               f"Email: {self.email}"
