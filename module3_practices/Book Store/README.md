Step 1:

For this you are creating a Book() class.

It should have the fields title, quantity, author, genre, price, and discount. Discount should default to None.

There should be four methods.
set_discount => which sets the discount amount for this book.
get_price => which returns the price (and applies any discounts if applicable)
**repr** => This should return the string expected when the book is called. Title: {}, Qty: {}, Author: {}, Price {}
purchase => which should use get_price, return the currency string of the book and removes one from the quantity. It should raise an error if you were to purchase a book that is at 0 qty.

Step 2:

For this you are creating 2 subclasses.

The first subclass is Textbook(Book).

It should take in all the fields and methods of the parent class but additionally take in a topic field.

The second subclass is Comic(Book).

It should take in all the fields and methods of the parent class but additionally take in a publisher field.
