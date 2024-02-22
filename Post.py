import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import User

class PostFactory:

    def create_post(user, post_type, *args):
        temp = args[0]
        list_data= list(temp)

        if post_type == "Text":
            return TextPost(user,list_data[0])
        elif post_type == "Image":
            return ImagePost(user, list_data[0])
        elif post_type == "Sale":
            temp2= SalePost(user, list_data[0], list_data[1],list_data[2])
            return temp2
        else:
            raise ValueError("Invalid post type")

class Post:
    def __init__(self, user):
        self.owner = user
        self.comments = []
        self.likes = []

    def like(self, new_user):
        if new_user not in self.likes:
            self.likes.append(new_user)
        message = f"{new_user.username} liked your post"
        if new_user != self.owner:
           self.owner.update(message)

    def comment(self, new_user, new_comment):
        self.comments.append(new_comment)
        message = f"{new_user.username} commented on your post: {new_comment}"
        self.owner.update(message)


class TextPost(Post):
    def __init__(self, user, text):
        super().__init__(user)
        self.data = text

    def __str__(self):
        return self.owner.username + " published a post:\n" + self.data + "\n"


class ImagePost(Post):
    def __init__(self, user, path):
        super().__init__(user)
        self.image_path = path

    def display(self):
        img = mpimg.imread(self.image_path)
        plt.imshow(img)
        plt.axis('off')  # Turn off axis
        plt.show()

    def __str__(self):
        return self.owner.username + " posted a picture\n"


class SalePost(Post):
    def __init__(self, user, description, price, place):
        super().__init__(user)
        self.description = description
        self.price = price
        self.place = place
        self.availability = True

    def __str__(self):
       return self.owner.username + " posted a product for sale:\n" + self.description + ", price: " + str(self.price) + ", pick up from: " + self.place

    def discount(self, discount_percent, password):
        try:
            if self.owner.password == password:
                self.price = ((100 - discount_percent) / 100) * self.price
                print("Discount on " + self.owner.username + "'s product! The new price is: " + str(self.price))
            else:
                raise ValueError("Invalid password. Price update failed.")
        except AttributeError:
            raise AttributeError("Owner has no password set.")

    def sold(self, password):
        try:
            if self.owner.password == password:
                self.availability = False
                print(self.owner.username + "'s product is sold")
            else:
                raise ValueError("Invalid password. Availability update failed.")
        except AttributeError:
            raise AttributeError("Owner has no password set.")