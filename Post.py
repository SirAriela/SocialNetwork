import matplotlib.pyplot as plt
import matplotlib.image as mpimg
class Post:

    def __init__(self, username):
        self.owner = username
        self.comments = []
        self.likes = []

    def update_likes(self, new_user):
        if new_user not in self.likes:
            self.likes.append(new_user)

    def add_comment(self, new_comment):
        self.comments.append(new_comment)

class TextPost(Post):
    def __init__(self, username, text):
        self.data = text
        super().__init__(username)

    def print_post(self):
        print(self.owner + " published a post:\n" + self.data)


class ImagePost(Post):
    def __init__(self, image_path):
        self.image = image_path
        super().__init__()

    def display_image(self):
        img = mpimg.imread(self.image_path)
        plt.imshow(img)
        plt.axis('off')  # Turn off axis
        plt.show()

    def print_post(self):
        print(self.owner + " posted a picture")

class SalePost(Post):
    def __init__(self, username, description, price, place, availability):
        self.description = description
        self.price = price
        self.place = place
        self.availability = availability
        super().__init__(username)

    def print_post(self):
        print(self.owner + " posted a product for sale:\n" + self.description + ", price: " + self.price + ", pick up from: " + self.place)

    def update_price(self, discount_percent, password):
        try:
            if self.owner.password == password:
                self.price = ((100-discount_percent)/100) * self.price
                print("Discount on " + self.owner + "'s product! The new price is: " + str(self.price))
            else:
                raise ValueError("Invalid password. Price update failed.")
        except AttributeError:
            raise AttributeError("Owner has no password set.")

    def change_availability(self, password):
        try:
            if self.owner.password == password:
                self.availability = False
                print(self.owner + "'s product is sold")
            else:
                raise ValueError("Invalid password. Availability update failed.")
        except AttributeError:
            raise AttributeError("Owner has no password set.")